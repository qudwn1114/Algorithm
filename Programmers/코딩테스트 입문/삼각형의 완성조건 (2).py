def solution(sides):
    answer = 0
    sides.sort()
    # 가장 긴변이 리스트 포함인 경우
    for i in range(1, sides[1]):
        if i + sides[0] > sides[1]:
            answer += 1
    # 나머지 한변이 긴변일 경우
    for i in range(sides[1], sides[0]+ sides[1]):
        answer += 1
    
    return answer