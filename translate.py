import argostranslate.translate

TRANSLATE_FROM = "ja"
TRANSLATE_TO = "en"

def translate(text, tn_from, tn_to):
    translated_text = argostranslate.translate.translate(text, tn_from, tn_to)
    return translated_text

with open("Data/text/data.txt", "r", encoding="utf-8") as file:
    try:
        text = file.read()
    except FileNotFoundError:
        print("No file found")

translated_text = translate(text, TRANSLATE_FROM, TRANSLATE_TO)
with open("Data/text/translated_data.txt", "w", encoding="utf-8") as file:
    file.write(translated_text)
