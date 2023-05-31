def goAction():
    print("I'm Going Now")

def leftAction():
    print("Turn Left")

def rightAction():
    print("Turn Right")

def stopAction():
    print("Stop")

def moveMain(mAction):
    for i in range(len(mAction)):
        if(mAction[i] == 'GO'):
            goAction()

        elif(mAction[i] == 'TL'):
            leftAction()

        elif(mAction[i] == 'TR'):
            rightAction()

        else:
            stopAction()