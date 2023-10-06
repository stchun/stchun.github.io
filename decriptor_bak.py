# %%
special_char = [' ', '.', ',', '!', '?', '~']
def char_tokenize(str):
    char_list = []
    word_index = 1
    for word in str.split('#'):
        for char in word.split('*'):
            sp = ''

            for ch in char:
                if ch in special_char:
                    sp = ch

            if sp == '':
                char_list.append(char)
            else:
                index = 1
                sp_list = char.split(sp)

                for tok in sp_list:
                    if len(tok) > 0:
                        char_list.append(tok)

                    if index < len(sp_list):
                        char_list.append(sp)
                    index += 1

        if word_index < len(str.split('#')):
            char_list.append(' ')
        word_index += 1
        
    return char_list

# %%
import numpy as np
max_arr_len = 15

def string_split(dataset):
    ret = []
    for data in dataset:
        data_arr = []

        for char in data[0]:
            data_arr.append(int(char))
        
        while len(data_arr) < max_arr_len:
            data_arr.append(-1)
        
        # print(data_arr, len(data_arr))
        
        ret.append(data_arr)
    return ret

# %%
import pandas as pd
from sklearn import tree

def learn_model():
    data = pd.read_excel('data.xlsx', dtype={'암호문':str})

    X = string_split(data['암호문'].to_numpy().reshape(-1, 1))
    Y = data['평문'].to_numpy()

    model = tree.DecisionTreeClassifier()
    model = model.fit(X, Y)
    return model

# %%
def convert(tok, model):
    ret = model.predict(string_split([[tok]]))

    return ret[0]

# %%
def decrpit(str, model):
    out_list = []
    tok_list = char_tokenize(str)
    ret = ''
    for index in range(len(tok_list)):
        if tok_list[index] not in special_char:
            out_list.append(convert(tok_list[index], model))
        else:
            out_list.append(tok_list[index])
    
    for ch in out_list:
        ret += ch
            
    return ret

# %%
from matplotlib import pyplot as plt

if __name__ == "__main__":
    # input_val = input()
    # input_val = '0125*52210#821*02210*012.'
    input_val = '621*6324#9127*012*5512!!*7127*623*6324'
    print(input_val)

    clf = learn_model()
    output = decrpit(input_val, clf)
    print(output)

    plt.figure(figsize=(20,20))
    tree.plot_tree(clf, fontsize=5)
    plt.show()

