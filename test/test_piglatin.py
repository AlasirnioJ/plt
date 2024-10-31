import unittest

import piglatin
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

    def test_word_multiple_consonants(self):
        translator = PigLatin("known")
        translation = translator.translate()
        self.assertEqual(translation, "ownknay")
    def test_translate_more_words_hello_world(self):
        translator = PigLatin("hello world")
        translation = translator.translate()
        self.assertEqual(translation, "ellohay orldway")
    def test_translate_unison_word(self):
        translator = PigLatin("well-being")
        translation = translator.translate()
        self.assertEqual(translation, "ellway-eingbay")
    def test_translate_punctuation(self):
        translator = PigLatin("hello world!")
        translation = translator.translate()
        self.assertEqual(translation, "ellohay orldway!")

