# base image
FROM python:3.10.6

# set working directory
WORKDIR /app

# set environment variables
ADD requirements.txt /app/requirements.txt

# copy all the files to the container
COPY . .

# install system dependencies
RUN apt-get update && \
    apt-get install -y portaudio19-dev && \
    rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE THE PORT
EXPOSE 7860

# start the app
CMD ["python3", "app.py", "--share"]







