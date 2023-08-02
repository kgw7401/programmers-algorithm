#1
# 순위를 매길 수 있다는건?
# 모든 그래프가 다 차있다는 것

def solution(n, results):
    answer = 0
    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = -1

    for result in results:
        winner = result[0]
        loser = result[1]
        graph[winner-1][loser-1] = 1 # 이겼다
        graph[loser-1][winner-1] = 2 # 졌다

    for k in range(n):
        for a in range(n):
            for b in range(n):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
                elif graph[a][k] == 2 and graph[k][b] == 2:
                    graph[a][b] = 2

    for g in graph:
        if 0 not in g:
            answer += 1

    return answer