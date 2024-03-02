## Use an official Python runtime as a parent image
FROM python:3.7-slim

## Set the working directory in the container to /app
WORKDIR /crud

## Add the current directory contents into the container at /app
ADD . /crud

## Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN ls
## Make port 80 available to the world outside this container
EXPOSE 80

## Run app.py when the container launches
CMD streamlit run --server.port 80 app.py
