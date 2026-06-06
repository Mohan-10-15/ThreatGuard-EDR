def get_threat_category(score):

    if score < 25:
        return "SAFE"

    elif score < 50:
        return "LOW"

    elif score < 70:
        return "MEDIUM"

    elif score < 85:
        return "HIGH"

    return "CRITICAL"