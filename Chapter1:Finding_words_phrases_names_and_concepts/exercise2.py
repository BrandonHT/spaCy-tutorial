#Accesing content of specific token 
from spacy.lang.en import English

nlp = English()

doc = nlp("I like tree kangaroos and narwhals.")
first_token=doc[0]

print(first_token.text)