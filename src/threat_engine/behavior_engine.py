import os


SUSPICIOUS_PROCESSES = [

    "powershell.exe",

    "cmd.exe",

    "wscript.exe",

    "cscript.exe",

    "rundll32.exe",

    "regsvr32.exe"

]


def analyze_behavior(
    process_name,
    cpu,
    memory,
    connections
):

    score = 0

    reasons = []

    process_name = process_name.lower()

    if process_name in SUSPICIOUS_PROCESSES:

        score += 20

        reasons.append(
            "Suspicious System Tool"
        )

    if cpu > 70:

        score += 20

        reasons.append(
            "High CPU Usage"
        )

    if memory > 20:

        score += 15

        reasons.append(
            "High Memory Usage"
        )

    if connections > 30:

        score += 25

        reasons.append(
            "Excessive Network Activity"
        )

    if (
        cpu > 70
        and
        connections > 30
    ):

        score += 20

        reasons.append(
            "CPU + Network Correlation"
        )

    return (
        score,
        reasons
    )