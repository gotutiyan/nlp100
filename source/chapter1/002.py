#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
s1 = "パトカー"
s2 = "タクシー"
ans = ""
for i in range(0,len(s1)):
    ans += s1[i]
    ans += s2[i]
print(ans)