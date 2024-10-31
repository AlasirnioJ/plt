import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        translator = PigLatin("This is a phrase")
        phrase = translator.get_phrase()
        self.assertEqual(phrase, "This is a phrase")
    def test_empty_phrase(self):
        translator = PigLatin("")
        phrase = translator.get_phrase()
        self.assertEqual(phrase, "nil")
    def test_word_ends_y(self):
        translator = PigLatin("any")
        translation = translator.translate()
        self.assertEqual(translation, "anynay")
    def test_word_starts_e(self):
        translator = PigLatin("apple")
        translation = translator.translate()
        self.assertEqual(translation, "applenay")
    def test_word_starts_k(self):
        translator = PigLatin("ask")
        translation = translator.translate()
        self.assertEqual(translation, "askay")
    def test_word_single_consonant(self):
        translator = PigLatin("hello")
        translation = translator.translate()
        self.assertEqual(translation, "ellohay")