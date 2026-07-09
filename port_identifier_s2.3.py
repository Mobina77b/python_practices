port=int(input("port: "))
if port==22:
    print("SSH")
elif port==80:
    print("HTTP")
elif port==443:
    print("HTTPS")
elif port==21:
    print("FTP")
else:
    print("unknown port")