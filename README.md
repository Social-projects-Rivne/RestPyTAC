# RestPyTAC
Short description

# Setup
### Prerequisites 
- Python [3.4 or higher](https://www.python.org/downloads/)
- Virtual environment [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- Cloned repository [git](git@github.com:repo/repo.git)
- Docker [install](https://docs.docker.com/install/)
- Docker-compose [install](https://docs.docker.com/compose/install/)

### Setting up the project
- create new virtual env `mkvirtualenv -p <path/to/python3> project_name`, 
you could use any other name instead of `project_name`
- activate the env by running `workon project_name`
- Install modules `pip install -r ~/<path to project>/requirements.pip`
- Clone repository [rest_Spring_Docker](https://github.com/momel/rest_Spring_Docker)  
- Up clone image: `cd ~/<path to your cloned repository>` and `docker-compose up -d`

# Libs
- lib [unittest-for python 3.7.1](https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest)
- lib [requests-2.20.0](http://docs.python-requests.org/en/master/)

## Code quality
Project supports code style inspections with [pycodestyle]() tool.

Run `pip install pycodestyle` to perform project code inspection using `pep8`.
 
## Run tests
- To run unit tests execute `python unit.py`.
- To run functional tests execute `python functional.py`.