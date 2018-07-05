import os
import time

import jsonlines
import pandas as pd


class Aggregator:
    data = []
    df = None
    # List of files already processed
    files = []

    def __init__(self, path):
        self.path = path

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
        self.df = pd.DataFrame(self.data)
        # Total each event type
        counts = self.df["type"].groupby(self.df["type"]).count()
        # Print to terminal
        print("============================")
        print(counts)

    def run(self):
        # Run every 5 seconds
        while True:
            self.file_reader()
            self.stats_generator()
            time.sleep(5)


if __name__ == "__main__":
    print("Event Aggregator")
    Aggregator("/home/treilly/Documents/projects/fresh8-exercise/data/").run()
