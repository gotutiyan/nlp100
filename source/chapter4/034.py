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

# Number 34
nouns_set = set()
for sentence in sentences:
    nouns = []
    for i, morph in enumerate(sentence):
        if morph['pos'] == '名詞':
            nouns.append(morph['surface'])
        else:
            if nouns != []:
                nouns_set.add(' '.join(nouns))
            nouns = []
            
print(nouns_set)
"""
{'枝振り', 'シドニー', '一 たび 服装',
..... , '一 晩', '一 歳', '来訪'}
"""




    

