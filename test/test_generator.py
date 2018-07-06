from unittest import TestCase

from fresh8_exercise.event_generator import Generator


class TestGenerator(TestCase):
    def setUp(self):
        params = ["-n", "3", "-i", "10", "-b", "30", "-o", ""]
        self.g = Generator(params)

    def test_record_generator(self):
        output = self.g.record_generator("View", "44", "2018-4-3")
        expected = {"type": "View", "data": {"viewId": "44", "eventDateTime": "2018-4-3"}}

        self.assertEqual(output, expected)

    def test_batch_generator(self):
        self.fail()

    def test_batch_writer(self):
        self.fail()

    def test_run(self):
        self.fail()
