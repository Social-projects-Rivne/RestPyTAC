# RestPyTAC
Short description

# Setup
### Prerequisites 
- Python [3.4 or higher](https://www.python.org/downloads/)
- Virtual environment [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- Cloned repository [git](https://github.com/Social-projects-Rivne/RestPyTAC)
- Docker [install](https://docs.docker.com/install/)
- Docker-compose [install](https://docs.docker.com/compose/install/)

### Setting up the project
- create new virtual env `mkvirtualenv api-tests -p <path/to/python3>`
- activate the env by running `workon api-tests`
- Install modules `pip install -r ~/<path to project>/requirements.pip`
- Clone repository [rest_Spring_Docker](https://github.com/momel/rest_Spring_Docker)  
- Run docker image from cloned repository: `cd ~/<path to your cloned repository>` and `docker-compose up -d`

# Libs
- lib [unittest-2.4.0](https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest)
- lib [requests-2.20.0](http://docs.python-requests.org/en/master/)
- lib [nose-1.3.7](https://nose.readthedocs.io/en/latest/index.html)

## Code quality
Project supports code style inspections with [pycodestyle]() tool.

Run `pip install pycodestyle` to perform project code inspection using `pep8`.
 
## Run tests
- To run unit tests execute: `cd ~/<path to project>/tests/unit` and `nosetests __init__.py`.
- To run functional tests execute: `cd ~/<path to project>/tests/functional` and `nosetests __init__.py`.