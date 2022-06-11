import pickle
import json
import re
import numpy as np
import string
with open('./embed/wordEmbed.pickle', 'rb') as handle:
   embedding = pickle.load(handle)
   #print(len(embedding))

with open("./embed/keywords.json") as f:
    j = json.load(f)
    all_keywords = []
    for k, v in j.items():
        all_keywords.extend(v)
def clean_word(s):
    punctuation_string = string.punctuation
    for i in punctuation_string:
        s = s.replace(i, '')
    return s
def find_nearest_keyword(sentence):
    s_list = sentence.split()
    min_dist = 10000000
    nearest_key = "eat"
    for i, word in enumerate(s_list):
        word=clean_word(word)
        if (word in embedding):
            vec_word = embedding[word]
        else:
            continue
        for j, k in enumerate(all_keywords):
            k_tmp = k
            if k == "ice cream":
                k_tmp = "ice" 
            elif k == "seafooder":
                k_tmp = "seafood"
            elif k == "coffee shop":
                k_tmp = "coffee"
            elif k == "room key":
                k_tmp = "key"
            elif k == "check in":
                k_tmp = "check"
            elif k == "room service":
                k_tmp = "service"
            elif k == "b & b":
                k_tmp = "hotel"
            elif k == "book a room":
                k_tmp = "booking"
            elif k == "wake up":
                k_tmp = "wake"
            elif k == "check out":
                k_tmp = "check"
            elif k == "media product":
                k_tmp = "media"
            elif k == "requel":
                k_tmp = "novel"
            elif k == "see a story":
                k_tmp = "story"
            elif k == "top hits":
                k_tmp = "hits"
            elif k == "national park":
                k_tmp = "park"
            elif k == "amusement park":
                k_tmp = "park"
            elif k == "theme park":
                k_tmp = "park"
            vec_key = embedding[k_tmp]
            # print("vec_word:", vec_word, "vec_key:", vec_key)
            dist = np.linalg.norm(vec_word-vec_key)
            
            if dist < min_dist:
                min_dist = dist
                nearest_key = k
                
    return nearest_key


