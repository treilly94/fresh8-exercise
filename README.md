# fresh8-exercise
This project contains a solution to the Fresh8 data-engineer challenge written in python 3.6

## Setting up the environment 
This package needs to be run on a python 3.6 environment with the requirements found in the requirements.txt  
A clean python environment can be created either using the [venv package](https://docs.python.org/3/tutorial/venv.html) 
or [docker](https://www.docker.com). I used the below command to generate a interactive docker container:
```shell
docker run -it -d --name fresh8 --rm -v <path to local fresh8-exercise>:/fresh8-exercise/ python:3.6.6-jessie

``` 
One or more connections can then be made to the terminal using the below command:
```shell
docker exec -it <container name> bash
```
Using this method will allow you to have one terminal running each method at the same time.  


Within the container you can then cd into the fresh8-exercise directory and install the requirements using  
```shell
pip install -r requirements.txt 
```

## Running the tests
The tests are written using the unittest library and can be called in the below way. 
 
Navigate into the project directory (the one containing the test folder) and run the below command in an 
appropriate python environment
```shell
python -m unittest
```

## Running the package
### event_generator
The event generator takes the following runtime arguments:  
* -n Number of files 
    * Defaults to 1
* -i Number of seconds between files 
    * Defaults to 1
* -b Number of events in a file
    * Defaults to 1
* -o Output directory
    * Defaults to the cwd /data/
* -h Help (Optional)

And can be run in the following ways
#### From file
Open a terminal in the directory containing the event_generator.py file.  
In an appropriate python environment run a command like the below example:
```shell
python event_generator.py -n 3 -i 10 -b 30 -o /home/data/
```
### event_aggregator
The event_aggregator takes the following runtime arguments:  
* -d The directory of the files
* -h Help (Optional)

And can be run in the following ways, and will continue to run until interrupted (for example using Control-C) 
#### From file
Open a terminal in the directory containing the event_aggregator.py file.  
In an appropriate python environment run a command like the below example:
```shell
python event_aggregator.py -d /home/data/
```
## Improvements
* More unit tests
* Package and put on [test.pypi.org](https://test.pypi.org/)
* Look into making it conform to the structure outlined [here](http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html)
