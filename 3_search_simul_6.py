### Section3_Search_Simulation_문제6: 격자판 최대합

import sys
n = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0

# 행방향, 열방향 조사
for i in range(n):
    sum1 = 0    # 행방향 합
    sum2 = 0    # 열방향 합
    for j in range(n):
        sum1 += mat[i][j]
        sum2 += mat[j][i]
        ans = max(ans, sum1, sum2)
# 대각선방향 조사
hap1 = 0    # 좌측상단~우측하단 대각선
hap2 = 0    # 우측상단~좌측하단 대각선
for i in range(n):
    for j in range(n):
        if i==j:
            hap1 += mat[i][j]
        if i+j == (n-1):
            hap2 += mat[i][j]
ans = max(ans, hap1, hap2)
print(ans)


### 대각선방향 조사부분을 아래처럼 바꿀수도 있다
hap1=hap2=0
for i in range(n):
    hap1+=mat[i][i]
    hap2+=mat[i][n-i-1]
ans = max(ans, hap1, hap2)
print(ans)