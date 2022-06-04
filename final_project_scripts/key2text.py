import json
from keytotext import pipeline

nlp = pipeline("k2t")

nlp(['India','wedding','Food'])
f=open('keywords.json')
j=json.load(f)
texts={}
for k in j:
    texts[k]={}
    for w in j[k]:
        print(w)
f.close()