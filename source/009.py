import random
def sent_shuffle(sent):
    sent = sent.rstrip().split()
    ret = []
    for word in sent:
        if len(word) > 4:
            ret.append(word[0] + ''.join(random.sample(word[1:-1],len(word[1:-1]))) + word[-1])
        else:
            ret.append(word)
    return ' '.join(ret)

ans = sent_shuffle("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
print(ans)

"""
output(one of example):
I cdoln'ut beileve that I cloud alcluaty uanrnsedtd what I was radieng : the ponnhmaeel peowr of the human mind .
"""