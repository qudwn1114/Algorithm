def solution(box, n):
    
    l = box[0] // n
    w = box[1] // n
    h = box[2] // n
    answer = l*w*h
    
    return answer