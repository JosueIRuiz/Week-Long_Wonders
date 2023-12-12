import Ending_Selection


def write_file():
    Ending_Selection.read_file()
    Ending_Selection.char_1()
    Ending_Selection.char_2()
    Ending_Selection.char_3()
    Ending_Selection.char_4()
    Ending_Selection.char_5()
    Ending_Selection.char_6()
    Ending_Selection.char_7()
    Ending_Selection.char_8()
    Ending_Selection.char_9()
    Ending_Selection.char_10()
    Ending_Selection.char_11()
    Ending_Selection.char_12()
    Ending_Selection.char_13()
    Ending_Selection.char_14()
    Ending_Selection.char_15()
    Ending_Selection.char_16()
    Ending_Selection.char_17()
    Ending_Selection.char_18()
    Ending_Selection.char_19()
    Ending_Selection.char_20()
    Ending_Selection.char_21()
    Ending_Selection.e.close()


e = open('Endings.txt', 'r')


def read_file():
    global c
    fc = e.read()
    c = fc.split('\n')


r = open('Right.txt', 'a')
w = open('Wrong.txt', 'a')


def answer_number():
    if c[0] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[1] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[2] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[3] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[4] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[5] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[6] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[7] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[8] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[9] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[10] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[11] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[12] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[13] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[14] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[15] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[16] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[17] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[18] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[19] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    if c[20] == 'right':
        r.write('r\n')
    else:
        w.write('w\n')

    r.close()
    w.close()


g = open('Ending_Selec.txt', 'a')


def end():
    r = open('Right.txt', 'r')
    rc = r.readlines()
    lrc = len(rc)
    r.close()

    w = open('Wrong.txt', 'r')
    wc = w.readlines()
    lwc = len(wc)
    w.close()

    if lrc > lwc:
        g.write('G')
        g.close()
    else:
        g.write('B')
        g.close()
