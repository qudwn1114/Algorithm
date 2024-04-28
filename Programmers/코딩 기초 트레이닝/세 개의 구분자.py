def solution(myStr):
    answer = []
    a = ''
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            if a != '':
                answer.append(a)
                a = ''
        else:
            a += i
    # 마지막 값 추가
    if a != '':
        answer.append(a)
    if not answer:
        answer = ["EMPTY"]
        
    return answer