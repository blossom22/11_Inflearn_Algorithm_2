### Section3_Search_Simulation_문제3: 카드 역배치 (정올 기출)

import sys
mat = list(range(21))   # 인덱스번호 1~20번에 1~20값이 들어가게 초기 배열을 만든다
for i in range(10):
    a,b = map(int, sys.stdin.readline().split())
    mat[a:b+1] = mat[b:a-1:-1]      # 주어진 구간을 역순으로 바꾼다
print(mat[1:])  # 맨앞의 0번인덱스만 버리고 나머지를 출력한다



### 이런 풀이도 가능하다
import sys
mat = list(range(21))
for _ in range(10):
    a,b = map(int, sys.stdin.readline().split())
    for i in range((b-a+1)//2):     # 검색하는 수랑 정해준 구간내에서 대칭되는 수를 교환시키는 방식
        mat[a+i], mat[b-i] = mat[b-i], mat[a+i]
mat.pop(0)  # 0번인덱스를 pop시킨다
print(mat)