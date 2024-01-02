### Section2_Implementation_4: 대표값

import sys
n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
mean = round(sum(score)/n)
minN = 2147000000

for idx, x in enumerate(score):
    tmp = abs(x-mean)
    if tmp<minN:
        minN = tmp
        a = x
        res = idx + 1
    elif tmp==minN:
        if x > a:
            a = x
            res = idx+1
print(mean, res)
