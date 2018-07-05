# fresh8-exercise
This project contains a solution to the Fresh8 data-engineer challenge written in python 3.6

## Running the tests
The tests are written using the unittest library and can be called in the below way. 
 
Navigate into the project directory (the one containing the test folder) and run the below command in an 
appropriate python environment
```shell
python -m unittest
```
## Installing the package

## Running the package
### event_generator
The event generator takes the following runtime arguments:  
* -n Number of files 
* -i Number of seconds between files 
* -b Number of events in a file
* -o Output directory
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