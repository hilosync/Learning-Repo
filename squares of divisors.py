def list_squared(m, n):
    if m+n == 2:
        return [1, 1]
    else:
        finalList = []
        def squarelist(list1):
            return[i**2 for i in list1]
        Divisors = []
        for x in range(m,n):
            for y in range(1,x+1):
                if x % y == 0:
                    Divisors.append(y)
                if y == x:
                    checker = sum(squarelist(Divisors))
                    RootCheck = checker ** 0.5
                    if RootCheck % 1 == 0.0:
                        finalList.append([x, checker])
            Divisors = []
        return finalList
