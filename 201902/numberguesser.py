low_numb = 0
high_numb = 100
print('Please think of a number between 0 and 100!')
while True:
    x = (high_numb + low_numb)//2
    print('Is your secret number ' + str(x) + ' ?')
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if a == 'c':
        print('Game over. Your secret number was:', str(x))
        break
    elif a == 'l':
        low_numb = x
    elif a == 'h':
        high_numb = x
    else:
        print('Sorry, I did not understand your input.')
