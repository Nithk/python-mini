try:   
    a=input("enter the sum")
    res=eval(a)
    print(res)
    while(1):
        try:
            print("Do you want to calculate further with these result Type y/n")
            b=input()
            if b=="y":
                a=input("enter")
                res+=eval(a)
                print(res)
            else:
                break
        except:
            print("Invalidd")
except:
    print("Not a valid ")