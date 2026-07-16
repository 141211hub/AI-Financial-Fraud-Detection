from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    filename,
    transaction,
    prediction,
    probability,
    risk,
    summary
):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph(
            "<b>SecureBank AI Investigation Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Prediction:</b> {prediction}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Fraud Probability:</b> {probability}%",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk Level:</b> {risk}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 15))

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
                styles["Normal"]
            )
        )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<b>AI Investigation Summary</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            summary,
            styles["Normal"]
        )
    )

    doc.build(story)