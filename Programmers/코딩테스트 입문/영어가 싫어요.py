def solution(numbers):
    answer = ''
    num_dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9 }
    number = ''
    for i in numbers:
        number += i
        if number in num_dict:
            answer += str(num_dict[number])
            number = ''
    answer = int(answer)
    
    return answer