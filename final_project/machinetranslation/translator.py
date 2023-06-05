from deep_translator import GoogleTranslator

def translate_english_to_french(text):
    translation = GoogleTranslator(source='en', target='fr').translate(text)
    return translation

def translate_french_to_english(text):
    translation = GoogleTranslator(source='fr', target='en').translate(text)
    return translation
