### Section2_Implementation_5: 정다면체
# 리스트 하나 만들어서, 각 인덱스번호가 두 주사위에서 나온 숫자의 합이 되도록 설정후,
# 배열에서 1씩 값을 증가시켜서 수의 합이 나온 횟수를 카운팅하자
import sys
n,m = map(int, sys.stdin.readline().split())
cnt = [0]*(n+m+3)   # 3은 그냥 임의의 수임. cnt길이는 n+m보다 크기만 하면 된다
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j] += 1
maxx = max(cnt)
for a,b in enumerate(cnt):
    if b==maxx:
        print(a, end=' ')