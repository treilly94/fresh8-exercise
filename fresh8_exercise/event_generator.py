import datetime
import getopt
import os
import random
import sys
import uuid

import jsonlines


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
                self.n_groups = int(arg)
            elif opt == "-b":
                self.batch_size = int(arg)
            elif opt == "-i":
                self.interval = int(arg)
            elif opt == "-o":
                self.output_dir = arg

    def record_generator(self, type, id, time):
        return {"type": type, "data": {"viewId": id, "eventDateTime": time}}

    def batch_generator(self):
        data = []
        for i in range(self.batch_size):
            r = random.randint(1, 100)
            view_id = str(uuid.uuid4())
            time = str(datetime.datetime.now())
            if r <= 85:
                data.append(self.record_generator("Viewed", view_id, time))
            elif r <= 90:
                data.append(self.record_generator("Viewed", view_id, time))
                data.append(self.record_generator("Interacted", view_id, time))
            elif r <= 95:
                data.append(self.record_generator("Viewed", view_id, time))
                data.append(self.record_generator("Click-Through", view_id, time))
            else:
                data.append(self.record_generator("Viewed", view_id, time))
                data.append(self.record_generator("Interacted", view_id, time))
                data.append(self.record_generator("Click-Through", view_id, time))

        return data

    def batch_writer(self, data):
        # Create formatted timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        # Build file path
        file = os.path.join(self.output_dir, "events-" + timestamp + ".json")
        # Open file and dump json data
        with jsonlines.open(file, mode='w') as writer:
            writer.write_all(data)

    def run(self):
        data = self.batch_generator()
        self.batch_writer(data)


if __name__ == "__main__":
    print("Event Generator")
    print(sys.argv[1:])
    Generator(sys.argv[1:]).run()
