# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Copy the script and text file into the container
COPY generate_images.py .
COPY input.txt .

# Install required libraries
RUN pip install requests 
RUN pip install pillow
RUN pip install python-dotenv

# Run the script when the container starts
CMD ["python", "generate_images.py"]
