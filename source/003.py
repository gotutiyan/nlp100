#"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
sentence="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words=sentence.split()
res=[]
for word in words:
    ans=0
    for c in word:
        if c.isalpha():
            ans+=1
    res.append(ans)
print(res)