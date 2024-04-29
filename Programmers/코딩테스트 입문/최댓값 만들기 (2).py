def solution(numbers):
    numbers.sort()
    if numbers[0] * numbers[1] < numbers[-2] * numbers[-1]:
        answer = numbers[-2] * numbers[-1]
    else:
        answer = numbers[0] * numbers[1]
    return answer