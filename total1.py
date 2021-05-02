def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count
print(total(3,3,56,6,7,76,5675,77,counterattackes=3, goals=28))
