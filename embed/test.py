import numpy as np
import pickle
from tqdm import tqdm


def load_glove_model(file):
    print("Loading Glove Model")
    glove_model = {}
    numlines = 2196017
    with open(file,'r') as f:
        for line in tqdm(f, total=numlines):
            split_line = line.split()
            word = split_line[0]
            try:
                embedding = np.array(split_line[1:], dtype=np.float64)
                glove_model[word] = embedding
            except Exception as e:
                print(e)
    print(f"{len(glove_model)} words loaded!")
    return glove_model
m = load_glove_model("glove.840B.300d.txt")

with open('wordEmbed.pickle', 'wb') as handle:
    pickle.dump(m, handle, protocol=pickle.HIGHEST_PROTOCOL)
print(len(m))
