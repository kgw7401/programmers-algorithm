#1.
# dp의 핵심! 이전의 값을 이용한다
# 따라서 N이 2번 쓰일 때는 1번 쓰인 것을 이용한다.
# 5 -> 55, 5+5, 5-5, 5/5, 5*5 -> 555, 55+5, 55/5...

def solution(N, number):
    dp = [set() for i in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    dp[i].add(k+l)
                    dp[i].add(k*l)
                    dp[i].add(k-l)
                    if l != 0 and k != 0:
                        dp[i].add(k//l)
        if number in dp[i]:
            return i
    return -1
