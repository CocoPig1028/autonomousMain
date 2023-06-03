import pathExtraction #경로 추출 함수
import pathCalc #행동 추출 함수
import move #이동 함수
import nodeTrans #현재 노드 및 향하는 노드를 구하는 함수
import time #timeSleep을 위한 함수

gcsGraph = {
        1 : {6 : 0},
        2 : {7 : 0},
        3 : {8 : 0},
        5 : {6 : 0},
        6 : {1 : 0, 5 : 0, 7 : 4, 11 : 0},
        7 : {2 : 0, 6 : 0, 8 : 0, 12 : 0},
        8 : {3 : 0, 7 : 0, 9 : 0, 13 : 0},
        9 : {8 : 0},
        10 : {11 : 0},
        11 : {6 : 0, 10 : 0, 12 : 0, 16 : 0},
        12 : {7 : 0, 11 : 0, 13 : 0, 17 : 0},
        13 : {8 : 0, 12 :0, 14 : 0, 18 : 0},
        14 : {13 : 0},
        15 : {16 : 0},
        16 : {11 : 0, 15 : 0, 17 : 0, 21 : 0},
        17 : {12 : 0, 16 : 0, 18 : 0, 22 : 0},
        18 : {13 : 0, 17 : 0, 19 : 0, 23 : 0},
        19 : {18  : 0},
        21 : {16 : 0},
        22 : {19 : 0},
        23 : {18 : 0}
    }

path = []
pathValue = []
direction = []
action = []
mAction = []

option = 0
nodeCount = 0
moveCount = 0
goCount = 0

while True:
    if option == 0:
        print("수신 대기 중")
        #출발지와 도착지를 받는 지점
#------------------------------------------------------출발지, 도착지 수신--------------------------------------------------------
        #아래 부분 지우고 여기에 통신으로 출발지와 도착지를 받는 코드 작성 바람
        print("출발지 입력: ")
        start = int(input())
        print("도착지 입력")
        curr = int(input())

        if start != 0 and curr != 0: #명령을 받는 것을 계속 반복하여 기다릴지 아니면 행동을 할지 선택해주는 조건문
            option = 1
        time.sleep(1)

    else:
        path = pathExtraction.pathExtraction(gcsGraph, start, curr)
        #경로 추출 완료

        path_length = len(path)
        #경로의 길이

        pathValue = [path[i + 1] - path[i] for i in range(path_length - 1)]
        #행동을 추출하기 위한 산술 알고리즘

        pathCalc.directionCalc(pathValue, direction) #좌표를 기준으로 위, 아래, 좌, 우의 움직임 추출
        pathCalc.actionCalc(action, direction, path_length) #direction의 배열을 이용하여 기초 행동 추출
        pathCalc.mobilActionCalc(mAction, direction, path_length) #direction의 배열을 이용하여 모빌리티에서 사용할 행동 추출
        print("행동실행")
        for i in range(len(mAction)): #노드 정보와 행동을 위한 유한(행동 크기)루프
            nodeTrans.nodeInOut(nodeCount, path)
            #현재 노드와 다음 노드를 전송해 줄 함수
            #위의 코드 들어간 후 comeIn, comeOut GCS와 통신 바람

            #아래의 부분은 모빌리티 행동 명령 호출
            if(mAction[moveCount] == 'GO'):
                move.goAction()
                goCount = goCount + 1
                #Go의 갯수를 goCount에 축적

            elif(mAction[moveCount] == 'TL'):
                move.leftAction()

            elif(mAction[moveCount] == 'TR'):
                move.rightAction()

            else:
                move.stopAction()

            print("goCount: ", goCount)

            if (goCount % 2 == 0):
                nodeCount = goCount // 2
                #goCount가 짝수개일 때마다 노드 이동이 이루어짐을 이용하여 nodeCount의 정보 변경)

            # print("nodeCount: ", nodeCount)
            moveCount = moveCount + 1
            #다음 행동을 추출하기 위해 moveCount 증가

            time.sleep(1)
            #단위 시간대로 움직이기

        option = 0
        nodeCount = 0
        moveCount = 0
        #행동이 끝난 후 사용된 변수 0으로 초기화
#-------------------------------------------------------행동이 끝났다는 명령 필요하면 통신 추가 바람----------------------------------------------------------