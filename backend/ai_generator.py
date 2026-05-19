from dotenv import load_dotenv
load_dotenv()

from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_insights(company, website, content):

    print("Generating AI insights with Groq...")

    prompt = f"""
    You are a senior business consultant and AI strategy advisor.

    Analyze this company deeply.

    COMPANY:
    {company}

    WEBSITE:
    {website}

    WEBSITE CONTENT:
    {content[:2000]}

    Generate a detailed professional audit report with LONG PARAGRAPHS covering:

    1. Executive Summary
    2. Business Strengths
    3. Potential Challenges
    4. AI Automation Opportunities
    5. Customer Experience & Digital Presence
    6. Strategic Recommendations

    Make the report:
    - professional
    - detailed
    - company-specific
    - consulting-style
    - easy to read
    """

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7
        )

        result = response.choices[0].message.content

        print("AI generation successful")

        return result

    except Exception as e:

        print("GROQ ERROR:")
        print(str(e))

        return f"""
        AI generation failed:

        {str(e)}
        """