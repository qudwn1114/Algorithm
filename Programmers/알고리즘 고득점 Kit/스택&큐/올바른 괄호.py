def solution(s):
    s_list = []
    for i in s:
        if i == ")":
            if s_list:
                s_list.pop()
            else:
                return False
        else:
            s_list.append(i)
    if s_list:
        return False
    return True