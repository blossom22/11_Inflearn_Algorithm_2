### Section2_Implementation_3: k번째 큰 수
# 문제조건: 세 수를 합한 결과가 같은 결과들이 여러개면 1개 취급을 한다. 
import sys
n,k = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))
answer = set()

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            if i!=j and j!=m:
                # set자료형에서 add함수는 list에서 append같은 것이다
                answer.add(nlist[i]+nlist[j]+nlist[m])
print(sorted(answer)[-k])