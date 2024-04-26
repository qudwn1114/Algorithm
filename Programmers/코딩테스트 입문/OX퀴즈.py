def solution(quiz):
    answer = []
    for i in quiz:
        arr = i.split(" ")
        x = arr[0]
        op = arr[1]
        y = arr[2]
        z = arr[4]
        result = "X"
        if op == '+':
            if int(x) + int(y) == int(z):
                result = "O"
        elif op == '-':
            if int(x) - int(y) == int(z):
                result = "O"
        answer.append(result)
    return answer