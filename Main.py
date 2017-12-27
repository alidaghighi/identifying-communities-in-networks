"""
Main files
"""
from DS import LinkedList


print(30 * ' ' + 20 * '*')
print('Type "exit" when you wanted to quit.')
print(30 * ' ' + 20 * '*')
print('Type "help" for allowed commands.')
print(30 * ' ' + 20 * '*')

while True:
    _input = input('Enter a command: ').split()
    try:
        if len(_input) is 0:
            print('Wrong!\ncheck "help" for more information!')
        elif 'exit' in _input[0]:
            break
        elif 'help' in _input[0]:
            print(30 * ' ' + 20 * '*')
            print('RUN command: \n')
            print('>>> RUN LinkedList Quick ')
            print('>>> RUN LinkedList Quick ')
            print('>>> RUN LinkedList Quick ')
            print('>>> RUN LinkedList Quick ')
            print('>>> RUN LinkedList Quick ')
            print('>>> RUN LinkedList Quick ')
            print('>>> RUN LinkedList Quick ')
            print('>>> RUN LinkedList Quick ')

        elif _input[0] == 'add':
            print("")
            if _input[1] in 'service':
                print("")
            elif _input[1] in 'subservice':
                print("")
            elif _input[1] in 'agency':
                print("")
            elif _input[1] in 'offer':
                print("")
            else:
                print('Wrong!\ncheck "help" for more information!')

        else:
            print('Wrong!\ncheck "help" for more information!')
        print(30 * ' ' + 20 * '*')
    except:
        print('Wrong!\ncheck "help" for more information!')