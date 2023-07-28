#1
# 집은 원 모양으로 이루어져 있음
# 붙어있는 집을 연속으로 털면 경보가 울림
# 3 < 집 개수 < 1e6
# 경보가 울리면 안됨
### 도둑이 훔칠 수 있는 돈의 최댓값 ###

#2
# 두 가지 경우
# 1) 한칸 건너 2) 두칸 건너
# 3번째까지만 하면 사이클 돌면 모든 경우의 수 나옴
# 재귀 이용

# 나름 발상 자체는 괜찮았는데 너무 깊게 생각했다

def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = dp1[1] = money[0]

    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    answer = max(max(dp1), max(dp2))
    return answer