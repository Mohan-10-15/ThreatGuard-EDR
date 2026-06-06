import os
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


REPORT_DIR = os.path.join(
    "reports",
    "reports_pdf"
)

os.makedirs(
    REPORT_DIR,
    exist_ok=True
)


def generate_report(stats):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    filename = os.path.join(
        REPORT_DIR,
        f"ThreatGuard_Report_{timestamp}.pdf"
    )

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "ThreatGuard EDR Incident Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Generated: {datetime.now()}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            f"Processes Scanned: "
            f"{stats['processes_scanned']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Threats Detected: "
            f"{stats['threats_detected']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Critical Threats: "
            f"{stats['critical_threats']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Registry Entries: "
            f"{stats['registry_entries']}",
            styles["Normal"]
        )
    )

    doc.build(content)

    return filename