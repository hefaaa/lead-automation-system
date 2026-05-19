from dotenv import load_dotenv
load_dotenv()

import resend
import os
import base64

resend.api_key = os.getenv("RESEND_API_KEY")


def send_email(to_email, company, pdf_path):

    with open(pdf_path, "rb") as f:

        pdf_content = base64.b64encode(
            f.read()
        ).decode("utf-8")

    resend.Emails.send({

        "from": "delivered@resend.dev",

        "to": to_email,

        "subject": f"{company} AI Audit Report",

        "html": f"""
        <h2>Your Personalized Audit Report</h2>

        <p>
        Please find attached your AI-generated company audit report.
        </p>
        """,

        "attachments": [
            {
                "filename": f"{company}.pdf",
                "content": pdf_content
            }
        ]
    })

    print("EMAIL SENT SUCCESSFULLY")