#1
# 한 번에 하나의 요청만 수행할 수 있음
# 각 작업마다 요청부터 종료까지 걸린 시간의 평균
# 요청 시간과 걸리는 시간이 주어짐
### 각 작업마다 요청부터 종료까지 걸린 시간의 평균의 최소(소수점 이하 수는 버린다) ###

#2
# jobs 길이 500
# 최대 요청 시간 1000
# 작업 수행 안할때는 먼저 들어온거 부터 수행

#3
# 무엇부터 처리해야 평균 시간이 짧아질까?
# 처리 시간은 줄일 수 없으니 대기 시간을 줄여야 한다
# 최대한 덜 기다리게 한다
# 작업이 짧은 순서대로 처리한다
# 현재 시점에서 할 수 있는 가장 짧은 일부터 처리한다

#4
# start < x < now 사이에 들어왔다면 힙에 push
# heap에 값이 있다면 가장 짧은 요청부터 pop
# 위의 과정 반복

import heapq

def solution(jobs):
    answer, start, now, t = 0, -1, 0, 0
    heap = []

    while True:
        if t == len(jobs):
            return answer // len(jobs)

        for job in jobs:
            if start < job[0] <= now:
                print(job)
                heapq.heappush(heap, (job[1], job[0]))

        if heap:
            j = heapq.heappop(heap)
            start = now
            now += j[0]
            answer += now - j[1]
            t += 1
        else:
            now += 1