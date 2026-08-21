import sys
import json
from pathlib import Path
from typing import Any
import requests
from bs4 import BeautifulSoup
import lxml
import re

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

PATH_EVENT = Path(__file__).parent
PATH_CIRCLES_JSON = PATH_EVENT / "circles.json"
NAME = PATH_EVENT.name


def retrieve_soup_fetch_if_needed(url: str) -> BeautifulSoup:
    """Retrieve BeautifulSoup object for the given URL, fetching the content if necessary."""
    html_path = PATH_EVENT / "raw.html"
    if not html_path.exists():
        print(f"Raw HTML file not found, fetching from {url} ...")
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(
                f"Failed to retrieve data from {url}, status code: {response.status_code}"
            )
        html_path.write_bytes(response.content)
    with html_path.open("rb") as f:
        return BeautifulSoup(f, "lxml")


def sanitize_string(s: str) -> str:
    s = s.strip()
    s = re.sub(r"[\s\n\t]+", " ", s)
    return s


def main():
    """Create circles.json"""
    print(f"Retrieving circles information for {NAME} ...")
    raw_url = "https://web.archive.org/web/20110811213205id_/http://www.puniket.com/cirno/cirno_list01.htm"
    
    # Parse the HTML content to extract circle information
    soup = retrieve_soup_fetch_if_needed(raw_url)
    circles = []

    tables = soup.find_all("table")
    # print(f"Found {len(tables)} tables.")

    is_active = True
    for table in tables:
        rows = table.find_all("tr")
        # print(f" Found {len(rows)} rows.")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 4 or "サークル名" in cols[0].get_text() or not cols[1].get_text().strip():
                # print(len(cols), cols)
                if "■幺樂団カァニバル！" in cols[0].get_text():
                    is_active = False
                continue
            if not is_active:
                continue
        
            name = cols[0].get_text(strip=True).replace("\r", "").replace("\n", "")
            penname = cols[1].get_text(strip=True).replace("\r", "").replace("\n", "")
            position = cols[3].get_text(strip=True)

            links = []
            link = cols[2].get_text(strip=True)
            if link:
                links.append(link)

            circle = Circle(
                position=position,
                pen_names=[penname],
                aliases=[name],
                links=[link for link in links],
            )
            circles.append(circle)


    # Save the extracted circle information to a JSON file
    with open(PATH_CIRCLES_JSON, "w", encoding="utf-8") as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=2)
    print(f"Saved {len(circles)} circles to {PATH_CIRCLES_JSON}")


if __name__ == "__main__":
    main()
