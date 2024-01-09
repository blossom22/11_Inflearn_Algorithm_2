### Section2_Implementation_7: 소수 (에라토스테네스 체)
# 이 방법은 소수를 구하는 가장 빠른 방법 중 하나이다. 
# 에라토스테네스 체: 범위에서 합성수를 지우는 방식으로 소수를 찾는다.
# 일단 1은 제거하고, 2를 소수취급+2의배수들은 전부 제거, 3을 소수취급+3의배수들은 전부 제거...이런 방식으로 합성수를 제거한다
# 그러기위해서는 인덱스1번자리 False, 인덱스2번~n번까지는 True인 초기 배열(아래의 nl)이 필요하다. True이면 소수취급~
import sys
n = int(sys.stdin.readline())
# 인덱스 0번자리는 차피 필요없으니까 그냥 False로 초기설정함
nl = [False] + [False] + [True]*(n-1)
prime = []
for i in range(2,n+1):
    if nl[i]:
        prime.append(i)
        for j in range(i*2, n+1, i):
            nl[j] = False
print(len(prime))



# 위 코드랑 비슷한 원리이다. 0인 곳은 소수, 1인 곳은 합성수로 생각한 것
n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2,n+1):
    if ch[i] == 0:
        cnt +=1
        for j in range(i,n+1, i):
            ch[j]=1
print(cnt)