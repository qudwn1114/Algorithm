permutation_set = set()

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    permutation('', numbers)
    for i in list(permutation_set):
        if i > 1:
            if is_prime(i):
                answer += 1
            
    return answer

def permutation(s, arr):
    if arr:
        for i in range(len(arr)):
            new = s + arr[i]
            permutation_set.add(int(new))
            temp = arr.copy()
            temp.pop(i)
            permutation(new, temp)
    else:
        return

def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True