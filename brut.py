from sys import argv

frequency = {'ъ': 0.0004,
                'р': 0.0473,
                'д': 0.0298,
                'ш': 0.0073,
                'й': 0.0121,
                'э': 0.0032,
                'ф': 0.0026,
                'е': 0.0845,
                'ь': 0.0174,
                'ы': 0.019,
                'о': 0.1097,
                'л': 0.044,
                'и': 0.0735,
                'к': 0.0349,
                'п': 0.0281,
                'ю': 0.0064,
                'н': 0.067,
                'ч': 0.0144,
                'ж': 0.0094,
                'я': 0.0201,
                'г': 0.017,
                'т': 0.0626,
                'с': 0.0547,
                'б': 0.0159,
                'а': 0.0801,
                'м': 0.0321,
                'у': 0.0262,
                'х': 0.0097,
                'в': 0.0454,
                'з': 0.0165,
                'щ': 0.0036,
                'ё': 0.0004,
                'ц': 0.0048}


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
