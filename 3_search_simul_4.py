### Section3_Search_Simulation_문제4: 두 리스트 합치기
# 단순히 두 리스트를 +연산자로 합치고 sort함수쓰면 안된다. (이경우, 시간복잡도가 nlogn)
# 이미 두 리스트가 오름차순 정렬되있다는 사실을 이용하면 O(n)=n으로 끝낼 수 있다

import sys
n = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ml = list(map(int, sys.stdin.readline().split()))
if n>m:
    n,m = m,n
    nl,ml = ml,nl
a = 0       # nl을 탐색할 포인터
b = 0       # ml을 탐색할 포인터
while a<n:
    if nl[a]<ml[b]:
        print(nl[a], end=' ')
        a += 1
    elif nl[a]>ml[b]:
        print(ml[b], end=' ')
        b += 1
    else:
        print(nl[a],ml[b], end=' ')
        a += 1
        b += 1
for i in range(m-b):
    print(ml[b+i], end=' ')




### 이런 풀이도 가능하다. 위에서 내가 푼 방식과 유사하나, 더 간결하다.
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
p1=p2=0
c = []
while p1<n and p2<m:    # 둘 중 한 포인터라도 끝에 도달하면 break
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:    # 이 경우, p1이 아직 n에 도달못한 것.
    c += a[p1:]
if p2<m:    # 이 경우, p2가 아직 m에 도달못한 것.
    c += b[p2:]
for x in c:
    print(x, end=' ')