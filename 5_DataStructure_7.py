### Section5_DataStructure_문제7: 교육과정 설계 (큐)

from collections import deque
sub = list(input())
n = int(input())
for i in range(n):
    plan = deque(input())
    tmp = ""
    j = 0
    while plan and j<len(sub):
        if sub[j] == plan[0]:
            tmp += plan.popleft()
            j += 1
        else:
            plan.popleft()
    if tmp == ''.join(sub):
        print('#%d YES'%(i+1))
    else:
        print('#%d NO'%(i+1))



# 이런 풀이도 가능하다. 필수과목을 데크로 만든후, 임시로 만든 수업설계의 원소들을 데크의 첫원소들과 비교해서 같으면 popleft
from collections import deque
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print('#%d YES'%(i+1))
        else:
            print("#%d NO" %(i+1))