f = open('Decisions.txt', 'r')
e = open('Endings.txt', 'a')


def read_file():
    global c
    fc = f.read()
    c = fc.split('\n')


def char_1():
    if c[0] == 'A':
        e.write('right\n')
    elif c[0] == 'I':
        e.write('wrong\n')
    else:
        e.write('wrong\n')


def char_2():
    if c[1] == 'I':
        e.write('right\n')
    elif c[1] == 'A':
        e.write('wrong\n')
    else:
        e.write('wrong\n')


def char_3():
    if c[2] == 'A':
        e.write('wrong\n')
    elif c[2] == 'I':
        e.write('wrong\n')
    else:
        e.write('right\n')


def char_4():
    if c[3] == 'I':
        e.write('right\n')
    elif c[3] == 'A':
        e.write('wrong\n')
    else:
        e.write('wrong\n')


def char_5():
    if c[4] == 'A':
        e.write('wrong\n')
    elif c[4] == 'I':
        e.write('wrong\n')
    else:
        e.write('right\n')


def char_6():
    if c[5] == 'A':
        e.write('right\n')
    elif c[5] == 'I':
        e.write('wrong\n')
    else:
        e.write('wrong\n')


def char_7():
    if c[6] == 'A':
        e.write('right\n')
    elif c[6] == 'I':
        e.write('wrong\n')
    else:
        e.write('wrong\n')


def char_8():
    if c[7] == 'A':
        e.write('wrong\n')
    elif c[7] == 'I':
        e.write('right\n')
    else:
        e.write('wrong\n')


def char_9():
    if c[8] == 'A':
        e.write('wrong\n')
    elif c[8] == 'I':
        e.write('wrong\n')
    else:
        e.write('right\n')


def char_10():
    if c[9] == 'A':
        e.write('wrong\n')
    elif c[9] == 'I':
        e.write('wrong\n')
    else:
        e.write('right\n')


def char_11():
    if c[10] == 'A':
        e.write('right\n')
    elif c[10] == 'I':
        e.write('wrong\n')
    else:
        e.write('wrong\n')


def char_12():
    if c[11] == 'A':
        e.write('wrong\n')
    elif c[11] == 'I':
        e.write('right\n')
    else:
        e.write('wrong\n')


def char_13():
    if c[12] == 'A':
        e.write('wrong\n')
    elif c[12] == 'I':
        e.write('wrong\n')
    else:
        e.write('right\n')


def char_14():
    if c[13] == 'A':
        e.write('right\n')
    elif c[13] == 'I':
        e.write('wrong\n')
    else:
        e.write('wrong\n')


def char_15():
    if c[14] == 'A':
        e.write('wrong\n')
    elif c[14] == 'I':
        e.write('right\n')
    else:
        e.write('wrong\n')


def char_16():
    if c[15] == 'A':
        e.write('wrong\n')
    elif c[15] == 'I':
        e.write('wrong\n')
    else:
        e.write('right\n')


def char_17():
    if c[16] == 'A':
        e.write('right\n')
    elif c[16] == 'I':
        e.write('wrong\n')
    else:
        e.write('wrong\n')


def char_18():
    if c[17] == 'A':
        e.write('wrong\n')
    elif c[17] == 'I':
        e.write('right\n')
    else:
        e.write('wrong\n')


def char_19():
    if c[18] == 'A':
        e.write('right\n')
    elif c[18] == 'I':
        e.write('wrong\n')
    else:
        e.write('wrong\n')


def char_20():
    if c[19] == 'A':
        e.write('wrong\n')
    elif c[19] == 'I':
        e.write('wrong\n')
    else:
        e.write('right\n')


def char_21():
    if c[20] == 'A':
        e.write('wrong\n')
    elif c[20] == 'I':
        e.write('right\n')
    else:
        e.write('wrong\n')
