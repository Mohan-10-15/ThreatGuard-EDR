import psutil

from src.monitors.network_monitor import (
    get_connection_count
)

from src.monitors.registry_monitor import (
    scan_registry
)

from src.threat_engine.ai_engine import (
    ai_engine
)

from src.threat_engine.threat_scoring import (
    get_threat_category
)

from src.threat_engine.behavior_engine import (
    analyze_behavior
)

from src.threat_intelligence.reputation_engine import (
    check_reputation
)

from src.threat_intelligence.hash_engine import (
    calculate_sha256
)

from src.threat_intelligence.ioc_engine import (
    check_process_ioc
)

from src.incidents.incident_engine import (
    log_incident
)

from src.utils.logger import (
    log_warning
)

from src.response.quarantine import (
    quarantine_process
)

LATEST_DATA = []

DASHBOARD_STATS = {
    "processes_scanned": 0,
    "threats_detected": 0,
    "critical_threats": 0,
    "registry_entries": 0
}


def get_latest_data():
    return LATEST_DATA


def get_dashboard_stats():
    return DASHBOARD_STATS


def scan_processes():

    global LATEST_DATA
    global DASHBOARD_STATS

    results = []

    threats_detected = 0
    critical_threats = 0

    registry_entries = len(
        scan_registry()
    )

    for proc in psutil.process_iter(
        [
            "pid",
            "name",
            "cpu_percent",
            "memory_percent"
        ]
    ):

        try:

            pid = proc.info["pid"]

            process_name = proc.info["name"]

            cpu = proc.info["cpu_percent"]

            memory = proc.info["memory_percent"]

            connections = get_connection_count(
                pid
            )

            behavior_score, behavior_reasons = (
                analyze_behavior(
                    process_name,
                    cpu,
                    memory,
                    connections
                )
            )

            ioc_match, ioc_severity = (
                check_process_ioc(
                    process_name
                )
            )

            ioc_bonus = 0

            if ioc_match:

                log_incident(
                    "IOC MATCH",
                    process_name,
                    ioc_severity
                )

                if ioc_severity == "CRITICAL":

                    ioc_bonus = 100

                elif ioc_severity == "HIGH":

                    ioc_bonus = 75

            try:

                process_path = proc.exe()

            except:

                process_path = None

            if process_path:

                file_hash = calculate_sha256(
                    process_path
                )

            else:

                file_hash = "UNAVAILABLE"

            score = ai_engine.predict_score(
                cpu,
                memory,
                connections
            )

            reputation, reputation_bonus = (
                check_reputation(
                    process_name
                )
            )

            score += reputation_bonus

            score += ioc_bonus

            score += behavior_score

            if score > 100:

                score = 100

            category = get_threat_category(
                score
            )

            if category in [
                "MEDIUM",
                "HIGH",
                "CRITICAL"
            ]:

                threats_detected += 1

            if category == "CRITICAL":

                critical_threats += 1

                log_warning(
                    f"CRITICAL THREAT | "
                    f"{process_name} | "
                    f"PID {pid} | "
                    f"Score {score}"
                )

                log_incident(
                    "CRITICAL THREAT",
                    process_name,
                    f"Score {score}"
                )

                if score >= 90:

                    quarantine_process(
                        pid,
                        process_name,
                        score
                    )

                    log_incident(
                        "QUARANTINED",
                        process_name,
                        f"PID {pid}"
                    )

            results.append({

                "pid": pid,

                "name": process_name,

                "path": process_path,

                "sha256": file_hash,

                "cpu": cpu,

                "memory": memory,

                "connections": connections,

                "score": score,

                "category": category,

                "reputation": reputation,

                "ioc_match": ioc_match,

                "ioc_severity": ioc_severity,

                "behavior_score": behavior_score,

                "behavior_reasons": behavior_reasons

            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):

            continue

    LATEST_DATA = results

    DASHBOARD_STATS = {

        "processes_scanned":
        len(results),

        "threats_detected":
        threats_detected,

        "critical_threats":
        critical_threats,

        "registry_entries":
        registry_entries

    }