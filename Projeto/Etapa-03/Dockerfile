FROM python:3.6.6-slim

# Mount current directory to /app in the container image
VOLUME ./:app/

# Copy local directory to /app in container
# Dont use COPY * /app/ , * will lead to lose of folder structure in /app
COPY . /app/

# Change WORKDIR
WORKDIR /app

# Install dependencies
# use --proxy http://<proxy host>:port if you have proxy
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port and run the application when the container is started
EXPOSE 9999:9999
ENTRYPOINT python flask_api.py 9999

# docker build
# docker build -t projeto .

# docker run
# docker run projeto -p 9999 # to make the port externally avaiable for browsers
