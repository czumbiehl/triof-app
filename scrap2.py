from urllib.parse import urlparse
import mimetypes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
import base64


def initialize_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver


def download_images(driver, url, max_images):
    driver.get(url)
    image_urls = set()
    scroll_attempts = 0
    last_height = driver.execute_script("return document.body.scrollHeight")

    while len(image_urls) < max_images and scroll_attempts < 10:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        images = driver.find_elements(By.CSS_SELECTOR, "img")
        for image in images:
            if len(image_urls) >= max_images:
                break
            src = image.get_attribute('src')
            if src:
                image_urls.add(src)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        scroll_attempts += 1

    print(f"Collected {len(image_urls)} image URLs.")
    return list(image_urls)


def download_image(url, folder_path, num):
    # Ensure the save folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Check if URL is a data URL
    if url.startswith('data:image'):
        # Handle base64 encoded images
        # Extract the base64 part
        header, encoded = url.split(',', 1)
        # Extract the image format (e.g., 'png' or 'jpeg')
        file_extension = header.split('/')[1].split(';')[0]
        image_data = base64.b64decode(encoded)
        file_path = os.path.join(folder_path, f'image_{num}.{file_extension}')
        try:
            with open(file_path, 'wb') as f:
                f.write(image_data)
            print(f"Downloaded {file_path}")
        except IOError as e:
            print(f"Could not write image to file: {e}")
        return  # Exit the function after handling base64 encoded image

    # Validate and modify the URL if necessary
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'http://' + url  # Default to HTTP if no scheme is provided

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Guess the file extension
            content_type = response.headers.get('content-type')
            file_extension = content_type.split(
                '/')[-1] if content_type else 'jpg'
            file_path = os.path.join(
                folder_path, f'image_{num}.{file_extension}')
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded {file_path}")
        else:
            print(
                f"Failed to download {url} - HTTP status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image {url}: {e}")


def main():
    driver = initialize_browser()
    try:
        image_urls = download_images(
            driver, "https://www.google.com/search?hl=en&tbm=isch&q=dirty+plastic+bottles", 20)
        for i, img_url in enumerate(image_urls):
            download_image(img_url, 'downloaded_images', i + 1)
            print(f"Downloaded image {i + 1}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
