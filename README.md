# Door_Lock_Flask
This is a simple IoT door lock system developped using [flask](https://palletsprojects.com/p/flask/)

## Overview
Here some photos about this work:

![main_page](/images/root.png)

![unlock](/images/unlock.png)

![door_locked](/images/door_locked.png)

## Running this app
This app is designed to run in different ways:
1. As a standalone app running on your machine
1. As a Docker container running on your machine

## As a standalone app
From a command/shell termianl 
1. `cd` into the parent directory you want to install the project in
2. `git clone` the project into a child directory 
3. `cd` into the child directory
4. run `pip install -r requirements.txt` to install dependencies

#### run the app
After installing, run the server using
    flask run 

## As a Docker container running on your machine
1. install [Docker](https://www.docker.com/)
2. run `docker --version` to check if docker is installed 
3. run `docker build -t flask_lock_door:latest .` to build the docker image
3. `docker images` list the local avaible images
4. `docker run --name flask_app -d -p 8000:5000 --rm flask_lock_door:latest` to start the container 






