#1
# i, j가 연결되어 있으면 1
# 컴퓨터의 개수 n -> 배열 n*n
### 네트워크의 개수 ###

#2
# dfs로 같은 네트워크에 방문한 노드를 같은 수로 표시
# 마지막에 set으로 유니크한 방문 표시 개수 리턴

def dfs(k, graph, visited):
    visited[k] = 1
    for i in range(len(graph[k])):
        if visited[i] == 0 and graph[k][i] == 1:
            dfs(i, graph, visited)

def solution(n, computers):
    visited = [0] * n
    answer = 0

    for i in range(n):
        if visited[i] == 0:
            dfs(i, computers, visited)
            answer += 1

    return answer