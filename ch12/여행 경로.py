#1
# 주어진 항공권은 모두 사용
# 항상 ICN에서 출발
# 가능한 경로가 2개 이상이라면 알파벳 순서로
### 방문하는 공항 경로 배열 ###

from collections import defaultdict

def dfs(graph, path, visit):
    if path:
        to = path[-1]
        if graph[to]:
            path.append(graph[to].pop(0))
        else:
            visit.append(path.pop())
        dfs(graph, path, visit)
    return visit[::-1]

def solution(tickets):
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)
    for key in graph.keys():
        graph[key].sort()

    answer = dfs(graph, ["ICN"], [])
    return answer
