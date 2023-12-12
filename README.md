# entrapeerProject
### Build the Docker image using:

``` bash
docker build -t <the_name_of_the_container> .
```

### Then run the docker container using:
``` bash
docker run -d -p 9000:8000 my-fastapi-app
```
### The FastAPI application uses port 8000 inside the Docker container, which will be mapped to your local machine's port 9000. This mapping allows you to access the API through your localhost on port 9000.

### To trigger the web crawler, go to::
http://0.0.0.0:9000/execute_tasks

The web crawler will start working.

