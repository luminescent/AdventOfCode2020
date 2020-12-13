# from itertools import quantify

with open("day_2.input", "r") as reader:
    lines = reader.readlines()


def parse_line(line):
    parts = line.split()
    first, second = [int(x) for x in parts[0].split('-')]
    letter = parts[1][:-1]
    word = parts[2]
    return first, second, letter, word


def verify_password(min_letters, max_letters, letter, word):
    occurrences = word.count(letter)
    return (min_letters <= occurrences) and (occurrences <= max_letters)


def verify_password2(first, second, letter, word):
    first -= 1
    second -= 1
    return (word[first] == letter and word[second] != letter) \
           or (word[first] != letter and word[second] == letter)


def verify_line(line, verifier):
    min_letters, max_letters, letter, word = parse_line(line)
    return verifier(min_letters, max_letters, letter, word)


print(sum([verify_line(line, verify_password) for line in lines]))
print(sum([verify_line(line, verify_password2) for line in lines]))

