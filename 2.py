# 3x3 
# 27 daktylious mikro-mesaio-megalo
# win game -> orizontia,ka8eta,diagwnia
# h triada kerdizei an:
# 1.exoun to idio mege8os
# 2.mikro->megalo : dhladh einai ths morfhs mikro - messaio - megalo

# ena kapaki mporei na mpei se kapoio allo kapaki ean 

# python i have a list 3x3?
import random
import numpy as np
mylist = [[0,0,0],
          [0,0,0],
          [0,0,0]]

steps = []

cupList = [{'s':9},{'m':9},{'l':9}]
s = list(cupList[0].keys())[0]
m = list(cupList[1].keys())[0]
l = list(cupList[2].keys())[0]
stepWin = []



def checkIfWin(board):
    global s,m,l
    vertical1 = [board[0][0],board[1][0],board[2][0]]
    vertical2 = [board[0][1],board[1][1],board[2][1]]
    vertical3 = [board[0][2],board[1][2],board[2][2]]
    # check horizontal first
    for rowIndex,row in enumerate(board):
        if(row.count(s) == 3):
            return True
        if(row.count(m) == 3):
            return True
        if(row.count(l) == 3):
            return True
    # check vertical
    if(vertical1.count(s) == 3):
        return True
    if(vertical1.count(m) == 3):
        return True    
    if(vertical1.count(l) == 3):
        return True

    if(vertical1[1] == m):
        if((vertical1[0] == s and vertical1[2] == l) or ((vertical1[0] == s and vertical1[2] == l))):
            return True
    if(vertical2[1] == m):
        if((vertical2[0] == s and vertical2[2] == l) or ((vertical2[0] == s and vertical2[2] == l))):
            return True
    if(vertical3[1] == m):
        if((vertical3[0] == s and vertical3[2] == l) or ((vertical3[0] == s and vertical3[2] == l))):
            return True
    
    # check diagonal!!
    diagonal_list = [board[0][0],board[1][1],board[2][2]]
    if(diagonal_list.count(s) == 3):
        return True
    if(diagonal_list.count(m) == 3):
        return True
    if(diagonal_list.count(l) == 3):
        return True
    if(diagonal_list[1] == m):
        if((diagonal_list[0] == s and diagonal_list[2] == l) or ((diagonal_list[0] == s and diagonal_list[2] == l))):
            return True
    return False
    
def makeMove(cupListTemp,board):
    while True:
        cupSizeIndex = random.randint(0,len(cupListTemp) - 1)
        cupSize = list(cupListTemp[cupSizeIndex].keys())[0]
        allowedIndexes = []
        for rowIndex,row in enumerate(board):
            for columnIndex,column in enumerate(row):
                if(cupSize == s):
                    if(column == 0):
                        allowedIndexes.append([rowIndex,columnIndex])
                if(cupSize == m):
                    if(column == s or column == 0):
                        allowedIndexes.append([rowIndex,columnIndex])
                if(cupSize == l):
                    if(column != l):
                        allowedIndexes.append([rowIndex,columnIndex])
        if len(allowedIndexes) == 0:
            continue
        else:
            break
    # i have the allowed indexes!!now lets make a moves!!
    allowdListIndex = random.randint(0,len(allowedIndexes) -1 )
    allowedListItem = allowedIndexes[allowdListIndex]
    # remove -1 
    cupListTemp[cupSizeIndex][cupSize] -= 1
    # show on board the cupsize!!
    board[allowedListItem[0]][allowedListItem[1]] = cupSize
    return board
def checkCups(list1):
    listTest = list1.copy()
    for index,dict1 in enumerate(listTest):
        for key,value in dict1.items():
            if(value <=0):
                list1.remove(dict1)
    return list1

def game(board,cups):
    stepTemp = 0
    global mylist,cupList
    global steps
    while True:
        # make a move!!! -> random
        # check if i am finsihed with some cups!
        cups_list = checkCups(cups) 
        if(checkIfWin(board)):
            steps.append(stepTemp)
            break
        else:
            # make a new move!
            stepTemp += 1
            board = makeMove(cups_list,board)
            

def playGames(board,cupList):
    global steps,mylist
    listTemp = mylist.copy()
    for i in range(0,100):
        game(listTemp,cupList)
        cupList = [{'s':9},{'m':9},{'l':9}]
        listTemp = [[0,0,0],
          [0,0,0],
          [0,0,0]]
    averageSteps = sum(steps)/100
    print("Average steps:",averageSteps)

#game(mylist,cupList)

playGames(mylist,cupList)