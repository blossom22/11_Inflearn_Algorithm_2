### Section3_Search_Simulation_문제5: 수들의 합
import sys
n,m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(n):
    for j in range(n):
        if sum(a[i:j+1]) == m:
            cnt += 1
        else:
            continue
print(cnt)



### 이런 풀이도 가능하다. 포인터 2개를 설정해서 부분합을 구하는 방식이다.
import sys
n,m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
lt = 0
rt = 1 
cnt = 0
tot = a[0]  # tot는 lt인덱스위치부터 rt인덱스 바로 전 위치까지의 부분합을 의미한다. 초기에는 a[0]만을 tot가 가진다고 가정하자
while True:
    if tot<m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot==m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)