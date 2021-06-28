FROM python:3.8
# set a key-value label for the Docker image
LABEL maintainer="Python King"
COPY . /app
WORKDIR /app
RUN sudo apt-get install python-yaml
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
