### Section3_Search_Simulation_문제8: 곳감(모래시계)
# 아래는 곳감을 회전시키는 코드. 데크를 사용하였다
from collections import deque
import sys
n = int(sys.stdin.readline())
mat = [deque(map(int, sys.stdin.readline().split())) for _ in range(n)]
m = int(sys.stdin.readline())
for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    if b==0:
        mat[a-1].rotate(-c)
    elif b==1:
        mat[a-1].rotate(c)
# 아래는 모래시계방향으로 곳감개수를 탐색하는 코드
cnt = 0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        cnt += mat[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(cnt)



### 데크를 사용하지 않고, 이런 풀이도 가능하다
import sys
n = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m = int(sys.stdin.readline())
for i in range(m):
    h,t,k = map(int,sys.stdin.readline().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))        # 0번 인덱스"를" pop한 것을 append한다.
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())      # 0번 인덱스"에" a[h-1]에서 pop을 한 것을 insert한다
cnt = 0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        cnt += mat[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(cnt)

