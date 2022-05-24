#vowels

init = 0
while init != 1:
    print('Give me a string to check for vowels: ')
    s = input()
    #vowels = ['a', 'e', 'i', 'o', 'u']
    vowelcount = 0 
    for char in s:
        if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
            vowelcount += 1
    print('Number of vowels: ' + str(vowelcount))
    print('Enter 1 to exit')
    init = int(input())
