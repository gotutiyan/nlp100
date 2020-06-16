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
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
word2freq = defaultdict(int)
for sentence in sentences:
    nouns = []
    for i, morph in enumerate(sentence):
        word2freq[morph['surface']] += 1

# Number 38
wordfreq2freq = defaultdict(int)
for word, freq in word2freq.items():
    wordfreq2freq[freq] += 1
x = list(wordfreq2freq.keys())
y = list(wordfreq2freq.values())
df = pd.DataFrame({'x':x, 'y':y})

plt.figure(figsize=[1000,500])
plt.yscale('log')
plt.xscale('log')
sns.barplot(x=df['x'], y=df['y'], color="#FF0000")
plt.show()
plt.savefig('pic39.png')
plt.close()

"""
Attempted to set non-positive left xlim on a log-scaled axis.
Invalid limit will be ignored.
  ax.set_xlim(-.5, len(self.plot_data) - .5, auto=None)

とエラーが出るので画像サイズを広げると

ValueError: Image size of 100000x50000 pixels is too large. It must be less than 2^16 in each direction.
のエラーが出て画像を保存できないため，詰まっている
"""









"""
"""




    

