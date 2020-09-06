import sys
lines = []
with open("hightemp.txt") as fp:
    for line in fp:
        lines.append(line.rstrip())
n = int(sys.argv[1])
print('\n'.join(lines[-n:]))
        
    
    

"""
unix command
(nは自然数)
> tail -n hightemp.txt
"""
        