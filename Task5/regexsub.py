for _ in range(int(input())):
    i = input()
    
    while ' && ' in i or ' || ' in i:
        i = i.replace(" && ", " and ").replace(" || ", " or ")
    
    print(i)
