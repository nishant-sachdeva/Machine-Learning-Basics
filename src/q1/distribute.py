import random


def distribute(xTrain ,yTrain):
    dx={}
    dy={}
    numCount={}
    for i in range(0, 10):
        dx["xTrain{0}".format(i)] = []
        dy["yTrain{0}".format(i)] = []
        numCount["count{0}".format(i)]=0
    j=0
    while j<4500:
        arrayVal=random.randint(0, 9)
        if numCount["count{0}".format(arrayVal)]>=450:
            continue
        else:
            dx["xTrain{0}".format(arrayVal)].append(xTrain[j])
            dy["yTrain{0}".format(arrayVal)].append(yTrain[j])
            numCount["count{0}".format(arrayVal)]+=1
            j+=1

    for i in range(0, 10):
        print(numCount["count{0}".format(arrayVal)])

    return dx, dy, numCount