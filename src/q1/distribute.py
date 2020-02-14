from imports import *


def distribute(xTrain , yTrain):
    # so I have the two arrays and I literally have to pick and place them into 10 different arrays
    dx = []
    dy = []


    for i in range(0 , len(xTrain), 450):
        lx = []
        ly = []
        for a in range(i , i+450):
            lx.append(float(xTrain[a]))
            ly.append(float(yTrain[a]))
        lx = np.asarray(lx)
        ly = np.asarray(ly)
        dx.append(lx)
        dy.append(ly)

    return dx, dy

