import os
from selenium.webdriver.remote.webdriver import WebDriver
from bs4 import BeautifulSoup
import urllib.request
import time
from settings import (
    DRIVER_PATH,
    DOWNLOAD_IMAGE_PATH,
    GOOGLE_IMAGE_CLASS,
    GOOGLE_IMAGE_URL,
    get_logger
)
from typing import List

# Instances
logger = get_logger(__name__)


def download_google_images(
    search_for: str,
    n_images: int,
    browser:WebDriver,
    download_path: str = DOWNLOAD_IMAGE_PATH,
    image_class: str = GOOGLE_IMAGE_CLASS) -> None:
    """
    Downloads images from Google search results.

    Args:
        search_for (str): search for image.
        n_images (int): The number of images to download.
        download_path (str): The path where images will be saved.
        image_class (str): The class name of the images to find in the HTML.

    Returns:
        None
    """
    
    
    # Check if the save folder exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        logger.info(f"Created directory {download_path}")
    
    logger.info('Start searching...\n')
    
    # Preparing search url
    search_url = GOOGLE_IMAGE_URL + 'q=' + search_for
    browser.get(search_url)

    # Scroll down the page to load images
    for _ in range(8):
        browser.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(1)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    results = soup.findAll('img', {'class': image_class}, limit=n_images)

    imagelinks: List[str] = [result['src'] for result in results]

    logger.info(f'Found {len(imagelinks)} images')
    logger.info('Start downloading...')

    for i, imagelink in enumerate(imagelinks, start=1):
        image_local_path = os.path.join(download_path, f'{search_for}.{i}.jpg')
        urllib.request.urlretrieve(imagelink, image_local_path)
        logger.info(f'Downloaded {image_local_path}')

    logger.info('Done')
