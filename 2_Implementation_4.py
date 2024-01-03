### Section2_Implementation_4: 대표값

import sys
n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
mean = round(sum(score)/n)
minN = 2147000000

for idx, x in enumerate(score):
    tmp = abs(x-mean)
    if tmp<minN:
        minN = tmp
        a = x
        res = idx + 1
    elif tmp==minN:
        if x > a:
            a = x
            res = idx+1
print(mean, res)

'''
주의할 점: 파이썬에서 round는 그냥 반올림 하는 것이 아니다.
round_half_even방식을 사용한다. 
예를들어, a=4.5000 처럼 정확하게 4와 5의 중간에 있으면, 반올림을 해서 5가 나오는게 아니라
짝수인쪽으로 바꿔준다. 즉, 4를 출력한다. 
그래서 위 코드에서 쓴 round는 적절하지 않다.
0.5를 더해서 int()로 묶는 해결책이 있다.
예를들어, 66.5였다면, 반올림한 결과로 int(66.5+0.5)하면 67이 나온다.
또는 66.6이었다면, 반올림한 결과로 int(66.6+0.5)하면 67이 나온다.
또는 66.1이었다면, 반올림한 결과로 int(66.1+0.5)하면, 66이 나온다. 
이런식으로 반올림을 해결할 수 있다.
'''

