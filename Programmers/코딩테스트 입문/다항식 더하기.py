def solution(polynomial):
    arr = polynomial.split(" + ")
    a = 0
    b = 0
    for i in arr:
        if "x" in str(i):
            s = str(i).split("x")[0]
            if s:
                a += int(s)
            else:
                a += 1
        else:
            b += int(i)
    if a > 0 and b > 0:
        if a == 1:
            answer = f"x + {b}"
        else:
            answer = f"{a}x + {b}"
    elif a > 0 and b == 0:
        if a == 1:
            answer = "x"
        else:
            answer = f"{a}x"
    elif a == 0 and b > 0:
        answer = f"{b}"
    return answer