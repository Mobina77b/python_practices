hex_data1 = input("hex1: ")
hex_data2 = input("hex2: ")
byt1 = bytes.fromhex(hex_data1)
byt2 = bytes.fromhex(hex_data2)
result = []
for i in range(len(byt1)):
    result.append(byt1[i] ^ byt2[i])
b = bytes(result)
print(b.hex())