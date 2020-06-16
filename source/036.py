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

# Number 35
from collections import defaultdict
word2freq = defaultdict(int)
for sentence in sentences:
    nouns = []
    for i, morph in enumerate(sentence):
        word2freq[morph['surface']] += 1
        
word2freq_list = list(word2freq.items())
sorted_word2freq_list = sorted(word2freq_list, key=lambda x:x[1], reverse=True)

# Number 36
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
top_word = sorted_word2freq_list[:10]
words = [word[0] for word in top_word]
freqs = [word[1] for word in top_word]
print(words, freqs)
df = pd.DataFrame({'words': words, 'freqs': freqs})
sns.set(font=['IPAMincho'])
sns.barplot(x=df['words'], y=df['freqs'], color='#FF0000')
plt.savefig('./pic36.png')
plt.close()



"""
"""




    

