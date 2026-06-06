import json
import os
from datetime import datetime

INCIDENT_FILE = os.path.join(
    os.path.dirname(__file__),
    "incident_log.json"
)


def log_incident(
    event_type,
    process_name,
    details
):

    incident = {

        "time":
        datetime.now().strftime(
            "%H:%M:%S"
        ),

        "event":
        event_type,

        "process":
        process_name,

        "details":
        details

    }

    incidents = []

    if os.path.exists(
        INCIDENT_FILE
    ):

        try:

            with open(
                INCIDENT_FILE,
                "r"
            ) as f:

                incidents = json.load(
                    f
                )

        except:

            incidents = []

    incidents.append(
        incident
    )

    with open(
        INCIDENT_FILE,
        "w"
    ) as f:

        json.dump(
            incidents,
            f,
            indent=4
        )


def get_incidents():

    if not os.path.exists(
        INCIDENT_FILE
    ):

        return []

    try:

        with open(
            INCIDENT_FILE,
            "r"
        ) as f:

            return json.load(
                f
            )

    except:

        return []