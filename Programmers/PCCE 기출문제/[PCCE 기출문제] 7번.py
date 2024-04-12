def func1(humidity, val_set):
    if humidity < val_set:
        return 3 #빈칸1
    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else: #빈칸2
        return 5 #빈칸3
    
        


def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0 #빈칸4


def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity) #빈칸5

    elif mode_type == "target":
        answer = func1(humidity, val_set) #빈칸6

    elif mode_type == "minimum":
        answer = func3(humidity, val_set) #빈칸7

    return answer