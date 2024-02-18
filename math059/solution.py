def decrypt_message():
    with open("math059/cipher.txt", "r", encoding="utf8") as f:
        text = f.read()

    result = []

    text = text.split(",")

    cipher = [text[i::3] for i in range(3)]
    dic = {}
    key = f"{ord('g')}{ord('o')}{ord('d')}"

    # for i in range(3):
    #     for ch in cipher[i]:
    #         dic[ch] = dic.get(ch, 0) + 1
    #     common_ch = sorted(dic.items(), key = lambda x: x[1], reverse=True)[0][0]
    #     key = "".join((key, str(int(common_ch) ^ 32)))

    for i in range(len(text)):
        result_byte = int(text[i]) ^ int(key[i % len(key)])
        result.append(result_byte)

    return sum(result)


print(decrypt_message())
