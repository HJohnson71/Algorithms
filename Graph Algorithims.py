# Depth first search for wrestler "heel or face" designation: O(V+E)

def designate(V, E):
    Wrestlers = V
    Rivals = E
    graph = {}
    for edge in Rivals:
        wrst1, wrst2 = edge
        if wrst1 not in graph:
            graph[wrst1] = []
        if wrst2 not in graph:
            graph[wrst2] = []
        graph[wrst1].append(wrst2)
        graph[wrst2].append(wrst1)
    faces = []
    heels = []
    groups = {}
    def depthfs(wrestler, group):
        groups[wrestler] = group
        if group == 'face':
            faces.append(wrestler)
        if group == 'heel':
            heels.append(wrestler)
        for k in graph[wrestler]:
            if k in groups:
                if groups[k] == group:
                    return False
            else:
                if not depthfs(k, 'heel' if group == 'face' else 'face'):
                    return False
        return True
    for i in Wrestlers:
        if i not in groups:
            if not depthfs(i, 'face'):
                return None
    return (faces, heels)

#Test:

V = ['The Rock','Steve Austin']
E = [('The Rock','Steve Austin')]
print(designate(V,E))
V = ['The Rock','Steve Austin','Triple H']
E = [('The Rock','Steve Austin'),('The Rock','Triple H'),('Steve Austin','Triple H')]
print(designate(V, E))


# ALien dictionary problem using topological sort: O(nm)

def alienDictionary(dict):
    def build_graph(words):
        graph = {}
        in_degree = {}
        for k in words:
            for i in k:
                in_degree[i] = 0
        for i in range(1, len(words)):
            prev_word = words[i - 1]
            curr_word = words[i]
            min_length = min(len(prev_word), len(curr_word))
            for j in range(min_length):
                if prev_word[j] != curr_word[j]:
                    if prev_word[j] not in graph:
                        graph[prev_word[j]] = []
                    graph[prev_word[j]].append(curr_word[j])
                    in_degree[curr_word[j]] = in_degree.get(curr_word[j], 0) + 1
                    break
        return graph, in_degree
    graph, in_degree = build_graph(dict)
    result = []
    queue = []
    for k in in_degree:
        if in_degree[k] == 0:
            queue.append(k)
    while queue:
        k = queue.pop(0)
        result.append(k)
        if k in graph:
            for neighbor in graph[k]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    return result

# Test:

print(alienDictionary(['bbc','ba','cb','a']))
print(alienDictionary(['baa','abcd','abca','cab','cad']))