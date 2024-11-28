# Use a Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for building wheels and other packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean

# Copy the application files into the container
COPY . .

# Step 7: Run build_bots.py to clone repos and install dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 build_bots.py

# Expose any ports necessary for the bots
EXPOSE 8080 8081

# Default command to run the bots
CMD ["python3", "run_bots.py"]
