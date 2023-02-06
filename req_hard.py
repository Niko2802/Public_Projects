# Вводится строка, которая состоит из английских заглавных и строчных букв и ( и ). Определить правильную самую длинную скобочную последовательнодсть.
# Добавляется { и }, [ и ].


def correct_sequence(s):
    for _ in s:
        s_tmp = s[s.rfind("("):]
        if s_tmp.find(")") != -1:
            s_rep = s[s.rfind("("): s.rfind("(") + s_tmp.find(")") + 1]
            s = s.replace(s_rep, "!"+s_rep[1:-1]+"!")
            l_rep = len(s_rep)
            s_max = ""
            l_max = 0
            if s.rfind("(") != -1 and s.find(")") != -1:
                s_max, l_max = correct_sequence(s)
            if l_max < l_rep:
                l_max = l_rep
                s_max = s_rep
            return s_max, l_max
        else:
            s = s[:s.rfind("(")] + "!" + s[s.rfind("(")+1:]

def cor_seq(s):
    idx_end = s.find(")")
    idx_beg = s.find("(")
    if idx_beg == -1 and idx_end == -1: # Нет скобок
        return s, False
    if idx_beg == -1 and idx_end >= 0: # Нет открывающей, но есть закрывающая
        return s[:idx_end], True
    if idx_end < idx_beg: # Сначала идет закрывающая потом открывающая
        return s[:idx_end], True
    cor_s = cor_seq(s[idx_beg+1:])

    if cor_s[1]:
        temp = "(" + cor_s[0] + ")"
        temp = s[:idx_beg] + temp
        if len(s) == idx_end:
            return temp, True
        # cor_ss = cor_seq(s[idx_end+1:])
        # if cor_ss[1]:
        #     temp += cor_ss[0]
        #     return temp, True
        # if len(temp) >= len(cor_ss[0]):
        #     return temp, True
        # return cor_ss
    if len(s[:idx_beg]) >= len(cor_s[0]):
        return s[:idx_beg], True
    return cor_s


s = "(very (lively) place). (Back used) (to)"
s1 = "very (Back used (lively) place)."

print(cor_seq(s))
