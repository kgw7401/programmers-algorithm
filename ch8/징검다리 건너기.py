#1.
# 징검다리가 있고 밟을 때마다 -1씩 밟을 수 있는 횟수가 줄어든다
# 무조건 다음 돌로 건너야 된다
# k 이상으로는 못 건넌다
# 건널 수 있는 최대 인원 # answer
# 무조건 이진탐색

#2.
# answer를 최대로 잡고 줄여가면서 계산한다
# answer를 stones에 빼준다
# 만약 음수면 answer를 타노스
# 모두 양수면 answer를 늘린다
# 만약 0이 나오면 0이 아닌 이전 돌과의 거리를 계산해서 k와 비교
# 만약 k보다 크면 answer를 줄인다
# k보다 작거나 같으면 answer를 늘린다

#3.
def solution(stones, k):
    answer = 0

    start, end = 0, max(stones)

    while start <= end:
        mid = (start + end) // 2

        first_zero = 0
        available = True
        for i in range(len(stones)):
            if stones[i] - mid < 0:
                first_zero += 1
                if first_zero >= k:
                    available = False
                    break
            else:
                first_zero = 0

        if available:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer
