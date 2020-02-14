from imports import *


def distribute(xTrain , yTrain):
    # so I have the two arrays and I literally have to pick and place them into 10 different arrays
    dx = []
    dy = []

    # what I want it to have a list of all x's and all y's just the way I have had it by n\

    for a in range(1, len(xTrain)+1):
        print(a)  

    # for i in range(0 , len(xTrain), 450):
    #     lx = []
    #     ly = []
    #     for a in range(i , i+450):
    #         lx.append(float(xTrain[a]))
    #         ly.append(float(yTrain[a]))
    #     lx = np.asarray(lx)
    #     ly = np.asarray(ly)
    #     dx.append(lx)
    #     dy.append(ly)

    return dx, dy

