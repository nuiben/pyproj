#bobs

init = 0
while init != 1:
    print('Give me a string to check for Bobs: ')
    s = input()
    bobcount = 0
    bobspeller = ''
    for char in s:
        if (char == 'b' and bobspeller == ''):
            bobspeller += char
        elif (char == 'o' and bobspeller == 'b'):
            bobspeller += char
        elif (char == 'o' and bobspeller == 'bo'):
            bobspeller = ''
        elif (char == 'b' and bobspeller == 'bo'):
            bobspeller += char
            bobcount += 1
            bobspeller = 'b'            
        elif (char != 'b' and char != 'o'):
            bobspeller = ''
    print('Number of Bobs: ' + str(bobcount))
    print('Enter 1 to exit')
    init = int(input())
