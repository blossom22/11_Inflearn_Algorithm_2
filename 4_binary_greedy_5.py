### Section4_Binary_Greedy_문제5: 회의실 배정(그리디)
# 회의를 겹치지 않게 하면서 최대한 많은 회의를 하게 만들때 할 수 있는 회의의 개수는?
import sys
n = int(sys.stdin.readline())
conf = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
conf.sort(key=lambda v:(v[1],v[0]))  # 회의가 "끝나는 시간"을 기준으로 정렬해야한다. 회의 시작 시간을 기준으로 정렬해봤자, 끝나는 시간이 늦으면 아무 의미없음
ans = 1
k = 0
for i in range(1,n):
    if conf[k][1]<=conf[i][0]:
        ans += 1
        k = i
print(ans)



# 또는 아래처럼해도 된다. 
import sys
n = int(sys.stdin.readline())
conf = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
conf.sort(key=lambda v:(v[1],v[0])) 
et = 0   # 회의가 끝나는 시간
cnt = 0
for s,e in conf:
    if s >= et:     # 회의시작시간이 끝나는 시간보다 크거나 같으면, 그 회의를 하고 et를 업데이트
        et = e
        cnt += 1
print(cnt)