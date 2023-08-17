#1
# n명의 사람이 줄을 서는 방법은 n!
### 사전순으로 나열했을 때 k번째 ###

#2
# n=3, k=5
# k/(n-1)! -> 몫: 가장 앞자리 수, 나머지: 그 중에서 몇번째인지

from math import factorial

def solution(n, k):
    numbers = list(range(1, n+1))
    answer = []
    k -= 1

    while numbers:
        idx, k = divmod(k, factorial(len(numbers) - 1))
        answer.append(numbers.pop(idx))
    return answer