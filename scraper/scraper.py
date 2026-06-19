import requests
import os
import json

from bs4 import BeautifulSoup
from datetime import datetime

from crawler import get_service_links

# Create folders
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)
os.makedirs("data/metadata", exist_ok=True)

urls = get_service_links()

print(f"Found {len(urls)} URLs\n")

for index, url in enumerate(urls):

    try:

        print(f"Scraping: {url}")

        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Create filename from page title
        title = (
            soup.title.text.strip()
            if soup.title
            else f"page_{index}"
        )

        file_name = (
            title.lower()
            .replace(" ", "_")
            .replace("-", "_")
            .replace("/", "_")
        )

        file_name = "".join(
            c for c in file_name
            if c.isalnum() or c == "_"
        )

        file_name = file_name[:80]

        # --------------------------
        # Save Raw HTML
        # --------------------------

        with open(
            f"data/raw/{file_name}.html",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(response.text)

        # --------------------------
        # Extract Main Content
        # --------------------------

        main_content = soup.find(
            "main",
            id="content"
        )

        # Fallbacks
        if not main_content:

            main_content = soup.find(
                "div",
                {"data-elementor-type": "wp-page"}
            )

        if not main_content:

            main_content = soup.find("article")

        if not main_content:

            main_content = soup.find("main")

        if main_content:

            text = main_content.get_text(
                separator="\n",
                strip=True
            )

        else:

            print(
                f"Warning: No main content found for {url}"
            )

            text = soup.get_text(
                separator="\n",
                strip=True
            )

        # --------------------------
        # Save Processed Text
        # --------------------------

        with open(
            f"data/processed/{file_name}.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)

        # --------------------------
        # Metadata
        # --------------------------

        metadata = {
            "url": url,
            "title": title,
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
                indent=4,
                ensure_ascii=False
            )

        print(
            f"✓ Saved {file_name}"
        )

    except Exception as e:

        print(f"✗ Failed: {url}")
        print(e)

print("\nScraping completed successfully!")