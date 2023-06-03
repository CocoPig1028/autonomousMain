#모빌리티에서 방향 추출할 함수
def directionCalc(pathValue, direction):
    for i in range(len(pathValue)):
        if pathValue[i] == 1:
            direction.append('R')
        elif pathValue[i] == -1:
            direction.append('L')
        elif pathValue[i] == 5:
            direction.append('D')
        elif pathValue[i] == -5:
            direction.append('U')
    
    print(direction)

#모빌리티에서 GCS로 넘겨줄 행동 추출
def actionCalc(action, direction, path_length,):
    action.append('GO')
    
    for i in range(path_length - 2):
        a = direction[i]
        b = direction[i+1]
        if (a == 'D'):
            if(b == 'D'):
                action.append('GO')
            elif(b == 'R'):
                action.append('TL')
            elif(b == 'L'):
                action.append('TR')
            else:
                action.append("ER")

        elif (a == 'U'):
            if(b == 'U'):
                action.append('GO')
            elif(b == 'L'):
                action.append('TL')
            elif(b == 'R'):
                action.append('TR')
            else:
                action.append("ER")

        elif (a == 'R'):
            if(b == 'R'):
                action.append('GO')
            elif(b == 'U'):
                action.append('TL')
            elif(b == 'D'):
                action.append('TR')
            else:
                action.append("ER")

        elif (a == 'L'):
            if(b == 'L'):
                action.append('GO')
            elif(b == 'D'):
                action.append('TL')
            elif(b == 'U'):
                action.append('TR')
            else:
                action.append("ER")

    # action.append('GO')
    print(action)

#모빌리티가 사용할 행동
def mobilActionCalc(mAction, direction, path_length,):
    mAction.append('GO')
    mAction.append('GO')

    for i in range(path_length - 2):
        a = direction[i]
        b = direction[i+1]

        # mAction.append('GO')
        if (a == 'D'):
            if(b == 'D'):
                mAction.append('GO')
            elif(b == 'R'):
                mAction.append('TL')
                mAction.append('GO')
            elif(b == 'L'):
                mAction.append('TR')
                mAction.append('GO')
            else:
                mAction.append("ER")

        elif (a == 'U'):
            if(b == 'U'):
                mAction.append('GO')
            elif(b == 'L'):
                mAction.append('TL')
                mAction.append('GO')
            elif(b == 'R'):
                mAction.append('TR')
                mAction.append('GO')
            else:
                mAction.append("ER")

        elif (a == 'R'):
            if(b == 'R'):
                mAction.append('GO')
            elif(b == 'U'):
                mAction.append('TL')
                mAction.append('GO')
            elif(b == 'D'):
                mAction.append('TR')
                mAction.append('GO')
            else:
                mAction.append("ER")

        elif (a == 'L'):
            if(b == 'L'):
                mAction.append('GO')
            elif(b == 'D'):
                mAction.append('TL')
                mAction.append('GO')
            elif(b == 'U'):
                mAction.append('TR')
                mAction.append('GO')
            else:
                mAction.append("ER")
        mAction.append('GO')

    print(mAction)