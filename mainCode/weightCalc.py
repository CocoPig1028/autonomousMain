#GCS
def weightCalc(node, action, path):
    #행동에 따른 노드 가중치 부여
    for i in range(len(action)):
        x = path[i]
        y = x // 5
        z = x % 5

        if(action[i] == 'GO'):
            node[i][y][z] = 4
        elif(action[i] == 'TL' or action[i] == 'TR'):
            node[i][y][z] = 5
        elif(action[i] == 'ER'):
            node[i][y][z] = 10

        print("노드정보: ", path[i], "가중치: ", node[i][y][z])
        print(node[i])