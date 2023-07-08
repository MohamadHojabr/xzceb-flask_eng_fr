# unit test case
import unittest
from machinetranslation.translator import english_to_french , french_to_english
  
class TestMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_englishToFrench(self):
        str_value = 'Hello'
        self.assertEqual(english_to_french(str_value), 'Bonjour')

    def test_frenchToEnglish(self):
        str_value = 'Bonjour'
        self.assertEqual(french_to_english(str_value), 'Hi')
  
if __name__ == '__main__':
    unittest.main()