import unittest
from hangman import *

class HangmanTest(unittest.TestCase):
    def test_it_can_determine_if_word_has_not_been_guessed(self):
        secretWord = 'apple'
        lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        actual = isWordGuessed(secretWord, lettersGuessed)
        expected = False

        self.assertEqual(actual, expected)

    def test_it_can_determine_if_word_has_been_guessed(self):
        secretWord = 'durian'
        lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
        actual = isWordGuessed(secretWord, lettersGuessed)
        expected = True

        self.assertEqual(actual, expected)

    def test_it_can_get_guessed_word(self):
        secretWord = 'apple'
        lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        actual = getGuessedWord(secretWord, lettersGuessed)
        expected = '_ pp_ e'

        self.assertEqual(actual, expected)

    def test_it_can_get_available_letters(self):
        lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        actual = getAvailableLetters(lettersGuessed)
        expected = 'abcdfghjlmnoqtuvwxyz'

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
