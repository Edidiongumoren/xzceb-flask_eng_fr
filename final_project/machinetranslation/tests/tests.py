import unittest
from translator import translate_english_to_french, translate_french_to_english

class TranslationTests(unittest.TestCase):
    def test_english_to_french_translation(self):
        text = "Hello"
        translation = translate_english_to_french(text)
        self.assertEqual(translation, "Bonjour")

    def test_french_to_english_translation(self):
        text = "Bonjour"
        translation = translate_french_to_english(text)
        self.assertEqual(translation, "Good morning")

if __name__ == '__main__':
    unittest.main()
