rulower = (ord("а"), ord("я"))
ruupper = (ord("А"), ord("Я"))
code_pages = [rulower, ruupper]

def code_len(codes):
    return codes[1] - codes[0] +1


def in_code_pages(a, cp):
    return ord(a) >= cp[0] and ord(a) <= cp[1]


def select_codes(a):
    for cp in code_pages:
        if in_code_pages(a, cp):
            return cp
    return None

def alpha_cipher(alpha, key, codes):
    if codes is None:
        return alpha
    key %= code_len(codes)
    return chr((ord(alpha) + key) % codes[1])


def cipher1(text, key):
    cipher_text = ""
    for a in text:
        codes = select_codes(a)
        cipher_text += alpha_cipher(a, key, codes)
    return cipher_text



def cipher(text, key):
    ru_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    ru_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    len_ru = len(ru_upper)
    idx = 0
    cipher_text = ""
    for i in range(len(text)):
        if text[i] in ru_upper:
            idx = ru_upper.index(text[i]) + key
            idx = idx % len_ru
            cipher_text += ru_upper[idx]
        elif text[i] in ru_lower:
            idx = ru_lower.index(text[i]) + key
            idx = idx % len_ru
            cipher_text += ru_lower[idx]
        else:
            cipher_text += text[i]
    return cipher_text

text = input("Введите текст для шифрования: ")
key = int(input("Введите ключ: "))
print(cipher1(text, key))


# ru_lower = set("абвгдежзийклмнопрстуфхцчшщъыьэюя")
# print(ru_lower)

# print(ord("а"))
# print(ord("я"))
# print(ord("А"))
# print(ord("Я"))

# print(alpha_cipher("б", 2, rulower))
# print(alpha_cipher("б", 32, rulower))

