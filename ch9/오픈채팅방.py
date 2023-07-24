def solution(record):
    answer = []

    id_to_nickname_dict = {}

    for r in record:
        data = r.split()

        if len(data) == 2:
            word = data[0]
            user_id = data[1]
            answer.append([word, user_id])
        else:
            word = data[0]
            user_id = data[1]
            nickname = data[2]
            if word == "Change":
                id_to_nickname_dict[user_id] = nickname
            else:
                id_to_nickname_dict[user_id] = nickname
                answer.append([word, user_id])

    for i in range(len(answer)):
        word = answer[i][0]
        user_id = answer[i][1]

        if word == "Enter":
            nickname = id_to_nickname_dict[user_id]
            answer[i] = f"{nickname}님이 들어왔습니다."
        else:
            nickname = id_to_nickname_dict[user_id]
            answer[i] = f"{nickname}님이 나갔습니다."
    return answer