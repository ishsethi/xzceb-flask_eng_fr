import unittest

from final_project.machinetranslation.translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_enlgish_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Bye'),'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')   
        self.assertNotEqual(french_to_english('Null'),'Hello')

if __name__ == "__main__":
    unittest.main()