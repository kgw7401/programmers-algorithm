def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        prev_row = triangle[i-1]
        now_row = triangle[i]
        for j in range(len(now_row)):
            if j == 0:
                now_row[j] += prev_row[j]
            elif j == len(now_row) - 1:
                now_row[j] += prev_row[j-1]
            else:
                now_row[j] += max(prev_row[j-1], prev_row[j])
    answer = max(triangle[-1])
    return answer