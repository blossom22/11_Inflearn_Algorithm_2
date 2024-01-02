### Section2_Implementation_2: k번째 수
# 간단한 문제이다. 일부만 추출해서 오름차순 정렬후, k번째 수를 출력하면 된다.

import sys
t = int(sys.stdin.readline())
for i in range(t):
    n,s,e,k = map(int, sys.stdin.readline().split())
    nl = list(map(int, sys.stdin.readline().split()))
    print('#%d %d' %(i+1, sorted(nl[s-1:e])[k-1]))