s = "3453245 345 38394 249"
n = [int(x) for x in s.split(" ")]
print(n)

l = [1, 3, 4, 7, 11, 2, 18, 20, 2]
print(all([l.count(x)==1 for x in l]))
