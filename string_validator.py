
if __name__ == '__main__':
    alphanumeric = False
    alphabetic = False
    digits = False
    lower = False
    upper = False
    s = input()
# if at least one characters is numeric/alpha...etc set variable to True
    for char in s:
        if char.isalnum():
            alphanumeric = True
    for char in s:
        if char.isalpha():
            alphabetic = True
    for char in s:
        if char.isdigit():
            digits = True
    for char in s:
        if char.islower():
            lower = True
    for char in s:
        if char.isupper():
            upper = True
# print variables
    print(alphanumeric)
    print(alphabetic)
    print(digits)
    print(lower)
    print(upper)



