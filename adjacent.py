text = open("list.txt", "r").readlines()

n = text[0].split(" ")[0]  # number of points
m = text[0].split(" ")[1]  # number of lines

dict1 = {}  # Left Column as Key
dict2 = {}  # Right Column as Key

values = []
key = []
values2 = []
key2 = []
for x in range(1, int(m) + 1):
    values.append(int(text[x].split(" ")[1]))
    values2.append(int(text[x].split(" ")[0]))
    key.append(int(text[x].split(" ")[0]))
    key2.append(int(text[x].split(" ")[1]))

tester = []
for x in range(1, len(key)):
    for y in range(len(key)):
        if x == key[y]:
            tester.append(values[y])
            dict1[x] = tester
    tester = []

tester2 = []
for x in range(1, len(key)):
    for y in range(len(key)):
        if x == key2[y]:
            tester2.append(values2[y])
            dict2[x] = tester2
    tester2 = []

result = {}

# Add values from dict1
for key, value in dict1.items():
    result[key] = value

# Add values from dict2 and combine with existing values if key exists
for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

# Sort by Keys
myKeys = list(result.keys())
myKeys.sort()
sorted_dict = {i: result[i] for i in myKeys}
result = sorted_dict

# Sort by Value
for key, value in result.items():
    sorted_dict[key] = sorted(value)

for daHOOD in result.values():
    print(*daHOOD)