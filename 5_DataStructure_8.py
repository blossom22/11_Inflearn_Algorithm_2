### Section5_DataStructure_문제8: 단어 찾기 (해쉬)

from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for i in range(n):
    s = input()
    dic[s] += 1
for i in range(n-1):
    s = input()
    del dic[s]
for i in dic.keys():
    print(i)

