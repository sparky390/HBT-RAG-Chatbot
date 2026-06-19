import requests
import os
import json

from bs4 import BeautifulSoup
from datetime import datetime

from crawler import get_service_links

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)
os.makedirs("data/metadata", exist_ok=True)

urls = get_service_links()

for index, url in enumerate(urls):

    try:

        response = requests.get(url)

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        file_name = f"page_{index}"

        # RAW HTML
        with open(
            f"data/raw/{file_name}.html",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(response.text)

        # CLEAN TEXT
        text = soup.get_text(
            separator="\n",
            strip=True
        )

        with open(
            f"data/processed/{file_name}.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)

        # METADATA
        metadata = {
            "url": url,
            "title": soup.title.text if soup.title else "",
            "scraped_at": str(datetime.now()),
            "content_length": len(text)
        }

        with open(
            f"data/metadata/{file_name}.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                metadata,
                f,
                indent=4
            )

        print(f"Saved: {file_name}")

    except Exception as e:

        print(
            f"Error scraping {url}"
        )

        print(e)