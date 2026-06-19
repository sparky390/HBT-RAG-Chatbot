import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://hbt-group.com"
START_URL = "https://hbt-group.com/aftermarket-services/technology-services/"


def get_service_links():
    try:
        response = requests.get(
            START_URL,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        urls = set()

        # Always include main page
        urls.add(START_URL)

        for tag in soup.find_all("a", href=True):

            href = tag["href"]

            full_url = urljoin(
                BASE_URL,
                href
            )

            # Remove URL fragments
            full_url = full_url.split("#")[0]

            # Only Technology Services pages
            if full_url.startswith(
                "https://hbt-group.com/aftermarket-services/technology-services/"
            ):
                urls.add(full_url)

        return sorted(list(urls))

    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":

    urls = get_service_links()

    print("\nDiscovered URLs:\n")

    for url in urls:
        print(url)

    print(f"\nTotal URLs Found: {len(urls)}")