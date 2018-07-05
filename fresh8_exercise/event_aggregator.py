import getopt
import os
import sys
import time

import jsonlines
import pandas as pd


class Aggregator:
    def __init__(self, argv):
        self.path = None  # The path to the data directory
        self.files = []  # List of files already processed
        self.data = []  # The raw data before it is converted to a pandas dataframe
        self.df = None  # The pandas dataframe
        self.counts = None  # The aggregated dataframe

        self.get_args(argv)

    def get_args(self, argv):
        help_string = 'event_aggregator.py -h <help> -d <directory>'
        # Get opts and args if available
        try:
            opts, args = getopt.getopt(argv, "hd:")
        except getopt.GetoptError:
            print(help_string)
            sys.exit(2)

        # Set args to variables
        for opt, arg in opts:
            if opt == '-h':
                print(help_string)
                sys.exit()
            elif opt == "-d":
                self.path = arg

    def file_reader(self):
        # Get list of files in directory
        new_files = os.listdir(self.path)

        for f in new_files:
            # Only process files not already processed
            if f not in self.files:
                # Add file to processed files
                self.files.append(f)
                # Construct path
                file_path = self.path + f
                # Open file and add records to data
                with jsonlines.open(file_path) as reader:
                    for obj in reader:
                        self.data.append(obj)

    def stats_generator(self):
        # Create pandas dataframe
        self.df = pd.DataFrame(self.data)
        # Total each event type
        self.counts = self.df["type"].groupby(self.df["type"]).count()

    def run(self):
        # Run forever
        while True:
            self.file_reader()
            self.stats_generator()
            # Print to terminal
            print("============================")
            print(self.counts)
            # Wait 5 seconds
            time.sleep(5)


if __name__ == "__main__":
    print("Event Aggregator")
    print(sys.argv[1:])
    Aggregator(sys.argv[1:]).run()
