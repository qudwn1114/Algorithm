def solution(friends, gifts):
    answer = 0
    
    history_dict = dict()
    score_dict = dict()

    # 친구들 선물 표 초기화
    for i in friends:
        for j in friends:
            if i==j:
                history_dict[f'{i} {j}'] = False
            else:
                history_dict[f'{i} {j}'] = 0
    
    # 선물표에 주고받은 현황 기록 추가
    for i in gifts:
        history_dict[f'{i}'] = history_dict[f'{i}'] + 1

    # 선물 지수 dict 초기화
    for i in friends:
        score_dict[f'{i}'] = 0

    # 선물 지수 
    for i in history_dict:
        sender, receiver = i.split(' ')
        x = history_dict[f'{i}']
        # 값이 있을 때만.. 0, False 는 연산 패스
        if x:
            score_dict[f'{sender}'] = score_dict[f'{sender}'] + x
            score_dict[f'{receiver}'] = score_dict[f'{receiver}'] - x
    
    for i in friends:
        next_month_take = 0
        for j in friends:
            if i == j:
                pass
            if history_dict[f'{i} {j}'] > history_dict[f'{j} {i}']:
                next_month_take += 1
            elif history_dict[f'{i} {j}'] == history_dict[f'{j} {i}']:
                if score_dict[f'{i}'] > score_dict[f'{j}']:
                    next_month_take += 1
            else:
                pass
        if next_month_take > answer:
            answer = next_month_take

    return answer

# friends = ["muzi", "ryan", "frodo", "neo"]
# gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

# print(solution(friends=friends, gifts=gifts))