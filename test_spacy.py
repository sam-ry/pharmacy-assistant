# test_spacy.py
import spacy

nlp = spacy.load("medicine_ner")

# text = "Patient was given Paracetamol and Ibuprofen."
# doc = nlp(text)

# for ent in doc.ents:
#     print(ent.text, ent.label_)

def medicine_list(text):
    doc = nlp(text)
    medicines = [i.text for i in doc.ents]
    return medicines