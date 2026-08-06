
# Python Based Docker
FROM python:3.11-slim

# Installing Packages
RUN apt update && apt upgrade -y
RUN apt install -y git curl python3-pip ffmpeg aria2 && rm -rf /var/lib/apt/lists/*

# Updating Pip Packages
RUN pip3 install -U pip

WORKDIR /EXTRACTOR

# Copying Requirements
COPY requirements.txt /EXTRACTOR/requirements.txt

# Installing Requirements
RUN pip3 install -U -r requirements.txt

# Copying rest of the source code
COPY . /EXTRACTOR

# Running Bot
CMD ["/bin/bash", "/EXTRACTOR/start.sh"]
