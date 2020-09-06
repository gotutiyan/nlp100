number_of_lins = 0
with open("hightemp.txt") as fp:
    for line in fp:
        number_of_lins += 1
print(number_of_lins)


"""
unix command
> wc -l hightemp.txt
     24 hightemp.txt
"""