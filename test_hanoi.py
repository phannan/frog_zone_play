from unittest import TestCase

from Hanoi import Hanoi


class TestHanoi(TestCase):
    def test_hanoi(self):
        h = Hanoi()
        self.assertEqual(1, 55, "badder")
