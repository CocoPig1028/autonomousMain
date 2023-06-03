def nodeInOut(nodeCount, path):
    comeOut = path[nodeCount]
    comeIn = path[nodeCount + 1]

    print("출발 노드: ", comeOut, "향하는 노드: ", comeIn)