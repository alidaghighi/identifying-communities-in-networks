from DS import LinkedList
import time
import sort_methods

# read a text file as a list of lines
# find the last line, change to a file you have
A = time.time()
fileHandle = open('test4.txt', "r")
lineList = fileHandle.readlines()
fileHandle.close()
for i in range(len(lineList)):
    lineList[i] = lineList[i].split('\t')


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


edges = [[0 for i in range(3)] for i in range(len(lineList))]
for i in range(len(lineList)):
    edges[i][0], edges[i][1] = lineList[i][0], lineList[i][1]
matrix = [[0 for i in range(3)] for i in range(len(lineList))]
for i in range(len(lineList)):
    matrix[i][0], matrix[i][1] = lineList[i][0], lineList[i][1]
k = []
degree = 0
start = 1
for i in range(0, len(edges)):
    if edges[i][0] is start:
        degree += 1
    else:
        start = edges[i][0]
        k.append(degree)
        degree = 1
k.append(degree)

def cycle_matrix(row):
    z = 0
    for v in graph[edges[row][0] - 1][1]:
        if v in graph[edges[row][1] - 1][1]:
            z += 1
    return z


# for member in range(len(edges)):
#     Cij = 0
#     Zij = cycle_matrix(member)
#     try:
#         Cij = Zij/(min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1))
#     except:
#         if k[edges[member][0] - 1] - 1 == 0:
#             Cij = 10 ** 7
#     edges[member][2] = Cij

"""
i = len(graph) - 1
while i is not -1:
    child = LinkedList()
    graph_linkedList.__add__(graph[i])
    graph_linkedList.add__child(child)
    j = len(graph[i][1]) - 1
    while j is not -1:
        child.__add__(graph[i][1][j])
        j -= 1
    i -= 1
print(graph_linkedList.head.child.head.data)
k = []
degree = 0
start = 1
for i in range(0, len(edges)):
    if edges[i][0] is start:
        degree += 1
    else:
        start = edges[i][0]
        k.append(degree)
        degree = 1
k.append(degree)


def cycle_matrix(row):
    z = 0
    for v in graph[edges[row][0] - 1][1]:
        if v in graph[edges[row][1] - 1][1]:
            z += 1
    return z


for member in range(len(edges)):
    Cij = 0
    Zij = cycle_matrix(member)
    try:
        Cij = Zij/(min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1))
    except:
        if k[edges[member][0] - 1] - 1 == 0:
            Cij = 10 ** 7
    edges[member][2] = Cij
"""

"""
def dfs(Graph, Start):
    Visited, stack = list(), [Start]
    while stack:
        vertex = stack.pop()
        if vertex not in Visited:
            Visited.append(vertex)
            for i in Visited:
                stack.extend(Graph[vertex - 1].remove(i))
    return Visited



def dfs(graph,start):
    path = []
    stack = [start]
    while stack != []:
        v = stack.pop()
        if v not in path:
            path.append(v)
        for w in reversed(graph[v - 1]):
            if w not in path:
                stack.append(w)
    return path
"""


def dfs(Graph, Start):
    Visited = []
    stack = [Start]
    Visited.append(stack[-1])
    while stack != []:
        for w in Graph[stack[-1] - 1][1]:
            if w not in Visited:
                stack.append(w)
                Visited.append(w)
            else:
                for w in Graph[stack[-1] - 1][1]:
                    if w not in Visited:
                        stack.append(w)
                        Visited.append(w)
        stack.pop()
    return Visited


def insertionsort(A):
    #we start loop at second element (index 1) since the first item is already sorted
    for j in range(1,len(A)):
        key = A[j][2] #The next item we are going to insert into the sorted section of the array

        i = j-1 #the last item we are going to compare to
        #now we keep moving the key back as long as it is smaller than the last item in the array
        while (i > -1) and key < A[i][2]: #if i == -1 means that this key belongs at the start
            A[i+1]=A[i] #move the last object compared one step ahead to make room for key
            i=i-1 #observe the next item for next time.
        #okay i is not greater than key means key belongs at i+1
        A[i+1] = key
    return A


start_time = time.time()


if True:#_input[2] in 'Quick' and len(_input) == 3:
    visited = dfs(graph, 1)
    while len(visited) == len(graph):
        for member in range(len(edges)):
            Cij = 0
            Zij = cycle_matrix(member)
            if min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1) != 0:
                Cij = Zij / (min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1))
            else:
                Cij = 10 ** 7
            edges[member][2] = Cij
        sort_methods.bubble_sort(edges)
        tmp1 = edges.pop(0)
        tmp2 = edges.pop(0)
        tmp1[2] = int(tmp1[2])
        tmp2[2] = int(tmp2[2])
        print(tmp1)
        print(matrix[7])
        matrix.remove(tmp1)
        matrix.remove(tmp2)
        k[tmp1[0] - 1] -= 1
        k[tmp1[1] - 1] -= 1
        graph[tmp1[0] - 1][1].remove(tmp1[1])
        graph[tmp1[1] - 1][1].remove(tmp1[0])
        visited = dfs(graph, 1)
    print(edges)
    end_time = time.time()
    print(graph)
    print(end_time - start_time)
"""
visited = dfs(graph, 1)

while len(visited) != len(graph):
    for member in range(len(edges)):
        Cij = 0
        Zij = cycle_matrix(member)
        if (min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1)) != 0:
            Cij = Zij / (min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1))
        else:
            Cij = 100000000

        edges[member][2] = Cij

    sort_methods.quick_sort(edges, 0, len(edges) - 1)
    edges.reverse()
    tmp1 = edges.pop(len(edges) - 1)
    tmp = []
    tmp.append(tmp1[0])
    tmp.append(tmp1[1])
    tmp.append(0)
    matrix.remove(tmp)
    k[tmp1[0] - 1] -= 1
    k[tmp1[1] - 1] -= 1
    graph[tmp1[0] - 1][1].remove(tmp1[1])
    graph[tmp1[1] - 1][1].remove(tmp1[0])
    visited = dfs(graph, 1)

print('edges:' + '\n')
print(edges)
print('graph:' +'\n')
print(graph)
"""