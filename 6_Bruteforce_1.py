### Section6_Bruteforce_문제1: 재귀함수를 이용한 이진수 출력

import sys
n = int(sys.stdin.readline())
ans = []
def DFS(x):
    global ans
    if x//2==1:
        ans.append(x%2)
        ans.append(x//2)
    else:
        ans.append(x%2)
        return DFS(x//2)
DFS(n)
k = len(ans)
for i in range(k-1,-1,-1):
    print(ans[i], end='')



## 아래 풀이가 더 간결하고 좋다. 
n = int(input())
def DFS(x):
    if x==0:
        return  # x가 0이되면 종료
    else:
        # 아래 두 식을 거꾸로 쓰면, 답이 거꾸로 나온다. (스택)
        DFS(x//2)   # x//2몫을 재귀함수로 들어가
        print(x%2, end='')  # x=0되어서 DFS(0)이 pop되면, 이제 저장되었던 스택프레임들이 하나씩 호출되면서 print되겠지
DFS(n)