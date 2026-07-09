website=input("website: ")
secure=website.startswith("https")
if secure:
    print("secure website")
else:
    print("not secure")