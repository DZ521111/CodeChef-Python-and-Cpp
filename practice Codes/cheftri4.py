'''
Author : Dhruv B Kakadiya

'''

# import libraries
import sys
import math
import copy

class YesException(BaseException) :
    # no content
    pass

class NoException(BaseException):
    # no content
    pass

def getInput(num) :
    if(num) :
        inputArr = input().split()
        if len(inputArr) != num :
            print(f"The length is {len(inputArr)} not same as asked for {num}")
            sys.exit(0)
        for i in range(0, len(inputArr)) :
            inputArr[i] = int(inputArr[i])
        return inputArr
    elif  num == 0 :
        return int(input())
    elif  num == None :
        return input()

def getValue(arg) :
    myVal0 = 0 + arg[0] + arg[1] + arg[2]
    myVal1 = 0 - arg[0] + arg[1] + arg[2]
    myVal2 = 0 + arg[0] - arg[1] + arg[2]
    myVal3 = 0 + arg[0] + arg[1] - arg[2]
    if myVal0 < 0 :
        raise NoException()
    if myVal1 < 0 :
        raise NoException()
    if myVal2 < 0 :
        raise NoException()
    if myVal3 < 0 :
        raise NoException()
    return myVal0 * myVal1 * myVal2 * myVal3

def getMulValue(arg0, arg1) :
    myVal0 = arg0 * arg1
    myVal1 = int(math.sqrt(myVal0))
    if myVal0 == myVal1 * myVal1 :
        return myVal1
    else :
        raise NoException()

def getFinalValue(arg0) :
    myLen = len(arg0)
    if myLen == 1 :
        return arg0[0]
    elif myLen == 2 :
        return arg0[0] + arg0[1] + 2 * getMulValue(arg0[0], arg0[1])
    elif myLen == 3 :
        return arg0[0] + arg0[1] + arg0[2] + 2 * getMulValue(arg0[0], arg0[1]) + 2 * getMulValue(arg0[0] , arg0[2]) + 2 * getMulValue(arg0[1], arg0[2])
    elif myLen == 4 :
        return arg0[0] + arg0[1] + arg0[2] + arg0[3] + 2 * getMulValue(arg0[0], arg0[1]) + 2 * getMulValue(arg0[0] , arg0[2]) + 2 * getMulValue(arg0[1], arg0[2]) + 2 * getMulValue(arg0[0], arg0[3]) + 2 * getMulValue(arg0[1], arg0[3]) + 2 * getMulValue(arg0[2], arg0[3])

def specialCheck_1(grp, targetValue) :
    for i in range(0, 3):
        for j in range(0, 3) :
            for k in range(0, 3) :
                tSides = [ grp[0][i], grp[1][j], grp[2][k] ]
                try :
                    if getValue(tSides) != targetValue :
                        continue
                except NoException :
                    continue
                remSides = [ [], [], [] ]
                ttList = [0, 1, 2]
                ttList.remove(i)
                remSides[0].append(grp[0][ttList[0]])
                remSides[0].append(grp[0][ttList[1]])
                ttList = [0, 1, 2]
                ttList.remove(j)
                remSides[1].append(grp[1][ttList[0]])
                remSides[1].append(grp[1][ttList[1]])
                ttList = [0, 1, 2]
                ttList.remove(k)
                remSides[2].append(grp[2][ttList[0]])
                remSides[2].append(grp[2][ttList[1]])
                if remSides[0][0] == remSides[1][0] and remSides[1][1] == remSides[2][0] and remSides[0][1] == remSides[2][1] :
                    return tSides
                if remSides[0][0] == remSides[1][1] and remSides[1][0] == remSides[2][0] and remSides[0][1] == remSides[2][1] :
                    return tSides
                if remSides[0][1] == remSides[1][0] and remSides[1][1] == remSides[2][0] and remSides[0][0] == remSides[2][1] :
                    return tSides
                if remSides[0][1] == remSides[1][1] and remSides[1][0] == remSides[2][0] and remSides[0][0] == remSides[2][1] :
                    return tSides
                if remSides[0][0] == remSides[1][0] and remSides[1][1] == remSides[2][1] and remSides[0][1] == remSides[2][0] :
                    return tSides
                if remSides[0][0] == remSides[1][1] and remSides[1][0] == remSides[2][1] and remSides[0][1] == remSides[2][0] :
                    return tSides
                if remSides[0][1] == remSides[1][0] and remSides[1][1] == remSides[2][1] and remSides[0][0] == remSides[2][0] :
                    return tSides
                if remSides[0][1] == remSides[1][1] and remSides[1][0] == remSides[2][1] and remSides[0][0] == remSides[2][0] :
                    return tSides
    return []


def specialCheck_0(grp, targetValue) :
    for i in range(0, 4) :
        tmpList = [0, 1, 2 ,3]
        tmpList.remove(i)
        for j in range(0, 3) :
            for k in range(0, 3) :
                for l in range(0, 3) :
                    tSides = [ grp[tmpList[0]][j], grp[tmpList[1]][k], grp[tmpList[2]][l] ]
                    try :
                        if getValue(tSides) != targetValue :
                            continue
                    except NoException :
                        continue
                    remSides = [ [], [], [] ]
                    ttList = [ 0, 1, 2]
                    ttList.remove(j)
                    remSides[0].append(grp[tmpList[0]][ttList[0]])
                    remSides[0].append(grp[tmpList[0]][ttList[1]])
                    ttList = [ 0, 1, 2]
                    ttList.remove(k)
                    remSides[1].append(grp[tmpList[1]][ttList[0]])
                    remSides[1].append(grp[tmpList[1]][ttList[1]])
                    ttList = [ 0, 1, 2]
                    ttList.remove(l)
                    remSides[2].append(grp[tmpList[2]][ttList[0]])
                    remSides[2].append(grp[tmpList[2]][ttList[1]])
                    cSides = [ grp[i][0], grp[i][1], grp[i][2] ]
                    cSides.sort()
                    tcSides = [abs(remSides[0][0] - remSides[1][0]), abs(remSides[1][1] - remSides[2][0]), abs(remSides[0][1] - remSides[2][1]) ]
                    tcSides.sort()
                    if tcSides == cSides :
                        raise YesException()
                    tcSides = [abs(remSides[0][0] - remSides[1][1]), abs(remSides[1][0] - remSides[2][0]), abs(remSides[0][1] - remSides[2][1]) ]
                    tcSides.sort()
                    if tcSides == cSides :
                        raise YesException()
                    tcSides = [abs(remSides[0][1] - remSides[1][0]), abs(remSides[1][1] - remSides[2][0]), abs(remSides[0][0] - remSides[2][1]) ]
                    tcSides.sort()
                    if tcSides == cSides :
                        raise YesException()
                    tcSides = [abs(remSides[0][1] - remSides[1][1]), abs(remSides[1][0] - remSides[2][0]), abs(remSides[0][0] - remSides[2][1]) ]
                    tcSides.sort()
                    if tcSides == cSides :
                        raise YesException()
                    tcSides = [abs(remSides[0][0] - remSides[1][0]), abs(remSides[1][1] - remSides[2][1]), abs(remSides[0][1] - remSides[2][0]) ]
                    tcSides.sort()
                    if tcSides == cSides :
                        raise YesException()
                    tcSides = [abs(remSides[0][0] - remSides[1][1]), abs(remSides[1][0] - remSides[2][1]), abs(remSides[0][1] - remSides[2][0]) ]
                    tcSides.sort()
                    if tcSides == cSides :
                        raise YesException()
                    tcSides = [abs(remSides[0][1] - remSides[1][0]), abs(remSides[1][1] - remSides[2][1]), abs(remSides[0][0] - remSides[2][0]) ]
                    tcSides.sort()
                    if tcSides == cSides :
                        raise YesException()
                    tcSides = [abs(remSides[0][1] - remSides[1][1]), abs(remSides[1][0] - remSides[2][1]), abs(remSides[0][0] - remSides[2][0]) ]
                    tcSides.sort()
                    if tcSides == cSides :
                        raise YesException()




def specialCheck_3(grp, targetValue) :
    adjencies = []
    for i in range(0, 4) :
        adjencies.append([])
        for j in range(0, 3) :
            adjencies[i].append([])
            for l in range(0, 4) :
                if i == l :
                    continue
                for k in range(0, 3) :
                    if grp[i][j] == grp[l][k] :
                        adjencies[i][j].append((l, k))
                        break
    for i in range(0, 4) :
        for mmm in [ (0 , 1, 2), (0, 2, 1), (1, 2, 0) ] :
            for firstSel in adjencies[i][mmm[0]] :
                for secSel in adjencies[i][mmm[1]] :
                    if firstSel[0] != secSel[0] :
                        thSide = grp[i][mmm[2]]
                        tt = [0 ,1 , 2]
                        tt.remove(firstSel[1])
                        ff = [grp[firstSel[0]][tt[0]], grp[firstSel[0]][tt[1]]]
                        tt = [0 ,1 , 2]
                        tt.remove(secSel[1])
                        ss = [grp[secSel[0]][tt[0]], grp[secSel[0]][tt[1]]]
                        ttt = [ (0, 0) , (0 ,1), (1, 0) , (1, 1)]
                        xx = [ 0, 1, 2, 3]
                        xx.remove(i)
                        xx.remove(firstSel[0])
                        xx.remove(secSel[0])
                        yy = [grp[xx[0]][0], grp[xx[0]][1], grp[xx[0]][2] ]
                        for x in ttt :
                            mySum0 = ff[x[0]] + ss[x[1]]
                            for y in yy :
                                if y == mySum0 :
                                    yyy = [grp[xx[0]][0], grp[xx[0]][1], grp[xx[0]][2] ]
                                    yyy.remove(y)
                                    fff = copy.deepcopy(ff)
                                    fff.remove(ff[x[0]])
                                    sss = copy.deepcopy(ss)
                                    sss.remove(ss[x[1]])
                                    if getValue([thSide, yyy[0]+fff[0], yyy[1]+sss[0]]) == targetValue :
                                        raise YesException()
                                    if getValue([thSide, yyy[1]+fff[0], yyy[0]+sss[0]]) == targetValue :
                                        raise YesException()


def specialCheck(grp, targetValue) :
    adjencies = []
    for i in range(0, 4) :
        adjencies.append([])
        for j in range(0, 3) :
            adjencies[i].append([])
            for l in range(0, 4) :
                if i == l :
                    continue
                for k in range(0, 3) :
                    if grp[i][j] == grp[l][k] :
                        adjencies[i][j].append((l, k))
                        break

    for i in range(0, 4) :
        for firstSel in adjencies[i][0] :
            for secSel in adjencies[i][1] :
                for thirdSel in adjencies[i][2] :
                    if firstSel[0] != secSel[0] and firstSel[0] != thirdSel[0] and secSel[0] != thirdSel[0]:
                        myEdgeComb = [ [], [], [] ]
                        myTempList = [0, 1, 2]
                        myTempList.remove(firstSel[1])
                        for x in myTempList :
                            myEdgeComb[0].append(grp[firstSel[0]][x])
                        myTempList = [0, 1, 2]
                        myTempList.remove(secSel[1])
                        for x in myTempList :
                            myEdgeComb[1].append(grp[secSel[0]][x])
                        myTempList = [0, 1, 2]
                        myTempList.remove(thirdSel[1])
                        for x in myTempList :
                            myEdgeComb[2].append(grp[thirdSel[0]][x])
                        try :
                            if getValue([myEdgeComb[0][0] + myEdgeComb[1][0], myEdgeComb[1][1] + myEdgeComb[2][0], myEdgeComb[0][1] + myEdgeComb[2][1]]) == targetValue :
                                raise YesException()
                        except NoException :
                            pass
                        try :
                            if getValue([myEdgeComb[0][0] + myEdgeComb[1][1], myEdgeComb[1][0] + myEdgeComb[2][0], myEdgeComb[0][1] + myEdgeComb[2][1]]) == targetValue :
                                raise YesException()
                        except NoException :
                            pass
                        try :
                            if getValue([myEdgeComb[0][1] + myEdgeComb[1][0], myEdgeComb[1][1] + myEdgeComb[2][0], myEdgeComb[0][0] + myEdgeComb[2][1]]) == targetValue :
                                raise YesException()
                        except NoException :
                            pass
                        try :
                            if getValue([myEdgeComb[0][1] + myEdgeComb[1][1], myEdgeComb[1][0] + myEdgeComb[2][0], myEdgeComb[0][0] + myEdgeComb[2][1]]) == targetValue :
                                raise YesException()
                        except NoException :
                            pass
                        try :
                            if getValue([myEdgeComb[0][0] + myEdgeComb[1][0], myEdgeComb[1][1] + myEdgeComb[2][1], myEdgeComb[0][1] + myEdgeComb[2][0]]) == targetValue :
                                raise YesException()
                        except NoException :
                            pass
                        try :
                            if getValue([myEdgeComb[0][0] + myEdgeComb[1][1], myEdgeComb[1][0] + myEdgeComb[2][1], myEdgeComb[0][1] + myEdgeComb[2][0]]) == targetValue :
                                raise YesException()
                        except NoException :
                            pass
                        try :
                            if getValue([myEdgeComb[0][1] + myEdgeComb[1][0], myEdgeComb[1][1] + myEdgeComb[2][1], myEdgeComb[0][0] + myEdgeComb[2][0]]) == targetValue :
                                raise YesException()
                        except NoException :
                            pass
                        try :
                            if getValue([myEdgeComb[0][1] + myEdgeComb[1][1], myEdgeComb[1][0] + myEdgeComb[2][1], myEdgeComb[0][0] + myEdgeComb[2][0]]) == targetValue :
                                raise YesException()
                        except NoException :
                            pass

def checkExist(grp, targetValue) :
    edges = []
    mySize = len(grp)
    if mySize == 1 :
        try :
            myVal0 = getValue(grp[0])
            return myVal0 == targetValue
        except NoException :
            return False

    if mySize == 3 :
        if specialCheck_1(grp, targetValue) :
            return True

    for i in range(0, mySize - 1) :
        for j in range(i + 1, mySize) :
            for k in range(0, 3) :
                for l in range(0, 3) :
                    if grp[i][k] == grp[j][l] :
                        edges.append([[i, k], [j, l]])
                        break
    for edge in edges :
        ((t0, s0), (t1, s1)) = edge
        tmpEdgeComp = [ [], [] ]
        myTempList = [0, 1, 2]
        myTempList.remove(s0)
        for x in myTempList :
            tmpEdgeComp[0].append(grp[t0][x])
        myTempList = [0, 1, 2]
        myTempList.remove(s1)
        for x in myTempList :
            tmpEdgeComp[1].append(grp[t1][x])
        tempTargetValue = 0
        try :
            tempTargetValue = getFinalValue([getValue(grp[t0]) , getValue(grp[t1])])
        except NoException :
            continue
        try :
            mTempList = []
            mTempList.append([tmpEdgeComp[0][0]+tmpEdgeComp[1][0], tmpEdgeComp[0][1], tmpEdgeComp[1][1]])
            mTempList.append([tmpEdgeComp[0][0]+tmpEdgeComp[1][1], tmpEdgeComp[0][1], tmpEdgeComp[1][0]])
            mTempList.append([tmpEdgeComp[0][1]+tmpEdgeComp[1][0], tmpEdgeComp[0][0], tmpEdgeComp[1][1]])
            mTempList.append([tmpEdgeComp[0][1]+tmpEdgeComp[1][1], tmpEdgeComp[0][0], tmpEdgeComp[1][0]])
            for tt in mTempList :
                newGrp = []
                newGrp.append(tt)
                if checkExist(newGrp, tempTargetValue) :
                    myGrp = []
                    myGrp.append(tt)
                    for i in range(0, mySize) :
                        if i == t0 :
                            continue
                        elif i == t1 :
                            continue
                        else :
                            myGrp.append(grp[i])
                    if checkExist(myGrp, targetValue) :
                        return True
        except NoException :
            pass
    return False

def specialCheck_2(grp, targetValue):
    for i in range(0, 4) :
        tt = [0, 1, 2, 3]
        tt.remove(i)
        myGrp = [ [], [], [] ]
        for j in range(0, 3) :
            for k in range(0, 3) :
                myGrp[j].append(grp[tt[j]][k])
        try :
            resll = specialCheck_1(myGrp, getFinalValue([getValue(myGrp[0]), getValue(myGrp[1]), getValue(myGrp[2])]))
            if resll :
                nGrp = [ [], [] ]
                nGrp[0].append(resll[0])
                nGrp[0].append(resll[1])
                nGrp[0].append(resll[2])
                nGrp[1].append(grp[i][0])
                nGrp[1].append(grp[i][1])
                nGrp[1].append(grp[i][2])
                if checkExist(nGrp, targetValue) :
                    raise YesException()
            else :
                continue
        except NoException :
            continue

def myTest(grp) :
    try :
        values = []
        for i in range(0, 4) :
            values.append(getValue(grp[i]))
        myTargetValue = getFinalValue(values)
        specialCheck(grp, myTargetValue)
        specialCheck_3(grp, myTargetValue)
        specialCheck_0(grp, myTargetValue)
        specialCheck_2(grp, myTargetValue)
        if checkExist(grp, myTargetValue) :
            raise YesException()
        raise NoException()

    except YesException :
        print("Yes")
    except NoException :
        print("No")

for test in range(0, getInput(0)) :
    grp = []
    grp.append(getInput(3))
    grp.append(getInput(3))
    grp.append(getInput(3))
    grp.append(getInput(3))
    myTest(grp)

