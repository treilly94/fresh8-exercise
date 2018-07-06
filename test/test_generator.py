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
        # This test passes most of the time but because of the nature of random numbers it may occasionally fail
        self.g.batch_size = 1000
        output = self.g.batch_generator()
        size_viewed = len([d for d in output if d['type'] == "Viewed"])
        size_interacted = len([d for d in output if d['type'] == "Interacted"])
        size_click = len([d for d in output if d['type'] == "Click-Through"])

        self.assertEqual(size_viewed, 1000)
        self.assertAlmostEqual(size_interacted, 100, delta=20)
        self.assertAlmostEqual(size_click, 100, delta=20)

