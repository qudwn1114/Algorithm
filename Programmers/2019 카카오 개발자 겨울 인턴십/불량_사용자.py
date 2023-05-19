def solution(user_id, banned_id):
    answer = 0
    arr = []
    for i in banned_id:
        temp = []
        for j in user_id:
            if compare(j, i):
                temp.append(j)
        arr.append(temp)
    answer = count_combination(arr)
    return answer

# 불량사용자 비교 id1:응모자 id, id2: 불량사용자
def compare(id1, id2) -> bool:
    if len(id1) != len(id2):
        return False
    for i in range(len(id1)):
        if id2[i] == '*':
            pass
        else:
            if id1[i] != id2[i]:
                return False
    return True

# 순열 세기
def count_combination(arr) -> int:
    combination = []
    for i in arr:
        if combination:
            copy_c = combination.copy()
            combination = []
            for j in i:    
                for k in copy_c:
                    temp = k.copy()
                    if j not in temp:
                        temp.append(j)
                        temp.sort()
                        if temp not in combination:
                            combination.append(temp)
        else:
            # 초기화
            for j in i:
                temp = []
                temp.append(j)
                combination.append(temp)

    count = len(combination)
    return count

a=["frodo", "fradi", "crodo", "abc123", "frodoc"]
b=["fr*d*", "*rodo", "******", "******"]
print(solution(a,b))