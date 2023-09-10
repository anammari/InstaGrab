from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_image_url(url: str) -> str:
    """
    Extracts the image URL from the given URL.
    """
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    # The image URL is in the content field of the first meta tag with property og:image
    image_url = soup.find("meta", {"property": "og:image"})["content"]
    # Remove any preceding characters before the http/https protocol
    image_url = image_url[image_url.find("http"):]
    return image_url

def download_image(image_url: str) -> bytes:
    """
    Downloads the image from the given image URL.
    """
    return requests.get(image_url).content

def save_image(image_data: bytes, file_name: str):
    """
    Saves the image data to a file.
    """
    with open(file_name, "wb") as fp:
        fp.write(image_data)

def download_and_save_image(url: str):
    """
    Downloads an image from a URL and saves it to a file.
    """
    print(f"Downloading image from {url} ...")
    image_url = get_image_url(url)
    image_data = download_image(image_url)
    file_name = f"{datetime.now():%Y-%m-%d_%H:%M:%S}.jpg"
    save_image(image_data, file_name)
    print(f"Done. Image saved to disk as {file_name}.")
