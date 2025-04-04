# image-generator

Generates images using Python, Docker and AI services

This app will read all rows within the `input.txt` file, loop through them and use an AI service to generate images.  
The generated images will be visible under `output_images/` named based on the line indexes and descriptions from your `input.txt` file.

All you have to do is to execute the bat file (on windows) or sh file (on linux).

# Prerequisites

Docker

# Preparation

* Copy the .env.example to .env and fill the API key appropriatly (see https://www.imagine.art/api/keys)
* Make sure that the images folder exists and is empty before running the application.
* Fill the input.txt with the image descriptions that will be used for image generation
