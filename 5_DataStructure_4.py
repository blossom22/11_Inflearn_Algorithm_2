### Section5_DataStructure_문제4: 후위식 연산 (스택)
# 문제: 후위표기식을 계산한 결과를 출력해라
a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=="+":
            tmp = stack.pop() + stack.pop()
            stack.append(tmp)
        elif x=='-':
            tmp = stack[-2] - stack[-1]
            stack.pop()
            stack.pop()
            stack.append(tmp)
        elif x=='*':
            tmp = stack.pop() * stack.pop()
            stack.append(tmp)
        elif x=='/':
            tmp = stack[-2]/stack[-1]
            stack.pop()
            stack.pop()
            stack.append(tmp)
print(*stack)



# 위의 내 풀이와 아이디어는 같은 풀이다. 아래는 보기에 깔끔한 풀이
a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=='+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2+n1)
        elif x=='-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2*n1)
        elif x=='/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)
print(stack[0])