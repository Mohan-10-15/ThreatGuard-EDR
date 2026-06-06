import os
from datetime import datetime

REPORTS_DIR = "reports"

if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

INCIDENT_LOG = os.path.join(
    REPORTS_DIR,
    "incidents.log"
)


def log_incident(
    process_name,
    pid,
    score,
    action
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        INCIDENT_LOG,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"\n{'='*50}\n"
            f"Time: {timestamp}\n"
            f"Process: {process_name}\n"
            f"PID: {pid}\n"
            f"Threat Score: {score}\n"
            f"Action: {action}\n"
        )