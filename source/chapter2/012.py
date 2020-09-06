col1 = open("col1.txt","w")
col2 = open("col2.txt","w")
with open("hightemp.txt") as fp:
    for line in fp:
        line = line.rstrip().split("\t")
        col1.write(line[0]+"\n")
        col2.write(line[1]+"\n")
col1.close()
col2.close()
    

"""
unix command
> cut -f 1 hightemp.txt > col1.txt
> cut -f 2 hightemp.txt > col2.txt
"""
        