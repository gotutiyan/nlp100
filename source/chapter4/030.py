def main():
    sentences = []
    with open('neko.txt.mecab') as fp:
        sentence = []
        for line in fp:
            morph_dic = morph_to_dict(line)
            sentence.append(morph_dic)
            if line[0]=='。':
                sentences.append(sentence)
                sentence = []
        print(sentences[:1])
        """
        output:
        [[{'surface': '一', 'base': '一', 'pos': '名詞', 'pos1': '数'}, 
        {'surface': '\u3000', 'base': '\u3000', 'pos': '記号', 'pos1': '空白'}, 
        {'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'}, 
        {'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '係助詞'}, 
        {'surface': '猫', 'base': '猫', 'pos': '名詞', 'pos1': '一般'}, 
        {'surface': 'で', 'base': 'だ', 'pos': '助動詞', 'pos1': '*'}, 
        {'surface': 'ある', 'base': 'ある', 'pos': '助動詞', 'pos1': '*'}, 
        {'surface': '。', 'base': '。', 'pos': '記号', 'pos1': '句点'}]]
        """
            
            
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

main()



    

