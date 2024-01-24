### Section5_DataStructure_문제2: 쇠막대기 (스택)

s = list(input())
stack = []
res = 0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        if s[i-1]=='(':
            stack.pop()
            res += len(stack)
        # 쇠막대기 끝 지점에 대해서는 아래 코드가 실행됨(막대의 마지막 조각 1개씩만 더해주면 된다)
        else:
            stack.pop()
            res += 1
print(res)