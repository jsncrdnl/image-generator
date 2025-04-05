import requests
import os
from PIL import Image
from io import BytesIO
import re
from dotenv import load_dotenv


# API URL for DALL-E image generation
API_URL = "https://api.vyro.ai/v2/image/generations"

# Your OpenAI API key
load_dotenv()
API_KEY = os.getenv('API_KEY')
IMG_PER_LINE = int(os.getenv('IMG_PER_LINE'))

# Injected base string for image generation 
# Use it to make the generate images look the same with Lunii standart format 
IMG_DESCRIPTION = ", in a cartoon style, drawed in white on a black background, only two colors used (black and white)"

# Desired output size (320x240, with 4:3 ratio)
WIDTH, HEIGHT = 320, 240

# Desired ratio (with 4:3 ratio)
RATIO = "4:3"

# Desired generated image style
# (anime, realistic, flux-schnell, flux-dev-fast, flux-dev, imagine-turbo)
STYLE = "imagine-turbo"

# Open the text file that contains the descriptions
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Create a folder to store the generated images
output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

# Function to clean filenames (remove invalid characters for Windows)
def sanitize_filename(text):
    return re.sub(r'[<>:"/\\|?*]', '_', text)[:100]  # Limit filename length

# Function to generate image from text description using OpenAI API (DALL-E)
def generate_image(description, index, iteration):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "prompt": (None, f"{description}{IMG_DESCRIPTION}"),
        "style": (None, STYLE),
        "aspect_ratio": (None, RATIO)
    }

    # Make the API request
    response = requests.post(API_URL, files=payload, headers=headers)

    if response.status_code == 200:
        # Open the image using PIL
        image = Image.open(BytesIO(response.content))

        # Resize the image to the desired 4:3 ratio (320x240)
        image = image.resize((WIDTH, HEIGHT))

        # Save the image as a PNG file
        filename = sanitize_filename(description)
        image.save(f'{output_dir}/{index}_{iteration}_{filename}.png')
        print(f"Image {index}_{iteration}_{filename}.png generated")
    else:
        print(f"Failed to generate image {index}: {response.text}")

# Iterate through each line and generate an image
for i, line in enumerate(lines):
    description = line.strip()  # Clean up the description
    if description:  # Avoid processing empty lines
        for j in range(IMG_PER_LINE):
            generate_image(description, i, j)

print(f"Generated {len(lines)} images in the '{output_dir}' folder.")
