l1 = int(input("number:"))
# print(int(l1/2))

if l1 > 1:
    for i in range(2, int(l1/2)+1):
        if l1%i == 0:
            print("Not prime")
            break
        else:
            print(l1, "is prime")
else:
    print("more than one.")