def number_to_words(n):
    basic = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
     6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    tens = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
         50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
         80: 'восемьдесят', 90: 'девяносто'}
    tensto = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    hun = {100: 'сто', 200: 'двести', 300: 'триста',
           400: 'четыреста', 500: 'пятьсот', 600: 'шестьсот',
           700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот'}
    n1 = n % 10
    n2 = n - n1
    n3 = n % 100
    n4 = n - n3
    n5 = n3 - n1
    if n < 10:
        return basic.get(n)
    elif 10 < n < 20:
        return tensto.get(n)
    elif n >= 10 and n in tens:
        return tens.get(n)
    elif n >= 100 and n in hun:
        return hun.get(n)
    else:
        if 100< n < 1000:
            if n1 == 0:
                return hun.get(n4) + ' ' + tens.get(n5)
            if 10 < n3 < 20:
                return hun.get(n4) + ' ' + tensto.get(n3)
            return hun.get(n4)+ ' ' + tens.get(n5) + ' ' + basic.get(n1)
        else:
             return tens.get(n2) + ' ' + basic.get(n1)

def math (o):
    number1 = float(input(" введите первое число:"))
    number2 = float(input(" введите второе число:"))
    counter = 0
    if o == "+":
        counter = number1 + number2
        print(" сумма чисел равна: " + number_to_words(counter))

    if o == "-":
        counter = number1 - number2
        print(" разность чисел равна: " + number_to_words(counter))

    if o == "*":
        counter = number1 * number2
        print(" произведение чисел равно: " + number_to_words(counter))

    if o == "/":
        counter = number1 / number2
        print(" частное из чисел: " + number_to_words(counter))

    if o == "%":
        counter = number1 % number2
        print(" остаток от деления: " + number_to_words(counter))

    if o == "**":
        counter = number1 ** number2
        print(" результат возведения числа ", number1, "в степень", number2, ": " +number_to_words(counter))