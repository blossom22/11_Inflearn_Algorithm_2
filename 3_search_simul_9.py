### Section3_Search_Simulation_문제9: 봉우리
# 간단한 시뮬레이션 문제이다
import sys
n = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 0
for i in range(n):
    for j in range(n):
        mark = True
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx>=0 and nx<n and ny>=0 and ny<n and mat[i][j]<=mat[nx][ny]:
                mark = False
        if mark:
            ans += 1
print(ans)



### 이런 풀이도 가능하다. 여기서는 실제로 0으로 이뤄진 패딩을 만들고 진행했다
import sys
n = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mat.insert(0,[0]*n)     # 0번위치에 [0]*n을 추가했다
mat.append([0]*n)       # 맨뒤에 [0]*n추가했다
for x in mat:
    x.insert(0,0)
    x.append(0)
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        # 4방향 탐색하는 과정을 아래처럼 간략하게 줄일 수 있다
        if all(mat[i][j]>mat[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt +=1
print(cnt)