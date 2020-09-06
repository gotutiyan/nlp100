col1_and_2 = open("col1_and_2.txt","w")
with open("hightemp.txt") as fp:
    for line in fp:
        line = line.rstrip().split("\t")
        col1_and_2.write("\t".join(line[0:2]) + "\n")
    
    

"""
unix command
> cut -f 1-2 hightemp.txt > col1_and_2.txt
"""
        