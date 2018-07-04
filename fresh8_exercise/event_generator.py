import datetime
import getopt
import json
import os
import sys


class Generator:
    def __init__(self, argv):
        help_string = 'event_generator.py -h <help> -n <number of groups> -b <batch size> ' \
                      '-i <interval> -o <output directory>'

        # Get opts and args if available
        try:
            opts, args = getopt.getopt(argv, "hn:b:i:o:")
        except getopt.GetoptError:
            print(help_string)
            sys.exit(2)

        # Set args to variables
        for opt, arg in opts:
            if opt == '-h':
                print(help_string)
                sys.exit()
            elif opt == "-n":
                self.n_groups = arg
            elif opt == "-b":
                self.batch_size = arg
            elif opt == "-i":
                self.interval = arg
            elif opt == "-o":
                self.output_dir = arg

    def batch_generator(self):
        self.data = []


    def batch_writer(self):
        # Create formatted timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        # Build file path
        file = os.path.join(self.output_dir, "events-" + timestamp + ".json")
        # Open file and dump json data
        with open(file, 'w') as outfile:
            json.dump(self.data, outfile)

    def run(self):
        self.batch_generator()
        self.batch_writer()


if __name__ == "__main__":
    print("Event Generator")
    print(sys.argv[1:])
    Generator(sys.argv[1:]).run()
