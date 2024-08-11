l=0
n=0
while n==0:
    password=input("\n\t\tEnter your password:")
    if len(password)>=7:
        if not password.isalnum():
            for i in password:
                if i.isupper():
                    l+=1
                    if l>=1:
                        print("\t\tvaild password")
                        n=1
                        break
                else:
                    print("\t\tinvalid password")
                    break
        else:
            print("\t\tinvalid password")
    else:
        print("\t\tinvalid password")
