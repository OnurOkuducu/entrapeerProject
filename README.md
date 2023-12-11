# entrapeerProject
Build the docker container using
docker build -t <the_name_of_the_container> .

Then run the docker image using:
docker run -d -p 9000:8000 my-fastapi-app

Fast api uses localhost port 8000 in docker image, this port will be mapped to your machines port 9000 so you can access the api through your localhost port 9000

When you go to:
http://0.0.0.0:9000/execute_tasks

The web crawler will start working.

