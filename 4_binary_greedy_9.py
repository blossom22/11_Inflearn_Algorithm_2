### Section4_Binary_Greedy_문제9: 증가수열 만들기(그리디)

from collections import deque
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
queue = deque(nums)
last = 0
lt = 0
rt = n-1
res = ""
tmp = []
while lt<=rt:
    if nums[lt]>last:
        tmp.append((nums[lt],'L'))
    if nums[rt]>last:
        tmp.append((nums[rt],'R'))
    tmp.sort()  # 추가된 튜플의 첫 원소(nums[lt]와 nums[rt])를 기준으로 오름차순 정렬을 한다
    if len(tmp)==0:     # 아무 원소도 추가 못하는 경우(마지막으로 본 수보다 양끝값이 작을때)
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()     # tmp를 초기화해서 다시 위 과정을 반복시켜
print(len(res))
print(res)
