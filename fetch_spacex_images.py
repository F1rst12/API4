import argparse
import requests
from dowload_images import download_images


def fetch_spacex_last_launch(spacex_id):
    url = f"https://api.spacexdata.com/v5/launches/{spacex_id}"
    response = requests.get(url)
    response.raise_for_status()
    spacex_images = response.json()["links"]["flickr"]["original"]
    for number, image_url in enumerate(spacex_images):
        download_images(image_url, f"spacex{number}.jpg")


def main():
    parser = argparse.ArgumentParser(description='Videos to images')
    parser.add_argument('--spacex_id', type=str, help='Введите ID запуска', default='5eb87d47ffd86e000604b38a')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.spacex_id)


if __name__ == "__main__":
    main()
