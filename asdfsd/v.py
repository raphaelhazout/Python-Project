pw=input("Put your Password: ")
for i in range(5):
    pw2 = input("Put your Verfection Password: ")
    if pw==pw2:
        print("great success")
        break
    print("invalid password")
else:
    print("5 times faild")

