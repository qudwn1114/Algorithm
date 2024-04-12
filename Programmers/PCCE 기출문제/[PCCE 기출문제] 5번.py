def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            north -= 1 #빈칸1
        elif i == "E" :
            east += 1 #빈칸2
        elif i == "W": #빈칸3
            east -= 1 #빈칸4

    return [east, north]