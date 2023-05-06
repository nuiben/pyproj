#ABC string

init = 0
while init != 1:
    print('Give me a string to check for an Alphabetical Succession of Letters: ')
    s = input()
    abcstring = ''
    longABC = ''
    currentindex = 0
    for char in s:
        if(abcstring == '' or char >= abcstring[(len(abcstring) - 1):(len(abcstring))]):
            abcstring += char
            if ((currentindex + 1) == len(s) and (len(abcstring) > len(longABC))):
                longABC = abcstring
                #if abcstring is not last index of string
        elif(char <= abcstring[(len(abcstring) - 1):(len(abcstring))]):
            if(len(abcstring) > len(longABC)):
                longABC = abcstring
            abcstring = char
        currentindex += 1
    print('Longest substring in alphabetical order is: ' + longABC)
    print('Enter 1 to exit')
    init = int(input())
