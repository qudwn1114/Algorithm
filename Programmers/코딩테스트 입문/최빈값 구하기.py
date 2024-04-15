def solution(array):
    answer = 0
    a = {}
    for i in array:
        if a.get(f'{i}'):
            a[f'{i}'] += 1
        else:
            a[f'{i}'] = 1
    
    sorted_a = sorted(a, key=lambda x:a[x], reverse=True)
    answer = int(sorted_a[0])
    if len(sorted_a) > 1:
        if a[sorted_a[0]] == a[sorted_a[1]]:
            answer = -1
        
    return answer