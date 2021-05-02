def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count
print(total(10, 3, 4, 4, vegtables=23, fruits=100))
