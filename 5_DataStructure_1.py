### Section5_DataStructure_문제1: 가장 큰 수 (스택)

import sys
n,m = map(int, sys.stdin.readline().split())
nums = list(map(int, str(n)))
stack = []
cnt = 0
i = 0
while True:
    if cnt<m and i<len(nums):
        if stack:
            if stack[-1] < nums[i]:
                stack.pop()
                cnt += 1
            else:
                stack.append(nums[i])
                i += 1
        else:
            stack.append(nums[i])
            i += 1
    elif cnt==m:
        stack.extend(nums[i:])
        print(*stack, sep='')
        break
    elif i==len(nums):          # 만약 cnt를 다 못채웠다면, 맨 뒤의 것들에서 나머지 필요한만큼 제거해야지
        for j in range(m-cnt):
            stack.pop()
        print(*stack, sep='')
        break



### 이 풀이가 더 좋은 풀이이다. 
import sys
num, m = map(int, sys.stdin.readline().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m -= 1      # 지워야하는 개수를 하나씩 줄여
    stack.append(x)
if m!=0:
    stack = stack[:-m]      # 만약 더 지웠어야는데 pop되지 않고 append되어있는 경우, stack[:-m]만 답이므로, 슬라이싱해
res = "".join(map(str, stack))  # stack의 원소는 현재 int여서 바로 join안됨. map거쳐라
print(res)