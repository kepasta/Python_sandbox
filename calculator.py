def calc(sentence):
    j = 0
    sign = ''
    isign = 0
    sentence = sentence.replace(' ', '')
    i = ''
    for i in sentence:
        if i in '123456789':
            j += 1
        elif i in '+-*/':
            sign = i
            isign = j
            j += 1
        else:
            j += 1
    number1 = 0
    number2 = 0
    k = len(sentence) - 1
    j = 0
    while k >= 0:
        if k == isign:
            j = 0
        elif k > isign:
            number2 += int(sentence[k]) * 10 ** j
            j += 1
        else:
            number1 += int(sentence[k]) * 10 ** j
            j += 1
        k -= 1
    if sign == '+':
        return number1 + number2
    elif sign == '-':
        return number1 - number2
    elif sign == '*':
        return number1 * number2
    elif sign == '/':
        return number1 / number2
    else:
        return 'wtf?'

sentence = input('vvedite stroku: ')
print(calc(sentence))
