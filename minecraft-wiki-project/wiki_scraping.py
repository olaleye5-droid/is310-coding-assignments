
import re

import requests
from bs4 import BeautifulSoup
import time
import csv

BASE_URL = "https://minecraft.wiki"

HEADERS = {
    "User-Agent": "IS310StudentResearch/1.0 (educational coursework)"
}

# Two categories of wiki pages
MOB_PAGES = [
    "Creeper",
    "Zombie",
    "Skeleton",
    "Enderman",
    "Spider"
]

BIOME_PAGES = [
    "Plains",
    "Desert",
    "Forest",
    "Savanna",
    "Taiga"
]


def scrape_page(page_name, category):
    """Retrieve and extract basic information from a wiki page."""

    url = f"{BASE_URL}/w/{page_name.replace(' ', '_')}"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find("h1")

        if title:
            page_title = title.get_text(" ", strip=True)
        else:
            page_title = page_name

        paragraphs = soup.select(
            ".mw-parser-output > p"
        )

        description = ""

        for paragraph in paragraphs:
            text = paragraph.get_text(" ", strip=True)
            text = re.sub(r"\s+([.,;:!?])", r"\1", text)

            if text:
                description = text
                break

        return {
            "category": category,
            "page_title": page_title,
            "description": description,
            "source_url": url,
            "status": response.status_code
        }

    except requests.RequestException as error:
        print(f"Error scraping {page_name}: {error}")
        return None


def main():

    records = []

    # Scrape mob pages
    for mob in MOB_PAGES:
        print(f"Scraping mob: {mob}")

        record = scrape_page(mob, "Mob")

        if record:
            records.append(record)

        time.sleep(3)

    # Scrape biome pages
    for biome in BIOME_PAGES:
        print(f"Scraping biome: {biome}")

        record = scrape_page(biome, "Biome")

        if record:
            records.append(record)

        time.sleep(3)

    # Save results
    with open(
        "minecraft_wiki_data.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        fieldnames = [
            "category",
            "page_title",
            "description",
            "source_url",
            "status"
        ]

        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(records)

    print(f"\nFinished! Saved {len(records)} records.")
    print("Output file: minecraft_wiki_data.csv")


if __name__ == "__main__":
    main()
