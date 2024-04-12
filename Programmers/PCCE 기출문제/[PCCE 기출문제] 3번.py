year = int(input())
age_type = input()

if age_type == "Korea": #빈칸1
    answer = 2030 - year + 1 #빈칸2

elif age_type == "Year":
    answer = 2030 - year #빈칸3


print(answer)