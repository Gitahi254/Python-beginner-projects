for num in range(1, 101):
    if num % 3 == 0 and  num % 5 == 0:
        print("Oya|Buda")
    elif num % 3 == 0:
        print("Oya")
    elif num % 5 == 0:
        print("Buda")
    elif num % 7 == 0:
        print("Wazi")
    else:
        print(num)
