def my_strip(s):
    marks = '".,()[]{/}\!?:;-'
    for x in s:
        if x in marks:
            s = s.replace(x, "")
    return s


phrase = input("Введите строку: ")
# s = my_strip(phrase)
s = phrase.translate({ord(x): "" for x in ['"', ',', '.', '(', ')', '[', ']', '{', '/', '}', '\\', '!', '?', ':', ';', '-']})
print(max(s.split(" "), key=len))
