import spacy

nlp = spacy.load("pt_core_news_sm") # Portuguese for while

text = "Texto usado para exemplos futuros"
doc = nlp(text)
for token in doc:
   treated = f"{token.text}\n {token.lemma}\n {token.pos}\n {token.morph}\n |||"
   with open("results.txt", "a") as file:
      file.write(treated)


