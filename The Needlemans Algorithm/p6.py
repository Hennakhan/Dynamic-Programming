#!/usr/bin/env python3

import sys

def makeMatrix():
    global matrix, s, mismatch, match

   # Intialize matrix
    matrix = [[ 0 for i in range(columns) ] for j in range(rows)]

    for col in range(1, columns):
        matrix[0][col] = 0 #matrix [0][col-1] + gap

    for row in range(1, rows):
        matrix[row][0] = 0 #matrix [0][row-1] + gap


    #Initialize match - mismatch matrix
    s = [[0 for i in range(columns)] for j in range(rows)]
    for j in range (1, rows):
        for i in range(1, columns):
            if sequence2[j-1] == sequence1[i-1]:
                s[j][i] = match
            else:
                s[j][i] = mismatch
    #calling method to create scoring matrix
    matrixFill()

def matrixFill():
    memoryArray = []
    tempArray = []

    #getting the index current element and the previous element where it came from in a list
    for j in range (1, rows):
        for i in range(1, columns):
            tempArray =  [(matrix[j-1][i-1] + s[j][i]), (matrix[j][i-1] + gap) , (matrix[j-1][i] + gap)]
            indexOfMaxInTempArray = (tempArray.index(max (tempArray)))
            if indexOfMaxInTempArray == 0:
                memoryArray.append([j, i, j-1, i-1])
            if indexOfMaxInTempArray == 1:
                memoryArray.append([j, i, j, i-1])
            if indexOfMaxInTempArray == 2:
                memoryArray.append([j, i, j-1, i])
            matrix[j][i] = max(tempArray)

    #calling traceback function to store only the path into a list
    traceback(memoryArray)

def traceback(memoryArray):
    traceArray = []
    memoryArray.reverse()


    traceArray.append([(memoryArray[0][0]), (memoryArray[0][1])])
    inode = memoryArray [0][2]
    jnode = memoryArray [0][3]

    for i, ro in enumerate(memoryArray):
             if memoryArray[i][0] == inode and memoryArray[i][1] == jnode:
                traceArray.append([(memoryArray [i][0]), (memoryArray[i][1])])
                inode = memoryArray[i][2]
                jnode = memoryArray[i][3]

             if inode == 0 or jnode == 0:
                traceArray.append([inode, jnode])
                if inode == 0:
                    jnode = jnode - 1
                elif jnode == 0:
                    inode = inode - 1

    print_Sequence(traceArray)

def print_Sequence(traceArray):
    seqPrinter1 = ''
    seqPrinter2 = ''

    for i in range(0,len(traceArray)-1):
        if traceArray[i][1] == (traceArray[i + 1][1] + 1) and traceArray[i][0] == (traceArray[i + 1][0] + 1):
            seqPrinter1 = seqPrinter1 + str(sequence1[traceArray[i][1] - 1])
            seqPrinter2 = seqPrinter2 + str(sequence2[traceArray[i][0] - 1])
        elif traceArray[i][1] == (traceArray[i+1][1] +1):
            seqPrinter1 = seqPrinter1 + str(sequence1[traceArray[i][1] - 1])
            seqPrinter2 = seqPrinter2 + '-'
        elif traceArray[i][0] == (traceArray[i+1][0] + 1):
            seqPrinter1 = seqPrinter1 + '-'
            seqPrinter2 = seqPrinter2 + str(sequence2[traceArray[i][0] - 1])

    print(seqPrinter1[::-1])
    print(seqPrinter2[::-1])

################# Main #################

match = int(sys.argv[1])
mismatch = int(sys.argv[2])
gap = int(sys.argv[3])

sequence1 = input().strip()
sequence2 = input().strip()
matrix = []
s = []
rows = len(sequence2) + 1
columns = len(sequence1) + 1
makeMatrix()

