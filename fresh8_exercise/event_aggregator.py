import os

import jsonlines


class Aggregator:
    data = []
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

        # Read each file not already read in
    #
    # def stats_generator(self):
    #     # Total each event type
    #
    #     # Print to terminal
    #
    # def run(self):
    #     # Run every 5 seconds


if __name__ == "__main__":
    print("Event Aggregator")
