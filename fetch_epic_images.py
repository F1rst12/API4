import datetime
import os
import requests
from dowload_images import download_image


def fetch_nasa_epic(nasa_token):
    url = f"https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"count": 30, "api_key":nasa_token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for nasa_image in response.json():
        epic_name = nasa_image["image"]
        epic_date = nasa_image["date"]
        formatted_epic_date = datetime.datetime.fromisoformat(
            epic_date).strftime("%Y/%m/%d")
        epic_image_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_epic_date}/png/{epic_name}.png?api_key={nasa_token}"
        download_image(epic_image_url, f"epic{epic_name}.png")


def main():
    nasa_token = os.environ['NASA_TOKEN']
    fetch_nasa_epic(nasa_token)


if __name__ == "__main__":
    main()
