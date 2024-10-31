import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        translator = PigLatin("This is a phrase")
        phrase = translator.get_phrase()
        self.assertEqual(phrase, "This is a phrase")