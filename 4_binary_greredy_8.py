### Section4_Binary_Greedy_문제8: 침몰하는 타이타닉(그리디)

from collections import deque
import sys
n,m = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))
weight.sort()
weight = deque(weight)
cnt = 0
while weight:
    if len(weight)==1:      # 만약 마지막 1명만 남는 경우에 대한 예외처리가 필요하다
        cnt+=1
        break
    if weight[0]+weight[-1] > m:    # 처음 원소와 끝 원소를 더해서 만약 m보다 크면 끝 원소는 혼자 구명보트 태워(pop시켜)
        weight.pop()
        cnt += 1
    else:               # 양끝을 더한게, m이하면, 그 조합이 구명보트 탈 수 있는 최대무게 조합이므로, 각각 weight에서 pop, popleft시켜
        weight.popleft()
        weight.pop()
        cnt += 1
print(cnt)