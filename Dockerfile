# Step 1: Use a Python base image
FROM python:3.12-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the local files (your build_bots.py, run_bots.py, requirements.txt, etc.) into the container
COPY . /app

# Step 4: Install any dependencies specified in requirements.txt
#RUN pip3 install --no-cache-dir -r requirements.txt

# Step 5: Install Git (required for cloning repositories)
RUN apt-get update && apt-get install -y git

# Step 7: Run build_bots.py to clone repos (if not already done) and install dependencies
RUN python3 build_bots.py

# Step 8: Expose any ports if necessary (for example, if your bots have a web interface)
EXPOSE 8080

# Step 9: Set the default command to run the bots using run_bots.py
CMD ["python3", "run_bots.py"]

