lines = open("list.txt", "r").readlines()

graph = {}

for idx, line in enumerate(lines):
    if idx == 0:
        vertices, edges = line.split()
        vertices = int(vertices)
        for i in range(vertices):
            graph[i+1] = []
    else:
        a, b = line.split()
        a = int(a)
        b = int(b)

        graph[a].append(b)
        graph[b].append(a)

for key in sorted(graph.keys()):
    print(' '.join([str(a) for a in sorted(graph[key])]))
