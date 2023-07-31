from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    route = [0] * (n+1)
    q = deque()

    for e in edge:
        e1 = e[0]
        e2 = e[1]
        graph[e1].append(e2)
        graph[e2].append(e1)

    q.append(1)
    route[1] = 1

    while q:
        now = q.popleft()
        for g in graph[now]:
            if route[g] == 0:
                q.append(g)
                route[g] = route[now] + 1

    max_edge = max(route)

    for r in route:
        if r == max_edge:
            answer += 1

    return answer