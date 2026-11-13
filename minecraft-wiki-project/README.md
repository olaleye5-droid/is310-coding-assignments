# Minecraft Wiki Web Scraping Project

## Research Question
How does the Minecraft community wiki organize information about mobs and biomes, and what characteristics does it make easy to compare?

## Why I Chose This Wiki
I chose the Minecraft Wiki because it is a community-maintained resource with detailed information about the Minecraft game. It provides structured pages for different types of game content, including mobs and biomes. Comparing these categories helps explore how the wiki organizes information.

## Website Policies and Permissions
Before scraping, I reviewed the Minecraft Wiki's `robots.txt` file and the Weird Gloop Meta licensing information. The general robots.txt rules restrict certain areas of the website, including special pages, user pages, and API endpoints. This project only requested ordinary article pages. The wiki's text is generally licensed under Creative Commons Attribution-NonCommercial-ShareAlike 3.0, with exceptions for some imported content. This project does not download images or reuse media.

## Data Collection Method
I used Python with the `requests` and `BeautifulSoup` libraries to retrieve and parse Minecraft Wiki article pages.

The scraper:
- Sends a User-Agent identifying the educational project.
- Checks HTTP responses for errors.
- Uses a 20-second request timeout.
- Waits three seconds between requests.
- Extracts the page title and first available introductory paragraph.
- Records the source URL and HTTP status code.
- Saves the collected information in a CSV file.

## Pages Collected
The scraper collected 10 pages across two categories:

**Mobs**
- Creeper
- Zombie
- Skeleton
- Enderman
- Spider

**Biomes**
- Plains
- Desert
- Forest
- Savanna
- Taiga

## Data Fields
The resulting CSV file, `minecraft_wiki_data.csv`, contains:
- `category`: Whether the page describes a mob or biome.
- `page_title`: The title of the wiki page.
- `description`: The first available introductory paragraph.
- `source_url`: The original article URL.
- `status`: The HTTP response status code.

## Results
The scraper successfully collected 10 records. All 10 pages returned an HTTP 200 status, indicating successful requests.

## Limitations
This project collects only the first introductory paragraph from each page. It does not capture every characteristic, table, statistic, or section. The introductory paragraph may describe mobs and biomes differently, so the collected descriptions are not necessarily directly comparable. The sample is also small and was selected intentionally rather than randomly.

## Ethical Considerations
The scraper uses delays between requests to reduce the load on the website. It collects text and source links rather than images or other media. The collected information remains connected to its original source URLs. The project is for educational, noncommercial research.

## Tools
- Python
- Requests
- BeautifulSoup
- CSV
- Visual Studio Code
