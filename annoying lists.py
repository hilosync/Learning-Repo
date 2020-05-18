def alphabet_position(text):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = [x for x in alp]

    textList = [x for x in text]
    for x in range(0, len(textList)):
        if len(textList) > x:
            if (textList[x]).lower() in alphabet:
                print(x)
                textList[x] = str(alphabet.index(textList[x].lower()) + 1)
            else:
                textList[x] = 'x'
    textList = ' '.join(i for i in map(str, textList) if i != 'x')
    return textList
