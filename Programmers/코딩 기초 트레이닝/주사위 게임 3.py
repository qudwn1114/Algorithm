def solution(a, b, c, d):
    answer = 0
    arr = [a, b, c, d]
    cnt_dict = {}
    for i in arr:
        if cnt_dict.get(i):
            cnt_dict[i] += 1
        else:
            cnt_dict[i] = 1

    

    sorted_cnt = sorted(cnt_dict.items(), key=lambda x:(-x[1], x[0]))
    a = len(sorted_cnt)

    if a == 1:
        answer = 1111 * sorted_cnt[0][0]
    elif a == 2:
        # 3개 같을때
        if sorted_cnt[0][1] !=  sorted_cnt[1][1]:
            answer = (10 * sorted_cnt[0][0] + sorted_cnt[1][0]) * (10 * sorted_cnt[0][0] + sorted_cnt[1][0])
        else:
            answer = (sorted_cnt[0][0] + sorted_cnt[1][0]) * abs(sorted_cnt[0][0] - sorted_cnt[1][0])
    elif a == 3:
        answer = sorted_cnt[1][0] * sorted_cnt[2][0]
    elif a == 4:
        answer = sorted_cnt[0][0]

    return answer