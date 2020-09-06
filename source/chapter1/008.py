def cipher(sent):
    ret = ""
    for char in sent:
        if char.islower():
            ret += chr(219 - ord(char))
        else:
            ret += char
    return ret

ans = cipher("Sentence!!")
print(ans)

"""
Sentence!!
->>
Svmgvmxv!!
"""
