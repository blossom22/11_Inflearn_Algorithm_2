### Section2_Implementation_6: 자릿수의 합

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
def digit_sum(x):
    sum = 0
    for i in str(x):    # 숫자를 문자열로 바꿔서 하나하나 뽑아낸다
        sum += int(i)
    return sum
max = 0
for x in a:
    tot = digit_sum(x)
    res = x
print(res)


# 그냥 10으로 계속나눠서 몫과 나머지를 이용하는 방법도 가능하다
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x = x//10
    return sum
max = 0
for x in a:
    tot = digit_sum(x)
    if tot>max:
        max = tot
        res = x 
print(res)
