from unittest import TestCase

from fresh8_exercise.event_aggregator import Aggregator


class TestAggregator(TestCase):
    def setUp(self):
        self.a = Aggregator(["-d", "./resources/"])

    def test_file_reader(self):
        self.a.file_reader()

        expected = [
            {"type": "Viewed", "data": {"viewId": "1", "eventDateTime": "2018-07-05T09:32:47.083473"}},
            {"type": "Viewed", "data": {"viewId": "2", "eventDateTime": "2018-07-05T09:32:47.083507"}},
            {"type": "Click-Through", "data": {"viewId": "2", "eventDateTime": "2018-07-05T09:32:47.083507"}},
            {"type": "Viewed", "data": {"viewId": "3", "eventDateTime": "2018-07-05T09:32:47.083527"}},
            {"type": "Viewed", "data": {"viewId": "4", "eventDateTime": "2018-07-05T09:32:47.083538"}},
            {"type": "Interacted", "data": {"viewId": "4", "eventDateTime": "2018-07-05T09:32:47.083538"}}
        ]

        self.assertEqual(self.a.data, expected)

    def test_stats_generator(self):
        self.fail()

    def test_run(self):
        self.fail()
