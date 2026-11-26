import re


def remove_sarcasm(text):
    return re.compile(r"(?<!\S)/s(?![\w/])").sub("sarcastic", text)



def preprocess_data():
    pass