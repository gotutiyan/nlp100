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

# Number 33
connect_set = set()
for sentence in sentences:
    for i, morph in enumerate(sentence):
        if morph['surface'] == 'の' and i>0 and i<len(sentence)-1 and sentence[i-1]['pos']=='名詞' and sentence[i+1]['pos']=='名詞':
            connect_set.add(sentence[i-1]['surface'] + sentence[i]['surface'] + sentence[i+1]['surface'])
            
print(connect_set)
"""
{'主人の先君', '仏陀の福音', 'これしきの事', '方のため',
..... , '穴の横', '最前の倒行', '化物の競争', '彼の朦朧', '源の前'}
"""




    

