import re


operators = ['-', '*', '/', '+']


def is_correct(sequence):
    eq = sequence.split('=')
    true_result = eval(eq[0])
    if true_result == int(eq[1]):
        return True
    return False


def is_valid(sequence):
    result = re.match(r"^\d[+*\-/]\d=\d", sequence)
    if result:
        return True
    return False


sequence = input()

if is_valid(sequence) and not is_correct(sequence):
    print('NO')
elif not is_valid(sequence):
    print('ERROR')
elif is_valid(sequence) and is_correct(sequence):
    print('YES')
