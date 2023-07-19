# info와 query를 모두 비교한다면 50,000 * 100,000 = 5,000,000,000여서 효율성 테스트를 통과하지 못한다.
# 따라서 이진 탐색을 무조건 이용해야 한다.
# 이진 탐색을 어디에 이용할 것인가?

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []

    # info의 모든 경우의 수를 저장한다.
    people = defaultdict(list)

    for i in info:
        person = i.split()
        score = person.pop()
        people[''.join(person)].append(int(score))

        for count in range(len(person)):
            candidates = list(combinations(person, count))
            for c in candidates:
                people[''.join(c)].append(int(score))

    # 모든 경우의 수에 대한 점수들을 모두 정렬한다.
    for p in people:
        people[p].sort()

    print(people)

    # query 변환 후 info의 모든 값과 비교
    for q in query:
        q = q.replace("and ", "").replace("-", "").split(" ")
        q_score = int(q.pop())
        q_person = "".join(q)

        print(q_person)

        find_scores = people[q_person]
        score_index = bisect_left(find_scores, q_score)
        total = len(find_scores) - score_index
        answer.append(total)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))