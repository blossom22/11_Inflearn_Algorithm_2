### Section5_DataStructure_문제6: 응급실 (큐)

from collections import deque
import sys
n,m = map(int, sys.stdin.readline().split())
ems = deque(map(int, sys.stdin.readline().split()))     # 위험도가 담긴 큐
nums = deque(range(n))      # 난 여기서 사람들의 번호가 담긴 큐를 하나 더 만들었다
cnt = 0

while m in nums:        # m번째 사람이 아직 대기목록에 있다면 계속 이 과정을 진행
    x = ems[0]
    if max(ems)>x:
        ems.append(ems.popleft())
        nums.append(nums.popleft())     # 위험도가 낮아서 대기목록의 맨뒤로 보낼때, 사람들의 번호도 함께 뒤로 보냈다
    else:
        ems.popleft()
        nums.popleft()      # 한명씩 진료를 볼때마다 cnt +=1
        cnt += 1
print(cnt)


# 이런 풀이도 가능하다. (enumerate을 사용해서 순서랑 위험도를 함깨 담았다)
from collections import deque
import sys
n,m = map(int, sys.stdin.readline().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, sys.stdin.readline().split())))]        # 위에서 했던 풀이는 위험도랑 순서를 따로 담았는데 그냥 옆에처럼 enumerate로 한번에 받으면 편함
Q = deque(Q)
cnt = 0
while True:
    current = Q.popleft()
    if any(current[1]<x[1] for x in Q):     # Q의 자료를 하나하나(x) 읽으면서 x[1]이 current[1]보다 큰게 하나라도 있으면 True(위험도가 현재 보는 놈보다 큰게 한명이상 있다면~)
        Q.append(current)
    else:
        cnt+=1
        if current[0]==m:
            print(cnt)
            break