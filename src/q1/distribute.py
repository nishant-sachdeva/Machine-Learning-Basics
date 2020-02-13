from imports import *


def distribute(xTrain , yTrain, xTest, yTest):
    # so I have the two arrays and I literally have to pick and place them into 10 different arrays
    dx = []
    dy = []

    xtest = []
    ytest = []

    for a in range(0, len(xTest)):
        xtest.append([a , xTest[a]])


    for i in range(0 , len(xTrain), 450):
        lx = []
        ly = []
        for a in range(i , i+450):
            lx.append([ int(a-i) , float(xTrain[a]) ])
            ly.append(float(yTrain[a]))
        lx = np.asarray(lx)
        ly = np.asarray(ly)
        dx.append(lx)
        dy.append(ly)

    return dx, dy , xtest , yTest

