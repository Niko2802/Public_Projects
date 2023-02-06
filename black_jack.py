# Создать колоду 52 карты
# Карта - кортеж из 3 элементов (имя(Т,2,3,...В,Д,К), масть, стоимость)
# Колода - список кортежей

# Перемешать колоду

# Снять верх колоды на случайное количество карт

# Сдать карты

# Добавить карту, добавить карты в колоду

# Добавить печать карты и печать списка карт
import random


def deck_get():
    values = ('Т', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'В', 'Д', 'К')
    suites = ('♠', '♣', '♦', '♥')
    cost = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    deck = []
    for suit in suites:
        for i in range(len(values)):
            deck.append((values[i], suit, cost[i]))
    return deck


def deck_shuffle(deck):
    return random.shuffle(deck)


def deck_shift(deck):
    deck_shift = random.randint(1, len(deck))
    return deck[deck_shift:] + deck[:deck_shift]


def deck_get_num_card(deck, num_card = 1):
    deck_num_card = []
    for i in range(num_card):
        deck_num_card.append(deck.pop(0))
    return deck_num_card


def pretty_print(deck):
    n, s, v = deck[0]
    st = n + s
    for n, s, v in deck[1:]:
        st += ", " + n + s
    print(st)


def add_cards(deck, new_deck):
    deck.extend(new_deck)
    return deck


def calc_bj_count(deck):
    summ = 0
    t_count = 0
    for i in deck:
        summ += i[2]
        if i[0] == "Т":
            t_count += 1
    if summ > 21:
        summ -= t_count * 10
    return summ

# Взять еще одну? Да/Нет  y
# 2♠, 5♣, Т♦
# 18
# Взять еще одну? Да/Нет  y
# 2♠, 5♣, Т♦, 3♠
# 21
# Взять еще одну? Да/Нет  y
# 2♠, 5♣, Т♦, 3♠, 6♦
# 17




def player_turn(deck):
    answer_yes = {"y", "yes", "да", "д"}
    answer_no = {"n", "no", "нет", "н"}
    player_deck = deck_get_num_card(deck, 2)
    print("Ваши карты:")
    pretty_print(player_deck)
    player_count = calc_bj_count(player_deck)
    while player_count <= 21:
        print("Ваши очки:")
        print(player_count)
        ret = input("Взять еще одну? Да/Нет  ")
        if ret.lower() in answer_no:
            return player_count
        if ret.lower() in answer_yes:
            player_deck = add_cards(player_deck, deck_get_num_card(deck))
            print("Ваши карты:")
            pretty_print(player_deck)
            player_count = calc_bj_count(player_deck)
        else:
            print("Ошибка ввода")
    return player_count

def comp_turn(deck):
    # Нужно рассчитать вероятность выпадения нужной карты и соответсвенно брать или не брать карту. 
    # P=n/N P-вероятность выпадения, n-количество заданных чисел, N-количество всех возможных чисел.
    comp_deck = deck_get_num_card(deck, 2)
    print("Карты соперника:")
    pretty_print(comp_deck)
    comp_count = calc_bj_count(comp_deck)
    while comp_count <= 21:
        print("Очки соперника:")
        print(comp_count)
        p_percent = round((21 - comp_count) / len(deck), 2) * 100
        if p_percent > 20:
            comp_deck = add_cards(comp_deck, deck_get_num_card(deck))
            print("Карты соперника:")
            pretty_print(comp_deck)
            comp_count = calc_bj_count(comp_deck)
        else:
            return comp_count
    return comp_count


def bj_turn(deck):
    plyaer_count = player_turn(deck)
    if plyaer_count > 21:
        print(f"{plyaer_count} - перебор. Победил компьютер!")
        return
    comp_count = comp_turn(deck)
    if comp_count > 21:
        print(f"{comp_count} - перебор. Победил игрок!")
        return
    if plyaer_count > comp_count:
        print(f"Игрок победил! Со счетом {plyaer_count} - {comp_count}")
    elif plyaer_count < comp_count:
        print(f"Компьютер победил! Со счетом {comp_count} - {plyaer_count}")
    else:
        print(f"Ничья! {plyaer_count} - {comp_count}")




deck = deck_get()
deck_shuffle(deck)

bj_turn(deck)
# deck_player = deck_get_num_card(deck, 2)
# pretty_print(deck_player)
# print(calc_bj_count(deck_player))

# Написать com_turn
# Вывод победных очков
# Учет туза как 1, если туз уже есть и перебор
# Облегчить ввод пользователю
