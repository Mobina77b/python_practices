password=input("password:")
uppercase=False
lowercase=False
digit=False
special=False
length=0
for character in password:
    if "A"<=character<="Z":
        uppercase=True
    elif "a"<=character<="z":
        lowercase=True
    elif "0"<=character<="9":
         digit=True
    else:
        special=True
    length+=1
if uppercase and lowercase and digit and special and length>=8:
    print("strong")
else:
    print("weak")