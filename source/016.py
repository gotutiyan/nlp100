import sys
lines = []
with open("hightemp.txt") as fp:
    for line in fp:
        lines.append(line.rstrip())
n = int(sys.argv[1])
sz = len(lines)
for i in range(n):
    idx = int(i)
    # a//bの切り上げ：(a+b-1)//b
    print('\n'.join(lines[(sz+n-1)//n*idx : (sz+n-1)//n*(idx+1)]))
    print()

"""
unix command
(nは自然数)
> split -n hightemp.txt
"""
        