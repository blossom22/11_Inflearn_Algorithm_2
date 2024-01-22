### Section4_Binary_Greedy_문제7: 창고 정리 (그리디)

import sys
l = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
box.sort()
m = int(sys.stdin.readline())
for i in range(m):
    box[0] += 1
    box[-1] -= 1
    box.sort()
print(box[-1]-box[0])