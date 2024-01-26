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


## 아래는 딕셔너리를 쓰지 않고 리스트로 풀어본 풀이이다 (아스키넘버 활용)
a = input()
b = input()
str1 = [0]*52   # 알파벳이 26개(대소문자 구분하면 52개)
str2 = [0]*52
for x in a:
    if x.isupper():
        # 대문자 알파벳은 65~90번 아스키넘버이므로, 이를 0~25번 인덱스로 만들려면 65를 빼야함
        str1[ord(x)-65] += 1
    else:
        # 소문자 알파벳은 97~122번이므로, 71을 빼야 인덱스번호가 26~51로 만들어진다
        str1[ord(x)-71] += 1
for x in b:
    if x.isupper():
        str2[ord(x)-65] += 1
    else:
        str2[ord(x)-71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print('NO')
        break
else:
    print("YES")