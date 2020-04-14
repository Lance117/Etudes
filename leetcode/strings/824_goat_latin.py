def toGoatLatin(S):
    w_lst, vowels = S.split(), list('aeiou')
    for i, w in enumerate(w_lst):
        if w[0].lower() not in vowels:
            w_lst[i] = w[1:] + w[0]
        w_lst[i] += ('ma' + 'a' * (i + 1))
    return ' '.join(w_lst)