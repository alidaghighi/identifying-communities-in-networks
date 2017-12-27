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
            print('RUN command:')
            print('>>> RUN LinkedList Quick ')
            print('>>> RUN LinkedList Insertion ')
            print('>>> RUN LinkedList Merge ')
            print('>>> RUN LinkedList Bubble ')
            print('>>> RUN LinkedList Optimum Insertion N ')
            print('>>> RUN LinkedList Optimum Bubble N ')
            print('>>> RUN Matrix Quick ')
            print('>>> RUN Matrix Insertion  ')
            print('>>> RUN Matrix Merge ')
            print('>>> RUN Matrix Bubble ')
            print('>>> RUN Matrix Optimum Insertion N ')
            print('>>> RUN Matrix Optimum Bubble N ')

        elif _input[1] == 'LinkedList':
            print("DO1")
            if _input[2] in 'Quick':
                print("DO2")
            elif _input[2] in 'Insertion':
                print("DO3")
            elif _input[2] in 'Merge':
                print("DO4")
            elif _input[2] in 'Bubble':
                print("DO5")
            elif _input[2] in 'Optimum':
                if _input[3] in 'Insertion':
                    print("DO6")
                elif _input[3] in 'Bubble':
                    print("DO7")
                else:
                    print('Wrong!\ncheck "help" for more information!')

        elif _input[1] == 'Matrix':
            print("DO12")
            if _input[2] in 'Quick':
                print("DO22")
            elif _input[2] in 'Insertion':
                print("DO32")
            elif _input[2] in 'Merge':
                print("DO42")
            elif _input[2] in 'Bubble':
                print("DO52")
            elif _input[2] in 'Optimum':
                if _input[3] in 'Insertion':
                    print("DO62")
                elif _input[3] in 'Bubble':
                    print("DO72")
                else:
                    print('Wrong!\ncheck "help" for more information!')

            else:
                print('Wrong!\ncheck "help" for more information!')
        else:
            print('Wrong!\ncheck "help" for more information!')
        print(30 * ' ' + 20 * '*')
    except:
        print('Wrong!\ncheck "help" for more information!')
