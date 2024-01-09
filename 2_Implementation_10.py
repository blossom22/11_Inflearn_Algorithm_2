### Section2_Implementation_10: 점수계산

n = int(input())
q = list(map(int, input().split()))
ans = 0     # 실제 점수
tmp = 0     # 임시 변수
for i in range(n):
    if q[i]==1:
        tmp += 1
        ans += tmp
    else:
        tmp = 0
print(ans)