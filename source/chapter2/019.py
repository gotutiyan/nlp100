with open("hightemp.txt") as fp:
    col1_to_freq = {}
    for line in fp:
        line = line.rstrip().split("\t")
        col1_to_freq[line[0]] = col1_to_freq.get(line[0], 0) + 1
    col1_score = [[col1, freq] for col1, freq in col1_to_freq.items()]
    col1_score.sort(key=lambda x:x[1], reverse=True)
    for elem in col1_score:
        print(elem)


"""
unix command
> cut -f 1 hightemp.txt | sort | uniq -c | sort -r
"""
        