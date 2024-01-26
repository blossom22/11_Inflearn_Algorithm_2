### Section5_DataStructure_문제5: 공주 구하기 (큐)

from collections import deque
import sys
n,k = map(int, sys.stdin.readline().split())
queue = deque(range(1,n+1))
while len(queue)>1:
    for _ in range(k-1):
        queue.append(queue.popleft())
    queue.popleft()
print(queue[0])