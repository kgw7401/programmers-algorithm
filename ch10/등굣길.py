# 마지막 1000000007을 까먹고 있었다
# 앞으로는 무조건 위에 조건 적어놓고 풀자

def solution(m, n, puddles):
    answer = 0
    # 기본 지도 세팅
    graph = [[0] * m for _ in range(n)]
    for puddle in puddles:
        x = puddle[0] - 1
        y = puddle[1] - 1
        graph[y][x] = -1
    graph[0][0] = 1
    for y in range(n):
        for x in range(m):
            if (x == 0 and y == 0) or graph[y][x] == -1:
                continue
            if y-1 < 0:
                graph[y][x] += graph[0][x-1]
            elif x-1 < 0:
                graph[y][x] += graph[y-1][0]
            else:
                prevs = [[0, -1], [-1, 0]]
                for prev in prevs:
                    if graph[y+prev[0]][x+prev[1]] != -1:
                        graph[y][x] += graph[y+prev[0]][x+prev[1]]
    answer = graph[n-1][m-1] % 1000000007
    return answer