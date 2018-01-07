"""
Main files
"""

print(30 * ' ' + 20 * '*')
print('Type "exit" when you wanted to quit.')
print(30 * ' ' + 20 * '*')
print('Type "help" for allowed commands.')
print(30 * ' ' + 20 * '*')

graph = {}

while True:
    _input = input('Enter a command: ').split()
    try:
        if len(_input) is 0:
            print('Wrong!\ncheck "help" for more information!')
        elif 'exit' in _input[0]:
            break
        elif 'help' in _input[0]:
            print(30 * ' ' + 40 * '*')
            print('run commands:')
            print('    >>> run LinkedList Quick ')
            print('    >>> run LinkedList Insertion ')
            print('    >>> run LinkedList Merge ')
            print('    >>> run LinkedList Bubble ')
            print('    >>> run LinkedList Optimum Insertion <your input number> ')
            print('    >>> run LinkedList Optimum Bubble <your input number> ')
            print('    >>> run Matrix Quick ')
            print('    >>> run Matrix Insertion  ')
            print('    >>> run Matrix Merge ')
            print('    >>> run Matrix Bubble ')
            print('    >>> run Matrix Optimum Insertion <your input number> ')
            print('    >>> run Matrix Optimum Bubble <your input number> ')
            print(30 * ' ' + 40 * '*')
            print('input command:')
            print('    >>> input <name of your test case file>')

        elif _input[0] in 'input':
            data = open(_input[1], 'r')
            lineList = data.readlines()
            for i in range(len(lineList)):
                lineList[i] = lineList[i].split('\t')
            for i in range(len(lineList)):
                last = lineList[i]
                s = ''
                s1 = last[1]
                for j in range(0, len(last[1]) - 1):
                    s += s1[j]
                last[1] = s
                lineList[i] = last
            D = {}
            s = []
            for i in range(0, int(lineList[-1][0])):
                if lineList[i + 1][0] == lineList[i][0]:
                    for j in [1]:
                        if lineList[i][j] not in s:
                            s.append(lineList[i][j])
                if lineList[i + 1][0] != lineList[i][0]:
                    if lineList[i][j] not in s:
                        s.append(lineList[i][j])
                    D[lineList[i][0]] = s
                    s = []

            print("Data set!", '\n', "Graph created!")
        elif _input[1] == 'LinkedList':
            if _input[2] in 'Quick' and len(_input) == 3:
                print("DO2")
            elif _input[2] in 'Insertion' and len(_input) == 3:
                print("DO3")
            elif _input[2] in 'Merge' and len(_input) == 3:
                print("DO4")
            elif _input[2] in 'Bubble' and len(_input) == 3:
                print("DO5")
            elif _input[2] in 'Optimum':
                if _input[3] in 'Insertion' and len(_input) == 4:
                    print("DO6")
                elif _input[3] in 'Bubble' and len(_input) == 4:
                    print("DO7")
                else:
                    print('Wrong!\ncheck "help" for more information!')

        elif _input[1] == 'Matrix':
            if _input[2] in 'Quick' and len(_input) == 3:
                print("DO22")
            elif _input[2] in 'Insertion' and len(_input) == 3:
                print("DO32")
            elif _input[2] in 'Merge' and len(_input) == 3:
                print("DO42")
            elif _input[2] in 'Bubble' and len(_input) == 3:
                print("DO52")
            elif _input[2] in 'Optimum':
                if _input[3] in 'Insertion' and len(_input) == 4:
                    print("DO62")
                elif _input[3] in 'Bubble' and len(_input) == 4:
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
