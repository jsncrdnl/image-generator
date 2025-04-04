mkdir -p output_images
docker build -t img-generator .
docker run --rm -v ./output_images:/app/output_images -v ./input.txt:/app/input.txt -v ./.env:/app/.env img-generator