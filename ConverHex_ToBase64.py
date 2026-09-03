import base64

hex_data=input("hex: ")
bytes_data=bytes.fromhex(hex_data)
result=base64.b64encode(bytes_data).decode()
print(result)