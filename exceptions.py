import complex

def numbers(numbers):
    if len(numbers) >= 2:
        a = numbers[0]
        b = numbers[1]
        while type(a) != float:
            try:
                a = float(a)
            except:
                a = 0
                b = 0
        while type(b) != float:
            try:
                b = float(b)
            except:
                b = 0
                a = 0
    else:
        a = 0
        b = 0
    return a, b

def square_root(numbers):
    a = numbers[0]
    while type(a) != float:
        try:
            a = float(a)
        except:
            a = 0
    return a

def complex_num(numbers):
    if len(numbers) >= 4:
        a1 = numbers[0]
        a2 = numbers[1]
        b1 = numbers[2]
        b2 = numbers[3]
        while type(a1) != float and type(a2) != float and type(b1) != float and type(b2) != float:
            try:
                a1 = float(a1)
                a2 = float(a2)
                b1 = float(b1)
                b2 = float(b2)
            except:
                a1 = 0
                a2 = 0
                b1 = 0
                b2 = 0
    else:
        a1 = 0
        a2 = 0
        b1 = 0
        b2 = 0
    if a1 != 0 and a2 != 0 and b1 != 0 and b2 != 0:
        a = complex.comp(a1, a2)
        b = complex.comp(b1, b2)
    else:
        a = 0
        b = 0
    return a, b

def complex_pow(numbers):
    if len(numbers) >= 3:
        a1 = numbers[0]
        a2 = numbers[1]
        b = numbers[2]
        while type(a1) != float and type(a2) != float and type(b) != float:
            try:
                a1 = float(a1)
                a2 = float(a2)
                b = float(b)
            except:
                a1 = 0
                a2 = 0
                b = 0
    else:
        a1 = 0
        a2 = 0
        b = 0
    if a1 != 0 and a2 != 0 and b != 0:
        a = complex.comp(a1, a2)
    else:
        a = 0
        b = 0
    return a, b

def complex_square(numbers):
    if len(numbers) >= 2:
        a1 = numbers[0]
        a2 = numbers[1]
        while type(a1) != float and type(a2) != float:
            try:
                a1 = float(a1)
                a2 = float(a2)
            except:
                a1 = 0
                a2 = 0
    else:
        a1 = 0
        a2 = 0
    if a1 != 0 and a2 != 0:
        a = complex.comp(a1, a2)
    else:
        a = 0
    return a
