from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from scraper import scrape_website
from ai_generator import generate_insights
from pdf_generator import create_pdf
from email_sender import send_email

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lead Form Model
class Lead(BaseModel):
    name: str
    email: str
    company: str
    website: str


@app.get("/")
async def root():
    return {"message": "Backend running successfully"}


@app.post("/submit-lead")
async def submit_lead(lead: Lead):

    print("Received Lead:")
    print(lead)

    # STEP 1 - SCRAPE WEBSITE
    scraped_data = scrape_website(lead.website)

    print("SCRAPED DATA:")
    print(scraped_data)

    # STEP 2 - GENERATE AI INSIGHTS
    insights = generate_insights(
        company=lead.company,
        website=lead.website,
        content=scraped_data
    )

    print("AI INSIGHTS GENERATED")

    # STEP 3 - GENERATE PDF
    pdf_path = create_pdf(
        lead.company,
        insights
    )

    print("PDF GENERATED:", pdf_path)

    # STEP 4 - SEND EMAIL
    send_email(
        to_email=lead.email,
        company=lead.company,
        pdf_path=pdf_path
    )

    print("EMAIL SENT")

    return {
        "status": "success",
        "message": "Audit generated and emailed successfully"
    }