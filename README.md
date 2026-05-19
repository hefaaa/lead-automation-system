# lead-automation-system

# AI-Powered Lead Automation System

## Overview

This project automates the complete lead intake and company audit workflow.

When a user submits a company form, the system automatically:

- Captures lead information
- Scrapes company website data
- Generates AI-powered business insights
- Creates a professional PDF audit report
- Emails the report to the prospect

The workflow runs fully automatically without human intervention.

---

# Features

- Lead intake form
- Website scraping
- AI-generated business analysis
- Professional PDF generation
- Automated email delivery
- End-to-end workflow automation

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- FastAPI (Python)

## AI
- Groq API
- Llama 3.3 70B model

## PDF Generation
- ReportLab

## Email Service
- Resend API

---

# Project Structure

```bash
lead-automation/
│
├── backend/
│   ├── main.py
│   ├── ai_generator.py
│   ├── scraper.py
│   ├── pdf_generator.py
│   ├── email_sender.py
│   └── .env
│
├── frontend/
│   └── index.html
│
├── generated_reports/
│
├── requirements.txt
│
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repo_url>
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create `.env` inside backend folder:

```env
GROQ_API_KEY=your_groq_api_key
RESEND_API_KEY=your_resend_api_key
```

---

## 4. Run Backend

```bash
uvicorn main:app --reload
```

---

## 5. Run Frontend

Open:

```text
frontend/index.html
```

in browser.

---

# Workflow

1. User submits lead form
2. Backend validates data
3. Website content is scraped
4. AI generates business insights
5. PDF report is created
6. Email with report is sent automatically

---

# Future Improvements

- Google Sheets lead logging
- Google Drive PDF storage
- Better website enrichment APIs
- Dashboard analytics
- Improved PDF branding

---

# Author

Haifa Rubina
