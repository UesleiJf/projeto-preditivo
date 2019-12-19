FROM python:3.6.6-slim


VOLUME ./:app/

# Copy local directory to /app in container
# Dont use COPY * /app/ , * will lead to lose of folder structure in /app
COPY . /app/


WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port and run the application when the container is started
EXPOSE 9999:9999
ENTRYPOINT python flask_api.py 9999


