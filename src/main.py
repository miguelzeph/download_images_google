from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from image_extraction.image_google import download_google_images
from settings import get_logger, DRIVER_PATH


# Constants
search_for = input('What are you looking for? ')
n_images = int(input('How many images do you want? '))

# Instance
logger = get_logger(__name__)
service = Service(DRIVER_PATH)
browser = webdriver.Chrome(service=service)


if __name__ == "__main__":
    
    download_google_images(
        search_for= search_for,
        n_images= n_images,
        browser=browser
    )
    browser.quit()

