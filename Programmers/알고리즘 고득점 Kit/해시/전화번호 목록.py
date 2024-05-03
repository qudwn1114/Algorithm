def solution(phone_book):
    answer = True
    phone_book.sort()
    last_phone = ''
    for i in range(len(phone_book)):
        if last_phone != '':
            l = len(last_phone)
            if last_phone == phone_book[i][:l]:
                return False
        last_phone = phone_book[i]
        
    return answer