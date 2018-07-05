# fresh8-exercise
This project contains a solution to the Fresh8 data-engineer challenge written in python 3.6

## Running the tests

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
python event_generator.py -n 3 -i 10 -b 30 -o /home/data
```
### event_aggregator
