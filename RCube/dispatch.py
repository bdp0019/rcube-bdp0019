import random
from random import shuffle
import math

def dispatch(parm={}):
    if(not('op' in parm)):
        return {'status':'error: missing op'}
    
    
    
    if isinstance(parm, set):
        return {'status':'error: op has not been specified'}
    
    
    #changed to include rotate
    if(not(parm['op'] == 'scramble' or parm['op'] == 'rotate')):
        return {'status':'error: invalid operation'}
    
    
    
    if(parm['op'] == 'scramble'):
        
        if('size' in parm):
            if (parm['size'] < 2):
                return {'status':'error: size must be greater than 1'}
            
            if (parm['size'] > 30):
                return {'status':'error: size must less than or equal to 30"'}
            
            if (parm['size'] > 1 and parm['size'] <= 30):
                dictToReturnWhenSizeIsValid = {}
                cube = scramble(parm ['size'])
                dictToReturnWhenSizeIsValid['cube'] = cube
                dictToReturnWhenSizeIsValid['status'] = 'scrambled'
                return dictToReturnWhenSizeIsValid
        else:
            dictToReturnWhenSizeIsNotGiven = {} 
            cubeGivenSizeThree = scramble(3)
            dictToReturnWhenSizeIsNotGiven['cube'] = cubeGivenSizeThree
            dictToReturnWhenSizeIsNotGiven['status'] = 'scrambled'
            return dictToReturnWhenSizeIsNotGiven
            
            
            
    if(parm['op'] == 'rotate'):
        
        if('cube' in parm):
            
            
            if(isValidCube(parm['cube'])):
            
            
                if('face' in parm):
                
                    if (isValidFace(parm['face'])):
                        #perform rotate
                        dictToReturnAfterRotate = {}
                        rotatedCube = rotate(parm['cube'], parm['face'])
                        
                        dictToReturnAfterRotate['status'] = 'rotated'
                        dictToReturnAfterRotate['cube'] = rotatedCube
                        return dictToReturnAfterRotate
                
                
                
                
                    else:
                        return {'status':'error: invalid face'}
                
            
            
                else:
                    return {'status':'error: face is missing'}
                
                
                
            else:
                return {'status':'error: invalid cube'}
        
        
        else:
            return {'status':'error: cube is missing'}
        
        
    return parm



#takes size as parameter. Returns a list representing the scrambled cube
def scramble(size):
    
    actualElementsInCube = []
    
    if size is None:
        size = 3
    
    sizeOfFaceOfCube = size*size
    
    increment1 = 0
    #adds 1 to list
    while (increment1 < sizeOfFaceOfCube):
        actualElementsInCube.append(1)
        increment1 = increment1 + 1
        
    increment2 = 0
    #adds 2 to list
    while (increment2 < sizeOfFaceOfCube):
        actualElementsInCube.append(2)
        increment2 = increment2 + 1
        
    increment3 = 0
    #adds 3 to list
    while (increment3 < sizeOfFaceOfCube):
        actualElementsInCube.append(3)
        increment3 = increment3 + 1
        
    increment4 = 0
    #adds 4 to list
    while (increment4 < sizeOfFaceOfCube):
        actualElementsInCube.append(4)
        increment4 = increment4 + 1
        
    increment5 = 0
    #adds 5 to list
    while (increment5 < sizeOfFaceOfCube):
        actualElementsInCube.append(5)
        increment5 = increment5 + 1
        
    increment6 = 0
    #adds 6 to list
    while (increment6 < sizeOfFaceOfCube):
        actualElementsInCube.append(6)
        increment6 = increment6 + 1
    
    #shuffles the list
    shuffle(actualElementsInCube)
    
    
    return actualElementsInCube







#takes cube and face as parameter. Returns a rotated cube.
def rotate(cube, face):
    if (face == "F" or face == 'F'):
        return rotateF(cube)
    
    elif (face == "F'" or face == "F%27"):
        return rotateFbackwards(cube)
    
    elif (face == "R"):
        return rotateR(cube)
    
    elif (face == "R'" or face == "R%27"):
        return rotateRbackwards(cube)
    
    elif (face == "L"):
        return rotateL(cube)
    
    elif (face == "L'" or face == "L%27"):
        return rotateLbackwards(cube)
    
    elif (face == "U"):
        return rotateU(cube)
    
    elif (face == "U'" or face == "U%27"):
        return rotateUbackwards(cube)
    
    elif (face == "D"):
        return rotateD(cube)
    
    elif (face == "D'" or face == "D%27"):
        return rotateDbackwards(cube)
    
    elif (face == "B"):
        return rotateB(cube)
    
    elif (face == "B'" or face == "%27"):
        return rotateBbackwards(cube)
    
    else:
        return cube
    
    
    
    
    
    




#Takes face as parameter. Checks to see if face given is valid. Returns a boolean
def isValidFace(face):
    if(face == "R"):
        return True
    elif(face == "R'" or face == "R%27"):
        return True
    elif(face == "L"):
        return True
    elif(face == "L'" or face == "L%27"):
        return True
    elif(face == "U"):
        return True
    elif(face == "U'" or face == "U%27"):
        return True
    elif(face == "D"):
        return True
    elif(face == "D'" or face == "D%27"):
        return True
    elif(face == "F" or face == 'F'):
        return True
    elif(face == "F'" or face == "F%27"):
        return True
    elif(face == "B"):
        return True
    elif(face == "B'" or face == "B%27"):
        return True
    else:
        return False
    



#not finished
def isValidCube(cube):
    countingForValidity = 0
    incrementer = 2
    
    sizeOfCube = len(cube)
    colorCount = sizeOfCube / 6
    sizeOfRadius = int(math.sqrt(colorCount))
    
    #checks validity of size. CountingForValidity = 1
    while (incrementer < 31):
        if (sizeOfCube == 6*incrementer**2):
            countingForValidity = countingForValidity + 1
        incrementer = incrementer + 1
    
    
    #checks for size of color 1. CountingForValidity = 2
    incrementer = 0
    tempColorCount = 0
    while (incrementer < sizeOfCube):
        if (cube[incrementer] == 1):
            tempColorCount = tempColorCount + 1
        incrementer = incrementer + 1
    if (tempColorCount == colorCount):
        countingForValidity = countingForValidity + 1
        
    
    #checks for size of color 2. CountingForValidity = 3
    incrementer = 0
    tempColorCount = 0
    while (incrementer < sizeOfCube):
        if (cube[incrementer] == 2):
            tempColorCount = tempColorCount + 1
        incrementer = incrementer + 1
    if (tempColorCount == colorCount):
        countingForValidity = countingForValidity + 1
        
    
    #checks for size of color 3. CountingForValidity = 4
    incrementer = 0
    tempColorCount = 0
    while (incrementer < sizeOfCube):
        if (cube[incrementer] == 3):
            tempColorCount = tempColorCount + 1
        incrementer = incrementer + 1
    if (tempColorCount == colorCount):
        countingForValidity = countingForValidity + 1
    
    
    #checks for size of color 4. CountingForValidity = 5
    incrementer = 0
    tempColorCount = 0
    while (incrementer < sizeOfCube):
        if (cube[incrementer] == 4):
            tempColorCount = tempColorCount + 1
        incrementer = incrementer + 1
    if (tempColorCount == colorCount):
        countingForValidity = countingForValidity + 1
    
    
    #checks for size of color 5. CountingForValidity = 6
    incrementer = 0
    tempColorCount = 0
    while (incrementer < sizeOfCube):
        if (cube[incrementer] == 5):
            tempColorCount = tempColorCount + 1
        incrementer = incrementer + 1
    if (tempColorCount == colorCount):
        countingForValidity = countingForValidity + 1
    
    
    #checks for size of color 6. CountingForValidity = 7
    incrementer = 0
    tempColorCount = 0
    while (incrementer < sizeOfCube):
        if (cube[incrementer] == 1):
            tempColorCount = tempColorCount + 1
        incrementer = incrementer + 1
    if (tempColorCount == colorCount):
        countingForValidity = countingForValidity + 1
    
    
    
    if (countingForValidity == 7):
        return True
    else:
        return False







def rotateF(cube):
    
    
    newCube = list(cube)
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    #first face
    while (increment < sizeOfSideOfCube):
        
        newCube[((increment + 1) % sizeOfRadius) * (sizeOfRadius - (increment / sizeOfRadius + 1))] = cube[increment]
        increment = increment + 1
    
    #second face gets squares from 5th face
    increment2 = sizeOfSideOfCube
    counterOfSwaps = 0
    
    while (increment2 < 2 * sizeOfSideOfCube):
        
        if (increment2 % sizeOfRadius == 0):
            #performs a swap
            newCube[increment2] = cube[5 * sizeOfSideOfCube - sizeOfRadius + counterOfSwaps]
            counterOfSwaps = counterOfSwaps + 1
        
        increment2 = increment2 + 1
        
    #third face does not change
    
    #4th face gets from 6th face. 
    increment3 = 3 * sizeOfSideOfCube
    counterOfSwaps1 = 0
    counterOfIncrements = 1
    
    while (increment3 < 4 * sizeOfSideOfCube):
        if (counterOfIncrements % sizeOfRadius == 0):
            #performs a swap
            newCube[increment3] = cube[5 * sizeOfSideOfCube + counterOfSwaps1]
            counterOfSwaps1 = counterOfSwaps1 + 1
        counterOfIncrements = counterOfIncrements + 1
        increment3 = increment3 + 1
    
    
    
    #5th face gets from 4th face
    increment4 = 0
    counterOfIncrements1 = 1
    while (increment4 < sizeOfSideOfCube):
        if (increment4 % sizeOfRadius == 0):
            newCube[5* sizeOfSideOfCube - counterOfIncrements1] = cube[3 * sizeOfSideOfCube + increment4]
            counterOfIncrements1 = counterOfIncrements1 + 1
        increment4 = increment4 + 1
    
    
    #6th face gets from 2nd face
    increment5 = 0
    counterOfIncrements2 = 1
    while (increment5 < sizeOfSideOfCube):
        if(increment5 % sizeOfRadius == 0):
            newCube[5 * sizeOfSideOfCube + sizeOfRadius - counterOfIncrements2] = cube[sizeOfSideOfCube + increment5]
            counterOfIncrements2 = counterOfIncrements2 + 1
        increment5 = increment5 + 1
    
    
    
    
    return newCube
















#
def rotateFbackwards(cube):
    
    
    newCube = list(cube)
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    #first face
    while (increment < sizeOfSideOfCube):
        
        newCube[increment] = cube[((increment + 1) % sizeOfRadius) * (sizeOfRadius - (increment / sizeOfRadius + 1))]
        increment = increment + 1
    
    #5th from 2nd
    increment2 = sizeOfSideOfCube
    counterOfSwaps = 0
    
    while (increment2 < 2 * sizeOfSideOfCube):
        
        if (increment2 % sizeOfRadius == 0):
            #performs a swap
            newCube[5 * sizeOfSideOfCube - sizeOfRadius + counterOfSwaps] = cube[increment2]
            counterOfSwaps = counterOfSwaps + 1
        
        increment2 = increment2 + 1
        
    #third face does not change
    
    #6th from 4th 
    increment3 = 3 * sizeOfSideOfCube
    counterOfSwaps1 = 0
    counterOfIncrements = 1
    
    while (increment3 < 4 * sizeOfSideOfCube):
        if (counterOfIncrements % sizeOfRadius == 0):
            #performs a swap
            newCube[5 * sizeOfSideOfCube + counterOfSwaps1] = cube[increment3]
            counterOfSwaps1 = counterOfSwaps1 + 1
        counterOfIncrements = counterOfIncrements + 1
        increment3 = increment3 + 1
    
    
    
    #4th from 5th
    increment4 = 0
    counterOfIncrements1 = 1
    while (increment4 < sizeOfSideOfCube):
        if (increment4 % sizeOfRadius == 0):
            newCube[3 * sizeOfSideOfCube + increment4 + (sizeOfRadius - 1)] = cube[5* sizeOfSideOfCube - counterOfIncrements1]
            counterOfIncrements1 = counterOfIncrements1 + 1
        increment4 = increment4 + 1
    
    
    #2nd from 6th
    increment5 = 0
    counterOfIncrements2 = 1
    while (increment5 < sizeOfSideOfCube):
        if(increment5 % sizeOfRadius == 0):
            newCube[sizeOfSideOfCube + increment5] = cube[5 * sizeOfSideOfCube + sizeOfRadius - counterOfIncrements2]
            counterOfIncrements2 = counterOfIncrements2 + 1
        increment5 = increment5 + 1
    
    
    
    return newCube




def rotateU(cube):
    
    newCube = list(cube)
    
    
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    #first face gets from 2nd
    while (increment < sizeOfRadius):
        newCube[increment] = cube[sizeOfSideOfCube + increment]
        increment = increment = increment + 1
        
    #second face gets from 3rd
    
    increment = 0
    while (increment < sizeOfRadius):
        newCube[sizeOfSideOfCube + increment] = cube[2 * sizeOfSideOfCube + increment]
        increment = increment = increment + 1
    
    #3rd face gets from 4th
    
    increment = 0
    while (increment < sizeOfRadius):
        newCube[2 * sizeOfSideOfCube + increment] = cube[3 * sizeOfSideOfCube + increment]
        increment = increment = increment + 1
    
    #4th face gets from 1st
    increment = 0
    while (increment < sizeOfRadius):
        newCube[2 * sizeOfSideOfCube + increment] = cube[3 * sizeOfSideOfCube + increment]
        increment = increment = increment + 1
        
        
    
    increment = 0
    while (increment < sizeOfRadius):
        newCube[3 * sizeOfSideOfCube + increment] = cube[increment]
        increment = increment = increment + 1
    
        
    
    #5th face rearranges
    while (increment < sizeOfSideOfCube):
        
        newCube[4 * sizeOfSideOfCube + increment] = cube[4 * sizeOfSideOfCube + ((increment + 1) % sizeOfRadius) * (sizeOfRadius - (increment / sizeOfRadius + 1))]
        increment = increment + 1
    
    
    return newCube


















def rotateUbackwards(cube):
    newCube = list(cube)
    
    
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    #first face gets from 2nd
    while (increment < sizeOfRadius):
        newCube[sizeOfSideOfCube + increment] = cube[increment]
        increment = increment = increment + 1
        
    #second face gets from 3rd
    
    increment = 0
    while (increment < sizeOfRadius):
        newCube[2 * sizeOfSideOfCube + increment] = cube[sizeOfSideOfCube + increment]
        increment = increment = increment + 1
    
    #3rd face gets from 4th
    
    increment = 0
    while (increment < sizeOfRadius):
        newCube[3 * sizeOfSideOfCube + increment] = cube[2 * sizeOfSideOfCube + increment]
        increment = increment = increment + 1
    
    #4th face gets from 1st
    increment = 0
    while (increment < sizeOfRadius):
        newCube[3 * sizeOfSideOfCube + increment] = cube[2 * sizeOfSideOfCube + increment]
        increment = increment = increment + 1
        
        
    
    increment = 0
    while (increment < sizeOfRadius):
        newCube[increment] = cube[3 * sizeOfSideOfCube + increment]
        increment = increment = increment + 1
    
        
    
    #5th face rearranges
    while (increment < sizeOfSideOfCube):
        
        newCube[4 * sizeOfSideOfCube + ((increment + 1) % sizeOfRadius) * (sizeOfRadius - (increment / sizeOfRadius + 1))] = cube[4 * sizeOfSideOfCube + increment]
        increment = increment + 1
    
    
    return newCube







def rotateR(cube):
    return cube

def rotateRbackwards(cube):
    return cube


def rotateL(cube):
    return cube

def rotateLbackwards(cube):
    return cube


def rotateD(cube):
    return cube

def rotateDbackwards(cube):
    return cube

def rotateB(cube):
    return cube

def rotateBbackwards(cube):
    return cube











