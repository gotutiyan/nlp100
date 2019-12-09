def make_ngram(sentence, n):
    result = []
    for i in range(0,len(sentence) - n + 1):
        result.append(sentence[i:i+n])
    
    return result

sent1 = "paraparaparadise"
sent2 = "paragraph"
X = make_ngram(sent1, 2)
Y = make_ngram(sent2, 2)
X = set(X)
Y = set(Y)

print("X", X)
print("Y", Y)
print("X|Y", X|Y)
print("X&Y", X&Y)
print("X-Y", X-Y)
if "se" in X:
    print("'se' in X")
else:
    print("'se' NOT in X")
if "se" in Y:
    print("'se' in Y")
else:
    print("'se' NOT in Y")