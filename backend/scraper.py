import requests
from bs4 import BeautifulSoup

def scrape_website(url):

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else ""

        paragraphs = soup.find_all("p")

        text = " ".join(
            [p.get_text() for p in paragraphs[:10]]
        )

        return f"""
        Website Title: {title}

        Website Content:
        {text}
        """

    except Exception as e:
        return f"Could not scrape website: {str(e)}"