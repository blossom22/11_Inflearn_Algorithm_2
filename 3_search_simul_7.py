### Section3_Search_Simulation_문제7: 사과나무(다이아몬드)

import sys
n = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0
s=e=n//2    # 다이아몬드를 행방향으로 잘랐을때, 시작점이 s, 끝점이 e
for i in range(n):
    for j in range(s,e+1):
        ans += mat[i][j]
    if i<n//2:      # 다이아몬드 가로길이가 최대이기 전까지만, s-=1, e+=1 해야함
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(ans)