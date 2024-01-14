### Section3_Search_Simulation_문제11: 격자판 회문수

import sys
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        # 행방향 회문 검사(이건 쉬움)
        tmp = mat[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            # 아래코드는 열방향으로 회문이 있나 검사할때 쓰이는 것. 
            # 열방향 회문에서 첫 원소와 짝이되는 끝 원소가 같은지 쭉쭉 비교하는 것이다. 
            # 그런데, 회문이 5자리이므로, 1번째와 5번째 / 2번째와 4번째만 비교하면 되니까 for k in range(2)인 것 
            if mat[i+k][j] != mat[i+5-k-1][j]:
                break
        else:   # for k in range(2)문이 전부 잘 돌았다면, 열방향 회문인것이므로, cnt+=1
            cnt += 1 
print(cnt)