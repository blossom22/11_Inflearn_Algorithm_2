### Section3_Search_Simulation_문제2: 숫자만 추출
import sys
n = list(sys.stdin.readline().strip())
num = ''
# 숫자를 찾아내는 코드
for i in n:
    if i.isdecimal():   # isdigit은 숫자모양이면 True, isdecimal은 주어진 문자열이 정수형(0~9)인 경우만 True, isnumeric은 숫자, 제곱근, 분수까지 다 True
        num += i
num = int(num)
print(num)
# 약수를 구하는 코드
ans = 0
for i in range(1,num+1):
    if num%i==0:
        ans += 1
print(ans)

