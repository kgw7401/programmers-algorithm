def solution(participant, completion):
    answer = ''
    completion_dict = {}

    for c in completion:
        if completion_dict.get(c):
            completion_dict[c] += 1
        else:
            completion_dict[c] = 1

    for p in participant:
        if not completion_dict.get(p) or completion_dict.get(p) == 0:
            answer = p
            break
        else:
            completion_dict[p] -= 1

    return answer
            