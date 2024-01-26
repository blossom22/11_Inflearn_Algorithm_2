### Section5_DataStructure_문제9: 아나그램 (딕셔너리해쉬)

from collections import defaultdict
a = input()
b = input()
adic = defaultdict(int)
bdic = defaultdict(int)
for x in a:
    adic[x] += 1
for x in b:
    bdic[x] += 1 
if adic == bdic:
    print('YES')
else:
    print("NO")


## 아래는 defaultdict을 쓰지 않으면서 딕셔너리는 하나만 쓰는 풀이이다. 
a = input()
b = input()
sH = dict()
for x in a:
    sH[x] = sH.get(x, 0) + 1    # sH에서 x값이 key로 존재하면 그 값을 출력하고 1을 더해. key로 존재 안하면 0으로 출력하고 1을 더해~라는 소리
for x in b:
    sH[x] = sH.get(x, 0) - 1 
for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")