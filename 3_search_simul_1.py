### Section3_Search_Simulation_문제1: 회문 문자열 검사
# 아래는 파이썬 스러운 풀이이다. 다만, 간혹 면접에서 이런 식으로 풀지말고 아래아래에 있는 코드처럼
# 직접 코드를 짜보라고도 한다. 두 방식 모두 알아둘 것! 
n = int(input())
a = [input().lower() for _ in range(n)]
for i in range(n):
    if a[i]==a[i][::-1]:
        print('#%d %s' %(i+1, 'YES'))
    else:
        print('#%d %s' %(i+1, 'NO'))



# 이런 풀이도 가능하다. 파이썬스럽지는 않지만, 이렇게 직접 회문을 검색하는 방식은 면접에서 나올수도 있으므로 알아야한다. 
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    # 한 문자에서 처음과 끝이 같은지 보는 것
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NP" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
