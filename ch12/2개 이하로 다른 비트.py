#1
# f(x): x보다 크고 x와 비트가 1~2개 다른 수 중 가장 작은 수

def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            binary = bin(num)[2:]
            binary = binary[:-1] + "1"
            answer.append(int(binary, 2))
        else:
            binary = "0" + bin(num)[2:]
            idx = binary.rindex("0")
            binary = binary[0:idx] + "10" + binary[idx+2:]
            answer.append(int(binary, 2))
    return answer