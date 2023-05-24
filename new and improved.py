text = open("list.txt", "r").readlines()

vertices = text[0].split()[0]
edges = text[0][1]
graph = {}
text.pop(0)

for x in range(int(vertices)):
    graph[x+1] = []

for x in range(len(text)):
    a = int(text[x].split()[0])
    b = int(text[x].split()[1])

    graph[a].append(b)
    graph[b].append(a)

for x in graph:
    graph[x].sort()

for daHOOD in graph.values():
    print(*daHOOD)

