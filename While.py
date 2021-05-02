number = 23 
running = True
while running:
    guess = int(input('Enter an integer:'))

    if guess == number:
        print('Congratulation, You\'ve earned it')
        running = False
    elif guess < number:
        print('Nope, it\'s a bit higher than that')
    else:
        print('Nope, it\'s a bit lower than that')
else:
    print('+++++++++++++++++++++++++')
    print('_____The game is over____')
    print('+++++++++++++++++++++++++')

print('DONE')
