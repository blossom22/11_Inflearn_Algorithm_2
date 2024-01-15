### Section4_Binary_Greedy_문제1: 이분검색
# 간단한 이분탐색문제이다. left, right, mid변수를 활용한다
# 시간복잡도 O(logn)으로 효율적인 방법이다. 
import sys
n,m = map(int, sys.stdin.readline().split())
nl = list(map(int, sys.stdin.readline().split()))
nl.sort()
left = 0
right = n-1
while left<=right:
    mid = (left+right)//2
    if nl[mid]==m:
        print(mid+1)
        break
    elif nl[mid]<m:
        left = mid + 1
    else:
        right = mid - 1
