from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

FILE_NAME = "translated_data"
FILE = f"Data/text/{FILE_NAME}.txt"

def load_text(filename):
    with open(filename, "r", encoding="utf-8") as file:
        try:
            text = file.read()
            return text
        except FileNotFoundError:
            print("No file found")

def summarize_text(text, max_length=130, min_length=30, length_penalty=2.0, num_beams=4):
    summary_text = summarizer(text, max_length=max_length, min_length=min_length, length_penalty=length_penalty, num_beams=num_beams)
    return summary_text[0]['summary_text']

text = load_text(FILE)
summary = summarize_text(text)
print(summary)