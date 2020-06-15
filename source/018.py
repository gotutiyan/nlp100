import sys
data = []
with open("hightemp.txt") as fp:
    for line in fp:
        line = line.rstrip().split("\t")
        data.append(line)
    data.sort(key=lambda x:x[2], reverse=True)
    for elem in data:
        print("\t".join(elem))


"""
unix command
> sort hightemp.txt -k 3,3 -n -r
"""
        