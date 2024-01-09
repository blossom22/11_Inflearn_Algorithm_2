### Section2_Implementation_8: 뒤집은 소수

# 소수인지 판별하는 함수
def prime(x):
    if x==1:
        return False
    else:
        for i in range(2,x//2+1):
            if x%i==0:
                return False
        return True
# 숫자를 뒤집는 함수
def reversing(x):
    tmp_list = list(str(x))
    tmp_list.reverse()
    tmp = int(''.join(tmp_list))
    return tmp

import sys
n = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    result = reversing(nl[i])
    if prime(result):
        print(result, end=' ')