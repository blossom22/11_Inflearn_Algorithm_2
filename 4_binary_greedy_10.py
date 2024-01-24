### Section4_Binary_Greedy_문제10: 역수열(그리디)

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ch = [0]*n

for i in range(n):
    for j in range(n):
        # 아래 if문은 자기자리를 찾아 들어간 것
        if a[i]==0 and ch[j]==0:    # 여기서 a[i]=0의 뜻은 자기보다 큰 수가 들어갈 빈공간을 자기 앞에 확보했다는 것이다
            ch[j] = i+1
            break   # for j 문을 break한다
        # 아래 elif문은 자기자리를 아직 찾지 못한 것
        elif ch[j]==0:  # ch리스트를 탐색할때, ch에서 0인 곳에 내가 관심있는 수(i+1)보다 큰 놈들이 들어갈테니, a[i] -= 1 
            a[i] -= 1
print(*ch)