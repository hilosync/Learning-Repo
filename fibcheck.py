x = 0
correctcheck = 0

def fibCheck(x):
    firstX = 0
    secondX = 1
    if x == 0:
        return 0
    if x == 1:
        return 1
    while x > 1:
        thirdX = firstX + secondX
        firstX = secondX
        secondX = thirdX
        x -= 1
    return thirdX

while x < 100000:
    fx = fibCheck(x)
    fx1 = fibCheck(x+1)
    if fx * fx1 == prod:
        print(fx, fx1, "True")
        correctcheck = 1
        break
    if fx * fx1 > prod:
        break
    x += 1

if correctcheck == 0:
    print(fx, fx1, "False")
