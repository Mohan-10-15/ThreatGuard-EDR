from src.threat_intelligence.signatures import (
    KNOWN_SUSPICIOUS
)


def check_reputation(process_name):

    name = process_name.lower()

    for signature in KNOWN_SUSPICIOUS:

        if signature in name:

            return (
                "SUSPICIOUS",
                90
            )

    return (
        "UNKNOWN",
        0
    )