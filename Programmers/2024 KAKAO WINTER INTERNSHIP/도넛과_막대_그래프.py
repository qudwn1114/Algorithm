def solution(edges):
    answer = []

    edge_in_out_dict = dict()

    for a, b in edges:
        if not edge_in_out_dict.get(a):
            edge_in_out_dict[a] = [0, 0]
        if not edge_in_out_dict.get(b):
            edge_in_out_dict[b] = [0, 0]
        
        edge_in_out_dict[a][0] += 1
        edge_in_out_dict[b][1] += 1
    
    answer = [0, 0, 0, 0]

    for k, v in edge_in_out_dict.items():
        # k점기준 v[0] : out     v[1] : in
        
        # 생성한 정점 찾기
        if v[0] >= 2 and v[1] == 0:    
            answer[0] = k
        
        # 8자 그래프 찾기
        elif v[0] >= 2 and v[1] >= 2:
            answer[3] += 1
        # 막대그래프 찾기 
        elif v[0] == 0 and v[1] > 0:
            answer[2] += 1
    
    answer[1] = edge_in_out_dict[answer[0]][0] - answer[2] - answer[3]

    return answer


# edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

# print(solution(edges=edges))