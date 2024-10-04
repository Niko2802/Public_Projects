def declension_minutes(num):
    if num % 10 == 1 and num % 100 != 11: 
        return "минута"
    elif 2 <= num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
        return "минуты"
    else:
        return "минут"
    
print(declension_minutes(3))
print(declension_minutes(11))
print(declension_minutes(21))
print(declension_minutes(13))
print(declension_minutes(14))
