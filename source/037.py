def program_30():
    sentences = []
    with open('neko.txt.mecab') as fp:
        sentence = []
        for line in fp:
            morph_dic = morph_to_dict(line)
            sentence.append(morph_dic)
            if line[0]=='。':
                sentences.append(sentence)
                sentence = []
    return sentences
            
            
def morph_to_dict(morph):
    dic = {}
    morph = morph.split('\t')
    dic['surface'] = morph[0]
    if len(morph) >= 2:
        if len(morph[1].split(',')) >=6:
            dic['base'] = morph[1].split(',')[6]
        dic['pos'] = morph[1].split(',')[0]
        dic['pos1'] = morph[1].split(',')[1]
    return dic

# Number 30
sentences = program_30()

# Number 37
# 猫が含まれている文に存在する単語を，共起する単語とする．
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.font_manager._rebuild()
word2freq_with_cat = defaultdict(int)
for sentence in sentences:
    is_exist_cat = False
    for morph in sentence:
        if morph['surface'] == '猫':
            is_exist_cat = True
    if is_exist_cat:
        for morph in sentence:
            if morph['surface'] != '猫':
                word2freq_with_cat[morph['surface']] += 1
word2freq_with_cat_list = list(word2freq_with_cat.items())
sorted_word2freq_with_cat_list = sorted(word2freq_with_cat_list, key=lambda x:x[1], reverse=True)
# print(sorted_list[:10])
# [('の', 397), ('は', 284), ('、', 265), ('に', 251), ('を', 240), ('て', 236), ('。', 219), ('と', 210), ('が', 185), ('で', 175)]

top_word = sorted_word2freq_with_cat_list[:10]
words = [word[0] for word in top_word]
freqs = [word[1] for word in top_word]
print(words, freqs)
df = pd.DataFrame({'words': words, 'freqs': freqs})
sns.set(font=['IPAMincho'])
sns.barplot(x=df['words'], y=df['freqs'], color='#FF0000')
plt.savefig('./pic37.png')
plt.close()







"""
"""




    

