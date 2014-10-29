class DirectedGraph():
    def __init__(self):
        self.graph = {}
        self.checked = []

    def __str__(self):
        result = ""
        for node in self.graph:
            result += "{} : {}\n".format(node, self.graph[node])
        return result

    def add_edge(self, node_a, node_b):
        if node_b not in self.graph:
            self.graph[node_b] = []
        if node_a in self.graph and node_b not in self.graph[node_a]:
            self.graph[node_a] += [node_b]
        elif node_a not in self.graph:
            self.graph[node_a] = [node_b]

    def get_neighbors_for(self, node_a):
        return self.graph[node_a]

    def path_between(self, node_a, node_b):
        if node_b in self.graph[node_a]:
            return True
        self.checked.append(node_a)
        for node in self.graph[node_a]:
            if node not in self.checked:
                if self.path_between(node, node_b):
                    return True
        return False
