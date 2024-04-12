start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before #빈칸1
    month += 1
while money < 100: #빈칸2
    money += after #빈칸3
    month += 1

print(month)