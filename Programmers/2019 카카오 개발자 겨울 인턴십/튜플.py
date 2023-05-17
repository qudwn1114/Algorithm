def solution(s):
    answer = []
    # 양끝 { } 제거
    s = s[1:len(s)-1]
    count = s.count("{")

    # answer 리스트 초기화
    answer = [0] * count

    s = s.replace("{", "")
    s = s.replace("}", "")
    # 숫자만 리스트화
    s = list(map(int, s.split(",")))

    # 중복제거
    set_list = list(set(s))
    for i in set_list:
        answer[count-s.count(i)] = i
    return answer