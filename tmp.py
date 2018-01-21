fileHandle = open('test0.txt', "r")
lineList = fileHandle.readlines()
fileHandle.close()
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



def dfs(Graph, Start):
    Visited = [Start]
    stack = []
    for i in range(0,len(Graph[Start-1][1])):
        stack.append(Graph[Start - 1][1][i])
    while stack != []:
        tmp = stack.pop()
        if tmp not in Visited:
            Visited.append(tmp)
            for i in range(0, len(Graph[tmp - 1][1])):
                stack.append(Graph[tmp - 1][1][i])

    return Visited
v = dfs(graph, 1)
# print(v)
if len(v) == len(graph):
    print("FUCK Yeah!")
