### Section5_DataStructure_문제11: 최대 힙
'''
최대힙은 최소힙과 반대로, 부모노드가 자식노드들보다 크면 된다. 즉, 루트노드가 가장 큰 값이겠지
기본적으로 heapq는 최소힙으로 작동한다. pop을 할때도 최소값을 출력하고, push할때도 최소힙을 만드려고 한다.
최대힙으로 작용시키려면, push를 할때 부호를 바꿔서 넣어버리면 된다.
그리고 나중에 출력할때, -만 다시 붙이면 되지~
'''
import heapq as hq
tree = []
while True:
    n = int(input())
    if n==-1:
        break
    elif n==0:
        if tree:
            print(-hq.heappop(tree))
        else:
            print(-1)
    else:
        hq.heappush(tree, -n)