import psutil

from src.response.incident_handler import (
    log_incident
)


def quarantine_process(
    pid,
    process_name,
    score
):

    try:

        process = psutil.Process(pid)

        process.terminate()

        try:
            process.wait(timeout=3)
        except:
            process.kill()

        log_incident(
            process_name,
            pid,
            score,
            "QUARANTINED"
        )

        return True

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied,
        psutil.ZombieProcess
    ):
        return False