str = input()
for i in str:
    if i.lower() == i:
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")