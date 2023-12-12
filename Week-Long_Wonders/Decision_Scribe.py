# Week-Long Wonders
# Josue I Ruiz
# Write the decisions the player makes into a .txt file which will be used to decide ending.


f = open('Decisions.txt', 'a')


def write_immortalize():
    f.write('I\n')


def write_erase():
    f.write('A\n')


def write_remember():
    f.write('P\n')


def close_file():
    f.close()
