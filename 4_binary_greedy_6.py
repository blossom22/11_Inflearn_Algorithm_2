### Section4_Binary_Greedy_문제6: 씨름 선수(그리디)
# 몸무게로 정렬해서 풀었다. 
import sys
n = int(sys.stdin.readline())
man = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
man.sort(key=lambda v:(v[1]))

cnt = 0     # 씨름선수가 될 수 없는 애들을 카운트하자
for i in range(n-1):
    for j in range(i+1,n):
        if man[i][0]<man[j][0]:
            cnt += 1
            break
print(n-cnt)


# 위같은 이중 for문은 비효율적이다. for문 하나로 끝내자.
# 키 순으로 내림차순 정렬후, 나보다 키 큰 놈들보다 몸무게가 더 커야 씨름선수 가능하다.
# 몸무게 최대값을 새롭게 갱신할 수 있으면, cnt+=1하고, maxx=y로 새롭게 업데이트하면 된다.
import sys
n = int(sys.stdin.readline())
man = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
man.sort(key=lambda v:(-v[0]))
# 위의 sort를 그냥 man.sort(reverse=True)하면 첫번째 원소(여기서는 키)를 기준으로 내림차순정렬함
cnt = 0 
maxx = 0
for x,y in man:
    if y > maxx:
        maxx = y
        cnt += 1
print(cnt)