hex_data = input("hex: ")
data = bytes.fromhex(hex_data)
for key in range(256):
    result = []

    for byte in data:
        result.append(byte ^ key)

    decrypted = bytes(result)
    print(key, decrypted)