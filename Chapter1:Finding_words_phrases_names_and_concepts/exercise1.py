from spacy.lang.en import English
nlp = English()

doc = nlp("This is a sentence")

print(doc.text)