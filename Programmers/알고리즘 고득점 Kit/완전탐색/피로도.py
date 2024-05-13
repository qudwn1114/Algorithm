permutation_list = []

def solution(k, dungeons):
    answer = -1
    idx_list = list(range(len(dungeons)))
    permutation([], idx_list)
    for i in permutation_list:
        point = k
        count = 0
        for j in i:
            if point >= dungeons[j][0]:
                point -= dungeons[j][1]
                count += 1
            else:
                if count > answer:
                    answer = count
                break
        if count > answer:
            answer = count
    
    return answer

def permutation(arr1, arr2):
    if arr2:
        for i in range(len(arr2)):
            x = arr1.copy()
            x.append(arr2[i])
            temp = arr2.copy()
            temp.pop(i)
            if temp:
                permutation(x, temp)
            else:
                permutation_list.append(x)

print(solution(80, [[80,20],[50,40],[30,10]]))