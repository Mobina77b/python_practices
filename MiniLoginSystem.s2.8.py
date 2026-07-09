password=input("password: ")
username=input("username: ")
if username!="mobina":
    print("invalid username")
elif username=="mobina"and password!="123":
    print("username is correct but password is wrong")
else:
    if password=="123"and username=="mobina":
       role=input("what's your role ? ")
       if role=="administrater":
           print("administrater panel")
       else:
           print("user dashbord")
