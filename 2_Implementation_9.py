### Section2_Implementation_9: 주사위 게임

import sys
n = int(sys.stdin.readline())
max_money = 0
for i in range(n):
    temp_money = 0
    a,b,c = map(int, sys.stdin.readline().split())
    if a==b==c:
        temp_money = 10000 + a*1000
    elif a!=b and b!=c and a!=c:
        temp_money = max(a,b,c)*100
    else:
        if a==b or a==c:
            temp_money = 1000*a + 100
        else:
            temp_money = 1000*b + 100
    max_money = max(max_money, temp_money)
print(max_money)
