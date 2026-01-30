"""Test how to use the Python requests library to download image data for Pillow"""

import requests
from PIL import Image

img_url = "https://i.pinimg.com/originals/4f/e7/06/4fe7066d4f3aa7201e38484230fc32b3.jpg"
response = requests.get(img_url, stream=True).raw
image = Image.open(response)
image.show()
