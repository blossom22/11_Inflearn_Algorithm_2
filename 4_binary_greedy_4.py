### Section4_Binary_Greedy_문제4: 마구간 정하기 (결정알고리즘)

import sys

def Count(len):
    cnt = 1
    end_point = horse[0]
    for i in range(1,n):
        if horse[i] - end_point >= len:
            cnt += 1
            end_point = horse[i]
    return cnt

n,c = map(int, sys.stdin.readline().split())
horse = sorted([int(sys.stdin.readline()) for _ in range(n)])
left = 1            # 두 마구간의 최소거리니까 1
right = horse[n-1]  # 두 마구간의 최대거리여서.
while left <= right:
    mid = (left+right)//2
    if Count(mid)>=c:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)