#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ
sentence = "I am an NLPer"

def make_ngram(sentence, n):
    result = []
    for i in range(0,len(sentence) - n + 1):
        result.append(sentence[i:i+n])
    
    return result

print(make_ngram(sentence, 2))
words = sentence.split()
print(make_ngram(words, 2))