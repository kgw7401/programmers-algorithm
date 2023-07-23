def solution(clothes):
    answer = 1
    cloth_dict = {}

    for cloth in clothes:
        if cloth[1] in cloth_dict:
            cloth_dict[cloth[1]] += 1
        else:
            cloth_dict[cloth[1]] = 1

    for i in cloth_dict.values():
        answer *= (i + 1)

    return answer - 1