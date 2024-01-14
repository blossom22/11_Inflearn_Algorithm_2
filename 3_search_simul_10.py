### Section3_Search_Simulation_문제10: 스도쿠 검사
### 
def check(a):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):          # 여기서 i와 j는 전체 스도쿠에서 9개의 그룹을 보려는 것
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):  # 여기서 k,s는 한 그룹에서 9개의 수를 탐색하는 것
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1    # 한 그룹에서 9개의 원소를 탐색한다
            if sum(ch3) != 9:
                return False
    return True

import sys
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
if check(mat):
    print('YES')
else:
    print('NO')