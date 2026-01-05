import spacy

nlp = spacy.load("pt_core_news_sm")

texto = input("TEXTO: ")
doc = nlp(texto)

for token in doc:
   print(f"palavra {token.text} {token.lemma} {token.pos} {token.morph}" )
