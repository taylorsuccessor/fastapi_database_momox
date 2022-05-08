# Momox: Task to Manage Books and BookShelves
- solution:
    - [Solution](#solution)
   
- How to install:
    - [How to install](#how-to-install) \
          - [Docker and docker-compose](#docker-and-docker-compose) \
          - [By virtual environment](#by-virtual-environment)  \
          - [By .pyenv](#by-pyenv) 

- Testing (the same test will test both solutions for same data):
    - [How to test](#how-to-test)
    
 
The target of this task to Manage books and bookShelves

## Solution

we used Fastapi to create the required API's with sqlite engine then we can change to any database

# How to install


1. [Docker and docker-compose](#docker-and-docker-compose)
2. [By virtual environment](#by-virtual-environment)
3. [By .pyenv](#by-pyenv)

## Docker and docker-compose
Currently I'm using docker and docker-compose to save Python (3.9) version a  pip 21.3.1 version \
and this is the easest way 
1. [install docker](https://docs.docker.com/engine/install/ubuntu/) 
2. [install docker-compose](https://docs.docker.com/compose/install/)
3. unzip the the code file and cd inside the folder
4. run docker-compose up
5. go to your browser [http://localhost:8000/docs](http://localhost:8000/docs)

## By virtual environment

make sure you have Python 3.9 and Pip 21.3.1

1. [Install Python 3.9](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)
2. unzip code file
3. [install virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

        python3 -m pip install --user virtualenv
          
4. cd to your project and create virtual env by run
   
        python3 -m venv .venv
        
5. activate your environment
 
        source .venv/bin/activate
        
6. Make sure you have correct pip version

        pip install --upgrade pip==21.3.1
7. install project packages

        pip install -r requirements.txt

8. Run the server 
        
        uvicorn main:app --reload --host 0.0.0.0 --port 8000
9. Test your app

        pytest -vv

## By .pyenv

same as the last way of installation you can use \
[Install .pyenv](https://github.com/pyenv/pyenv)

you can install spicific version of python and follow [By virtual environment](#by-virtual-environment)


# How to Test

* for testing I've added  => RUN pytest -vv inside Dockerfile so the build will not success till the test success
* if you are using virtualenv just run >> pytest -vv
* you can also enter the docker container and run the test
cd to your project first
          
          docker-compose exec server /bin/bash
          pytest -vv

