### Section5_DataStructure_문제3: 후위표기식 만들기 (스택)
# 문제: 중위표기식이 주어지면 후위표기식으로 변환해라 

a = input()
stack = []      # 이 스택에는 연산자들만 넣는다
res = ""
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x=="(":      # 여는 괄호는 무조건 stack에 첨가
            stack.append(x)
        elif x=="*" or x=="/":      
            # *, /는 자기들과 우선순위가 같은 놈들이 앞에 있다면, pop해서 앞에 있는 애들을 꺼내야함.
            while stack and (stack[-1]=="*" or stack[-1]=='/'):
                res += stack.pop()
            stack.append(x)     # 앞의 우선순위가 같은 놈들을 다 뽑았으면 자기자신은 stack에 첨가
        elif x=='+' or x=='-':      # +,-들은 앞에 있는 놈들은 전부 얘네보다 우선순위가 빠르다. 
            # 심지어 같은 +,-들 사이이더라도, 스택의 앞쪽에 있는 애들이 먼저 나온 연산자이므로, 우선순위가 더 빠르다고 할 수 있지.
            # 따라서 그냥 위에서 한 것처럼 스택에서 다 뽑아내면 된다(단 여는괄호를 만나기 전까지!)
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)     # 다 뽑았으면 자기자신은 stack에 첨가
        elif x==')':
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop() # 여는 괄호는 없애야지
while stack:
    res += stack.pop()
print(res)