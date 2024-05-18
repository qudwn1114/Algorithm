import itertools

def solution(word):
    dictionary = []
    arr = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        temp = list(itertools.product(arr, repeat=i))
        for j in temp:
            dictionary.append(''.join(j))
    dictionary.sort()
    answer = dictionary.index(word) + 1
    
    return answer