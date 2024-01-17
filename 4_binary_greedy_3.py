### Section4_Binary_Greedy_문제3: 뮤직비디오 (결정알고리즘)
import sys

def Count(capacity):
    cnt = 1     # DVD의 개수(곡의 개수아님!)
    hap = 0
    for x in song:
        if hap + x > capacity:      # 임시로 정한 최대용량보다 커지면 안되니까, 이때 다음 DVD사용해야지
            cnt += 1
            hap = x
        else:
            hap += x
    return cnt

n,m = map(int, sys.stdin.readline().split())
song = list(map(int, sys.stdin.readline().split()))
ans = 0 
left = 1
right = sum(song)
while left<=right:
    mid = (left + right)//2
    if Count(mid) <= m:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)