#1
# 147 왼, 369 오, 2580 양
# 2580은 더 가까운 손을 사용하되 거리가 같다면 주손으로 누른다
### LRLLRRR ###

#2
# 현재 손의 위치
# 2580일 때 현재 손의 위치와의 거리 계산
# 각 자판별로 좌표 저장

def solution(numbers, hand):
    answer = []
    left_hand = "*"
    right_hand = "#"

    coord = {}
    for i in range(1, 13):
        coord[i] = ((i-1)//3, (i-1)%3)

    coord["*"] = coord.pop(10)
    coord[0] = coord.pop(11)
    coord["#"] = coord.pop(12)

    for num in numbers:
        if num in [1,4,7]:
            answer.append("L")
            left_hand = num
        elif num in [3,6,9]:
            answer.append("R")
            right_hand = num
        else:
            left_coord = coord[left_hand]
            right_coord = coord[right_hand]
            next_num_coord = coord[num]
            left_dist = abs(left_coord[0] - next_num_coord[0]) + abs(left_coord[1] - next_num_coord[1])
            right_dist = abs(right_coord[0] - next_num_coord[0]) + abs(right_coord[1] - next_num_coord[1])

            if left_dist < right_dist:
                answer.append("L")
                left_hand = num
            elif right_dist < left_dist:
                answer.append("R")
                right_hand = num
            else:
                if hand == "right":
                    answer.append("R")
                    right_hand = num
                else:
                    answer.append("L")
                    left_hand = num
    return "".join(answer)