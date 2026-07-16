from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path
from datetime import datetime


def generate_report(
    prediction,
    probability,
    risk,
    transaction,
    explanation,
    summary
):
    """
    Generates a professional PDF report.
    """

    reports_folder = Path("../reports")
    reports_folder.mkdir(exist_ok=True)

    filename = reports_folder / f"Fraud_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(str(filename))

    styles = getSampleStyleSheet()

    story = []

    # ---------------- Title ---------------- #

    story.append(
        Paragraph("<b>SecureBank AI</b>", styles["Title"])
    )

    story.append(
        Paragraph(
            "Financial Fraud Investigation Report",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 20))

    # ---------------- Prediction ---------------- #

    story.append(
        Paragraph(
            f"<b>Prediction:</b> {prediction}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Fraud Probability:</b> {probability:.2f}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk Level:</b> {risk}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # ---------------- Transaction ---------------- #

    story.append(
        Paragraph(
            "<b>Transaction Details</b>",
            styles["Heading2"]
        )
    )

    for key, value in transaction.items():

        story.append(
            Paragraph(
                f"{key}: {value}",
                styles["BodyText"]
            )
        )

    story.append(Spacer(1, 20))

    # ---------------- SHAP ---------------- #

    story.append(
        Paragraph(
            "<b>Top Contributing Features</b>",
            styles["Heading2"]
        )
    )

    for item in explanation[:10]:

        story.append(
            Paragraph(
                f"{item['feature']} : {item['impact']:.4f}",
                styles["BodyText"]
            )
        )

    story.append(Spacer(1, 20))

    # ---------------- AI Summary ---------------- #

    story.append(
        Paragraph(
            "<b>AI Investigation Summary</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # ---------------- Footer ---------------- #

    story.append(
        Paragraph(
            f"Generated on {datetime.now()}",
            styles["Italic"]
        )
    )

    doc.build(story)

    return str(filename)