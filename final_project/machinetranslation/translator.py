"""Module translator version 1.00"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """translate english input to french"""
    french_text = MyMemoryTranslator(source="en-US", target="fr-FR").translate(text=english_text)
    return french_text

def french_to_english(french_text):
    """translate french input to english"""
    english_text = MyMemoryTranslator(source="fr-FR", target="en-US").translate(text=french_text)
    return english_text
