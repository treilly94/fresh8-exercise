import datetime
import getopt
import os
import random
import sys
import time
import uuid

import jsonlines


class Generator:
    def __init__(self, argv):
        """
        This method initialises the class variables

        :param argv: List[String] - The runtime arguments
        """

        self.n_groups = 1
        self.batch_size = 1
        self.interval = 1
        self.output_dir = os.getcwd() + "/data/"

        self.get_args(argv)

    def get_args(self, argv):
        """
        This method parses the runtime arguments

        :param argv: List[String] - The runtime arguments
        """

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
                self.n_groups = int(arg)
            elif opt == "-b":
                self.batch_size = int(arg)
            elif opt == "-i":
                self.interval = int(arg)
            elif opt == "-o":
                self.output_dir = arg

    def record_generator(self, event_type, event_id, event_time):
        """
        This method generates individual mock records

        :param event_type: String - The type of event for this record
        :param event_id: String - The ID of the event
        :param event_time: String - The time of the event
        :return: Dictionary - The record
        """
        return {"type": event_type, "data": {"viewId": event_id, "eventDateTime": event_time}}

    def batch_generator(self):
        """
        This method creates a batch of events.

        The number of events in the batch is determined by self.batch_size.

        The types of events should roughly follow the below distribution:

        * 85% Viewed
        * 5% Viewed / Interacted
        * 5% Viewed / Click-Through
        * 5% Viewed / Interacted / Click-Through
        """
        data = []
        # repeat for the batch size
        for i in range(self.batch_size):
            # Generate a random number for the probability
            r = random.randint(1, 100)
            # Generate a random uuid
            view_id = str(uuid.uuid4())
            # Get the datetime in a iso format
            current_time = datetime.datetime.now().isoformat()
            # Create the records based on the probability of each situation
            if r <= 85:
                data.append(self.record_generator("Viewed", view_id, current_time))
            elif r <= 90:
                data.append(self.record_generator("Viewed", view_id, current_time))
                data.append(self.record_generator("Interacted", view_id, current_time))
            elif r <= 95:
                data.append(self.record_generator("Viewed", view_id, current_time))
                data.append(self.record_generator("Click-Through", view_id, current_time))
            else:
                data.append(self.record_generator("Viewed", view_id, current_time))
                data.append(self.record_generator("Interacted", view_id, current_time))
                data.append(self.record_generator("Click-Through", view_id, current_time))

        return data

    def batch_writer(self, data):
        """
        This method writes the data to a directory in a json lines format.

        The directory is defined by self.output_dir

        :param data: List[Dictionary] - The data to be written
        """
        # Create formatted timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        # Build file path
        file = os.path.join(self.output_dir, "events-" + timestamp + ".json")
        # Open file and dump json data
        with jsonlines.open(file, mode='w') as writer:
            writer.write_all(data)

    def run(self):
        """This method produces records and writes them based on self.interval and self.n_groups"""
        for i in range(self.n_groups):
            data = self.batch_generator()
            self.batch_writer(data)
            time.sleep(self.interval)


if __name__ == "__main__":
    print("Event Generator")
    print(sys.argv[1:])
    Generator(sys.argv[1:]).run()
