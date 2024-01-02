### Section2_Implementation_1: k번째 약수
## 간단한 문제이다. 
import sys
n,k = map(int, sys.stdin.readline().split())
m = [i for i in range(1,n+1) if n%i==0]
print(m[k-1]) if len(m)>=k else print(-1)


## 이런 풀이도 가능하다.
n,k = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(1,n+1):
    if n%i==0:
        cnt +=1
    if cnt == k:
        print(i)
        break
# 만약 위의 for문을 정상적으로 다 돌았다면(break을 안 만났다면), print(-1)
else:
    print(-1)