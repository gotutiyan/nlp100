with open("hightemp.txt") as fp:
    result = []
    for line in fp:
        line = line.rstrip()
        changed_line = ""
        for char in line:
            if char == "\t":
                changed_line += " "
            else:
                changed_line += char
        result.append(changed_line)
    print("\n".join(result))

"""
unix command
(手元ではうまくできませんでしたが，これ以外に思いつかないので載せておきます．多分何かが違うんだとは思います．)
> sed 's/\t/ /g' hightemp.txt
"""
        