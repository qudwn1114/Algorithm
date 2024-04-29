def solution(spell, dic):
    answer = 2
    spell_len = len(spell)
    for i in dic:
        if len(i) == spell_len:
            c = 1
            for j in spell:
                if j not in i:
                    c = 0
            if c == 1:
                answer = 1
                break
    return answer