"""
Main files
"""

print(30 * ' ' + 20 * '*')
print('Type "exit" when you wanted to quit.')
print(30 * ' ' + 20 * '*')
print('Type "help" for allowed commands.')
print(30 * ' ' + 20 * '*')

data = []

while True:
    _input = input('Enter a command: ').split()
    try:
        if len(_input) is 0:
            print('Wrong!\ncheck "help" for more information!')
        elif 'exit' in _input[0]:
            break
        elif 'help' in _input[0]:
            print(30 * ' ' + 40 * '*')
            print('At first you have to set data!')
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
                lineList[i] = lineList[i].split(',')
            for i in range(len(lineList)):
                for j in range(2):
                    lineList[i][j] = int(lineList[i][j])
            graph = [[0 for i in range(2)] for i in range(int(lineList[-1][0]))]

            s = []
            start = 1
            for i in range(0, len(lineList)):
                if lineList[i][0] is start:
                    s.append(lineList[i][1])
                else:
                    start = lineList[i][0]
                    graph[lineList[i - 1][0] - 1][0] = lineList[i - 1][0]
                    graph[lineList[i - 1][0] - 1][1] = s
                    s = []
                    s.append(lineList[i][1])
            graph[-1][0] = lineList[-1][0]
            graph[-1][1] = s

            print("Data set!", '\n', "Graph created!")
        elif _input[1] == 'LinkedList' and data is not None:
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

        elif _input[1] == 'Matrix' and data is not None:
            matrix = [[0 for i in range(3)] for i in range(len(lineList))]
            for i in range(len(lineList)):
                matrix[i][0], matrix[i][1] = lineList[i][0], lineList[i][1]
            lineList.clear()
            k = []
            degree = 0
            start = 1
            for i in range(0, len(matrix)):
                if matrix[i][0] is start:
                    degree += 1
                else:
                    start = matrix[i][0]
                    k.append(degree)
                    degree = 1
            k.append(degree)
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
