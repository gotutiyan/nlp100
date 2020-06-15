with open("hightemp.txt") as fp:
    col1_to_freq = {}
    for line in fp:
        line = line.rstrip().split("\t")
        col1_to_freq[line[0]] = col1_to_freq.get(line[0],0) + 1
    for elem in list(col1_to_freq.keys()):
        print(elem)


"""
unix command
> cut -f 1 hightemp.txt | sort | uniq
"""
        