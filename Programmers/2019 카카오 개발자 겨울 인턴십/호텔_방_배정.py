def solution(k, room_number):
    answer = []
    # key: 방, value: 다음 방
    room_dict = dict()

    for room in room_number:
        next_room = room_dict.get(room)
        if next_room:
            # 업데이트 해야할 리스트
            update_list = [room]
            # 다음방 비어있을때까지..
            while True:
                temp = next_room
                next_room = room_dict.get(temp)
                
                if not next_room:
                    answer.append(temp)
                    room_dict[temp] = temp + 1
                    for i in update_list:
                        room_dict[i] = temp+1
                    break
                update_list.append(temp)    
        else:
            room_dict[room] = room + 1
            answer.append(room)
    return answer

# k=10
# room_number=[1,3,4,1,3,1]

# print(solution(k=k, room_number=room_number))