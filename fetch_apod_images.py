import requests
import os
from urllib.parse import unquote, urlparse
from dowload_images import download_images


def get_extension(url):
    decoded_link = unquote(url)
    parsed_link = urlparse(decoded_link)
    path, name = os.path.split(parsed_link.path)
    filename, extension = os.path.splitext(name)
    return extension, filename


def fetch_nasa_apod(nasa_token):
    payload = {"count": 30, "api_key":nasa_token}
    url = f"https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for nasa_image in response.json():
        if nasa_image.get("media_type") == "image":
            nasa_link_image = nasa_image["url"] or nasa_image["hdurl"]
        extension, filename = get_extension(nasa_link_image)
        download_images(nasa_link_image, f"nasa{filename}{extension}")


def main():
    nasa_token = os.environ['NASA_TOKEN']
    fetch_nasa_apod(nasa_token)


if __name__ == "__main__":
    main()
