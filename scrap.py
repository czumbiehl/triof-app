import requests
import json
import os

# Replace YOUR_API_KEY and YOUR_CX with your actual API Key and Custom Search Engine ID
api_key = 'AIzaSyASFLZxmRIxzfDe-2a99-bc5MKTKp08Hwg'
cx = 'b014ff164ae7e4dd5'
search_term = "dirty plastic bottles"

# Making a directory to store the images
os.makedirs('images', exist_ok=True)


def download_images(search_term, num_images):
    url = "https://www.googleapis.com/customsearch/v1/siterestrict"
    params = {
        'start': 11,
        'q': search_term,
        'cx': cx,
        'key': api_key,
        'searchType': 'image',
        'num': num_images,
        'imgType': 'photo',  # You can change this as per your need
        'fileType': 'jpg'
    }

    response = requests.get(url, params=params)
    results = response.json()

    for index, item in enumerate(results['items']):
        image_url = item['link']
        image_data = requests.get(image_url).content
        with open(f'images/{search_term}_{index}.jpg', 'wb') as file:
            file.write(image_data)


download_images(search_term, 5)  # Downloads 10 images


# <script async src="https://cse.google.com/cse.js?cx=b014ff164ae7e4dd5">
# </script>
# <div class="gcse-search"></div>
