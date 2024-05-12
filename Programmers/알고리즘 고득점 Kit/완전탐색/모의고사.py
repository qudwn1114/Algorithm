def solution(answers):
    answer=[]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_count = 0
    b_count = 0
    c_count = 0
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            a_count += 1
        if answers[i] == b[i%8]:
            b_count += 1
        if answers[i] == c[i%10]:
            c_count += 1
    count_list = [a_count, b_count, c_count]
    max_count = max(count_list)
    for i in range(3):
        if count_list[i] == max_count:
            answer.append(i+1)
            
    return answer