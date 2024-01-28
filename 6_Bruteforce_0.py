### Section6_Bruteforce_선수지식: 재귀함수와 스택

# 간단한 재귀함수: n~1까지 수를 출력한다.
def DFS(x):
    if x>0:
        print(x)    # 이 줄을 아래 DFS(x-1)과 자리를 바꾸면, 1~n으로 수가 출력된다.(이유는 재귀함수가 스택을 쓰기 때문)
        DFS(x-1)
if __name__ == "__main__":
    n = int(input())
    DFS(n)
# 스택을 이용해서 재귀가 돌아가는 것을 잊지 말자. 과정 복습하기
