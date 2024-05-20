def solution(name):
    name = list(name)
    alphabet = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':12, 'P':11, 'Q':10, 'R':9, 'S':8, 'T':7, 'U':6, 'V':5, 'W':4, 'X':3, 'Y':2, 'Z':1}
    answer = 0
    m = len(name) - 1

    for i in range(len(name)):
        answer += alphabet[name[i]]
        next = i + 1
        while True:
            if next >= len(name) or name[next] != 'A':
                break
            next += 1

        m = min([m, 2 * i + (len(name) - next), (len(name) - next) * 2 +i])

    answer += m
    return answer