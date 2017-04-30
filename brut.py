from sys import argv

frequency = {'ъ': 4,
                'р': 473,
                'д': 298,
                'ш': 73,
                'й': 121,
                'э': 32,
                'ф': 26,
                'е': 845,
                'ь': 174,
                'ы': 190,
                'о': 1097,
                'л': 440,
                'и': 735,
                'к': 349,
                'п': 281,
                'ю': 64,
                'н': 670,
                'ч': 144,
                'ж': 94,
                'я': 201,
                'г': 170,
                'т': 626,
                'с': 547,
                'б': 159,
                'а': 801,
                'м': 321,
                'у': 262,
                'х': 97,
                'в': 454,
                'з': 165,
                'щ': 36,
                'ё': 4,
                'ц': 48}


alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
Alph = str([i.upper() for i in alph])


def char_shift(char, shift):
    global alph, Alph
    char_ord = alph.find(char)
    if char_ord != -1:
        char_ord = (char_ord + shift) % len(alph)
        return alph[char_ord]
    char_ord = Alph.find(char)
    if char_ord == -1:
        return char
    char_ord = (char_ord + shift) % len(Alph)
    return Alph[char_ord]


def text_shift(text, shift):
    return ''.join([char_shift(i, shift) for i in text])


def make_counting(text):
    global alph
    chars_frequency = dict()
    for i in alph:
        chars_frequency[i] = 0
    for i in text:
        i = i.lower()
        if i in chars_frequency:
            chars_frequency[i] += 1
    return chars_frequency


def shift_counting(counting, shift):
    new_counting = dict()
    for i in counting:
        new_counting[char_shift(i, shift)] = counting[i]
    return new_counting


def calc_differ(counting):
    global frequency
    x = 0
    for i in counting:
        x += frequency[i] * counting[i]
    return x


def brut(text):
    shifts = 33 * [0]
    current_counting = make_counting(text)
    for i in range(33):
        shifts[i] = (calc_differ(shift_counting(current_counting, i)), i)
    maxx = max(shifts)
    return maxx[1]


def main():
    s = input()
    shift = brut(s)
    print(text_shift(s, shift))


main()
