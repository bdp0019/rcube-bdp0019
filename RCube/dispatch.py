import random
from random import shuffle
import math

def dispatch(parm={}):
    if(not('op' in parm)):
        return {'status':'error: missing op'}
    
    
    
    if isinstance(parm, set):
        return {'status':'error: op has not been specified'}
    
    
    #changed to include rotate
    if(not(parm['op'] == 'scramble' or parm['op'] == 'rotate' or parm['op'] == 'check')):
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
        
        
        
        
    
    if(parm['op'] == 'check'):
        
        
        if('cube' in parm):
            
            if(isValidCube(parm['cube'])):
                
                if(checkForCross(parm['cube'])):
                    
                    dictToReturnWhenCrossExists = {} 
                    dictToReturnWhenCrossExists['status'] = 'crosses'
                    return dictToReturnWhenCrossExists
                
                elif(checkForSpots(parm['cube'])):
                    
                    dictToReturnWhenSpotsExists = {} 
                    dictToReturnWhenSpotsExists['status'] = 'spots'
                    return dictToReturnWhenSpotsExists
                
                
                elif(checkForFull(parm['cube'])):
                    
                    dictToReturnWhenCubeIsSolved = {} 
                    dictToReturnWhenCubeIsSolved['status'] = 'full'
                    return dictToReturnWhenCubeIsSolved
                
                else:
                    
                    dictToReturnWhenCubeIsUnknown = {} 
                    dictToReturnWhenCubeIsUnknown['status'] = 'unknown'
                    return dictToReturnWhenCubeIsUnknown
                
                
            
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
    shuffle(actualElementsInCube)             ##   old method
    
    
    
    randomNumberOfTurns = random.randint(10, 21)        #between 10-20
    incrementForTurns = 0
    
    while(incrementForTurns < randomNumberOfTurns):
        randomTurn = random.randint(1, 13)              # 1-12
        
        if(randomTurn == 1):
            rotateF(actualElementsInCube)
            
        elif(randomTurn == 2):
            rotateFbackwards(actualElementsInCube)
        
        elif(randomTurn == 3):
            rotateU(actualElementsInCube)
            
        elif(randomTurn == 4):
            rotateUbackwards(actualElementsInCube)
            
        elif(randomTurn == 5):
            rotateR(actualElementsInCube)
        
        elif(randomTurn == 6):
            rotateRbackwards(actualElementsInCube)
            
        elif(randomTurn == 7):
            rotateL(actualElementsInCube)
        
        elif(randomTurn == 8):
            rotateFbackwards(actualElementsInCube)
        
        elif(randomTurn == 9):
            rotateD(actualElementsInCube)
            
        elif(randomTurn == 10):
            rotateDbackwards(actualElementsInCube)
            
        elif(randomTurn == 11):
            rotateB(actualElementsInCube)
        
        elif(randomTurn == 12):
            rotateBbackwards(actualElementsInCube)
        incrementForTurns = incrementForTurns + 1
    
    
    return actualElementsInCube







#takes cube and face as parameter. Returns a rotated cube.
def rotate(cube, face):
    if (face == "F"):
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
        
        #newCube[((increment + 1) % sizeOfRadius) * (sizeOfRadius - (increment / sizeOfRadius + 1))] = cube[increment]
        newCube[(((increment%sizeOfRadius) + 1) * sizeOfRadius) - ((increment / sizeOfRadius) + 1)] = cube[increment]
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
        
        newCube[increment] = cube[(((increment%sizeOfRadius) + 1) * sizeOfRadius) - (increment / sizeOfRadius + 1)]
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
        increment = increment + 1
        
    #second face gets from 3rd
    
    increment = 0
    while (increment < sizeOfRadius):
        newCube[sizeOfSideOfCube + increment] = cube[2 * sizeOfSideOfCube + increment]
        increment = increment + 1
    
    #3rd face gets from 4th
    
    increment = 0
    while (increment < sizeOfRadius):
        newCube[2 * sizeOfSideOfCube + increment] = cube[3 * sizeOfSideOfCube + increment]
        increment = increment + 1
    
    #4th face gets from 1st
    increment = 0
    while (increment < sizeOfRadius):
        newCube[2 * sizeOfSideOfCube + increment] = cube[3 * sizeOfSideOfCube + increment]
        increment = increment + 1
        
        
    
    increment = 0
    while (increment < sizeOfRadius):
        newCube[3 * sizeOfSideOfCube + increment] = cube[increment]
        increment = increment + 1
    
        
    
    #5th face rearranges
    while (increment < sizeOfSideOfCube):
        
        newCube[4 * sizeOfSideOfCube + increment] = cube[4 * sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (increment / sizeOfRadius + 1)]
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
        
        newCube[4 * sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (increment / sizeOfRadius + 1)] = cube[4 * sizeOfSideOfCube + increment]
        increment = increment + 1
    
    
    return newCube






def rotateR(cube):
    
    newCube = list(cube)
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    #first face pulls 6th face
    while (increment < sizeOfSideOfCube):
        
        
        if((increment + 1)%sizeOfRadius == 0):
            newCube[increment] = cube[5 * sizeOfSideOfCube - 1 + increment]
        increment = increment + 1
    
    #second face rearranges
    increment = sizeOfSideOfCube
    counter = 0
    
    while (increment < 2 * sizeOfSideOfCube): 
        newCube[sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (counter / sizeOfRadius + 1)] = cube[increment]
        increment = increment + 1
        counter = counter + 1
    
    
    #3rd from 5th face
    increment = 2 * sizeOfSideOfCube
    counterOfIncrements = 0
    counterForSwitch = sizeOfRadius
    
    while (increment < 3 * sizeOfSideOfCube):
        if (counterForSwitch%sizeOfRadius == 0):
            #performs a swap
            newCube[increment] = cube[5 * sizeOfSideOfCube - 1 - counterOfIncrements]
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
        counterForSwitch = counterForSwitch + 1
    
    #4th face unchanged
    #5th face gets from 1st face
    increment = 4 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (increment < 5 * sizeOfSideOfCube):
        if ((increment + 1)%sizeOfRadius == 0):
            newCube[increment] = cube[counterOfIncrements]
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    
    #6th face gets from 3rd face
    increment = 5 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (increment < 6 *sizeOfSideOfCube):
        if((increment + 1)%sizeOfRadius == 0):
            newCube[increment] = cube[3 * sizeOfSideOfCube - 1 - counterOfIncrements]
            
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    
    
    return newCube
    






def rotateRbackwards(cube):
    newCube = list(cube)
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    #first face pulls 6th face //ignore// all are backwards
    
    while (increment < sizeOfSideOfCube):
        
        
        if((increment + 1)%sizeOfRadius == 0):
            
            newCube[5 * sizeOfSideOfCube + increment] = cube[increment]
        increment = increment + 1
    #second face rearranges  //
    increment = sizeOfSideOfCube
    counter = 0
    
    while (increment < 2 * sizeOfSideOfCube): 
        newCube[increment] = cube[sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (counter / sizeOfRadius + 1)]
        increment = increment + 1
        counter = counter + 1
    
    #3rd from 5th face  //ignore
    increment = 2 * sizeOfSideOfCube
    counterOfIncrements = 0
    counterForSwitch = sizeOfRadius
    
    while (increment < 3 * sizeOfSideOfCube):
        if (counterForSwitch%sizeOfRadius == 0):
            #performs a swap
            newCube[5 * sizeOfSideOfCube - 1 - counterOfIncrements] = cube[increment]
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
        counterForSwitch = counterForSwitch + 1
    #4th face unchanged
    #5th face gets from 1st face  //ignore
    increment = 4 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (increment < 5 * sizeOfSideOfCube):
        if ((increment + 1)%sizeOfRadius == 0):
            newCube[counterOfIncrements] = cube[increment]
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    #6th face gets from 3rd face  //ignore 
    increment = 5 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (increment < 6 *sizeOfSideOfCube):
        if((increment + 1)%sizeOfRadius == 0):
            newCube[3 * sizeOfSideOfCube - 1 - counterOfIncrements] = cube[increment]
            
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    
    return newCube






def rotateL(cube):
    newCube = list(cube)
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    
    #first face pulls 5th
    while (increment < sizeOfSideOfCube):
        
        
        if((increment + sizeOfRadius)%sizeOfRadius == 0):
            newCube[increment] = cube[4 * sizeOfSideOfCube + increment]
        increment = increment + 1
    
    #second face does not change
    #3rd face pulls from 6th
    increment = 2 * sizeOfSideOfCube
    counterOfIncrements = 0
    
    while (increment < 3 * sizeOfSideOfCube): 
        if((increment + 1)%sizeOfRadius == 0):
            newCube[increment] = cube[6 * sizeOfSideOfCube - 1 - counterOfIncrements]
        increment = increment + 1
        counterOfIncrements = counterOfIncrements + 1
    
    
    #4th rearranges
    increment = 3 * sizeOfSideOfCube
    counter = 0
    
    while (increment < 3 * sizeOfSideOfCube):
        newCube[3 * sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (counter / sizeOfRadius + 1)] = cube[increment]
        increment = increment + 1
        counter = counter + 1
    
    
    #5th face gets from 3rd face
    increment = 4 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (increment < 5 * sizeOfSideOfCube):
        if ((increment)%sizeOfRadius == 0):
            newCube[increment] = cube[3 * sizeOfSideOfCube - 1 - counterOfIncrements]
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    
    #6th face gets from 1st
    increment = 5 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (increment < 6 *sizeOfSideOfCube):
        if((increment)%sizeOfRadius == 0):
            newCube[increment] = cube[counterOfIncrements]
            
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    
    
    return newCube




def rotateLbackwards(cube):
    newCube = list(cube)
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    
    #first face pulls 5th
    while (increment < sizeOfSideOfCube):
        
        
        if((increment + sizeOfRadius)%sizeOfRadius == 0):
            newCube[4 * sizeOfSideOfCube + increment] = cube[increment]
        increment = increment + 1
    
    #second face does not change
    #3rd face pulls from 6th
    increment = 2 * sizeOfSideOfCube
    counterOfIncrements = 0
    
    while (increment < 3 * sizeOfSideOfCube): 
        if((increment + 1)%sizeOfRadius == 0):
            newCube[6 * sizeOfSideOfCube - 1 - counterOfIncrements] = cube[increment]
        increment = increment + 1
        counterOfIncrements = counterOfIncrements + 1
    
    
    #4th rearranges
    increment = 3 * sizeOfSideOfCube
    counter = 0
    
    while (increment < 3 * sizeOfSideOfCube):
        newCube[increment] = cube[3 * sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (counter / sizeOfRadius + 1)]
        increment = increment + 1
        counter = counter + 1
    
    
    #5th face gets from 3rd face
    increment = 4 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (increment < 5 * sizeOfSideOfCube):
        if ((increment)%sizeOfRadius == 0):
            newCube[3 * sizeOfSideOfCube - 1 - counterOfIncrements] = cube[increment]
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    
    #6th face gets from 1st
    increment = 5 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (increment < 6 *sizeOfSideOfCube):
        if((increment)%sizeOfRadius == 0):
            newCube[counterOfIncrements] = cube[increment]
            
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    
    return newCube
















def rotateD(cube):
    newCube = list(cube)
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    
    #first face pulls 4th
    while (increment < sizeOfRadius):
        
        newCube[sizeOfSideOfCube - 1 - increment] = cube[4 * sizeOfSideOfCube - 1 - increment]
        increment = increment + 1
    

    #2nd face pulls from 1st
    increment = 0
    
    while (increment < sizeOfRadius): 
        newCube[2 * sizeOfSideOfCube - 1 - increment] = cube[sizeOfSideOfCube - 1 - increment]
        increment = increment + 1
    
    
    #3rd pulls from 2nd
    increment = 0
    
    while (increment < sizeOfRadius):
        newCube[3 * sizeOfSideOfCube - 1 - increment] = cube[2 * sizeOfSideOfCube - 1 - increment]
        increment = increment + 1
    
    
    #4th face gets from 3rd face
    increment = 0
    while (increment < sizeOfRadius):
        newCube[4 * sizeOfSideOfCube - 1 - increment] = cube[3 * sizeOfSideOfCube - 1 - increment]
        increment = increment + 1
    
    #5th stays the same
    #6th rearranges
    increment = 5 * sizeOfSideOfCube
    counter = 0
    while (increment < 6 *sizeOfSideOfCube):
        newCube[5 * sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (counter / sizeOfRadius + 1)] = cube[increment]
        increment = increment + 1
        counter = counter + 1
    
    
    
    return newCube







def rotateDbackwards(cube):
    newCube = list(cube)
    
    increment = 0
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    
    #first face pulls 4th
    while (increment < sizeOfRadius):
        newCube[4 * sizeOfSideOfCube - 1 - increment] = cube[sizeOfSideOfCube - 1 - increment]
        increment = increment + 1
    

    #2nd face pulls from 1st
    increment = 0
    
    while (increment < sizeOfRadius): 
        newCube[sizeOfSideOfCube - 1 - increment] = cube[2 * sizeOfSideOfCube - 1 - increment]
        increment = increment + 1
    
    
    #3rd pulls from 2nd
    increment = 0
    
    while (increment < sizeOfRadius):
        newCube[2 * sizeOfSideOfCube - 1 - increment] = cube[3 * sizeOfSideOfCube - 1 - increment]
        increment = increment + 1
    
    
    #4th face gets from 3rd face
    increment = 0
    while (increment < sizeOfRadius):
        newCube[3 * sizeOfSideOfCube - 1 - increment] = cube[4 * sizeOfSideOfCube - 1 - increment]
        increment = increment + 1
    
    #5th stays the same
    #6th rearranges
    increment = 5 * sizeOfSideOfCube
    counter = 0
    while (increment < 6 *sizeOfSideOfCube):
        newCube[increment] = cube[5 * sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (counter / sizeOfRadius + 1)]
        increment = increment + 1
        counter = counter + 1
    
    
    
    return newCube







def rotateB(cube):
    newCube = list(cube)
    
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    increment = sizeOfSideOfCube
    counterOfSwaps = 0
    #first does not change
    #2nd face pulls from 6th
    while (increment < 2 * sizeOfSideOfCube):
        
        if((increment + 1)%sizeOfRadius == 0):
            newCube[increment] = cube[6 * sizeOfSideOfCube - 1 - counterOfSwaps]
            counterOfSwaps = counterOfSwaps + 1
        increment = increment + 1
    
    #3rd rearranges
    increment = 2 * sizeOfSideOfCube
    counter = 0
    
    while (increment < 3 * sizeOfSideOfCube): 
        newCube[2 * sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (counter / sizeOfRadius + 1)] = cube[increment]
        increment = increment + 1
        counter = counter + 1
    
    
    #4th pulls from 5
    increment = 3 * sizeOfSideOfCube
    counterOfSwaps = 0
    
    while (increment < 4 * sizeOfSideOfCube):
        if((increment)%sizeOfRadius == 0):
            newCube[increment] = cube[4 * sizeOfSideOfCube + sizeOfRadius - counterOfSwaps]
            counterOfSwaps = counterOfSwaps + 1
        increment = increment + 1
    
    
    #5th face gets from 2nd face
    increment = 4 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (counterOfIncrements < sizeOfRadius):
        newCube[increment] = cube[sizeOfSideOfCube - 1 + (sizeOfRadius * (counterOfIncrements + 1))]
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    
    #6th face gets from 4th
    increment = 6 * sizeOfSideOfCube - 1
    counterOfIncrements = 0
    while (counterOfIncrements < sizeOfRadius):
        newCube[increment] = cube[4 * sizeOfSideOfCube - (sizeOfRadius * (counterOfIncrements + 1))]
            
        counterOfIncrements = counterOfIncrements + 1
        increment = increment - 1
    
    
    
    return newCube








def rotateBbackwards(cube):        ##   no change yet. 
    newCube = list(cube)
    
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    increment = sizeOfSideOfCube
    counterOfSwaps = 0
    #first does not change
    #2nd face pulls from 6th
    while (increment < 2 * sizeOfSideOfCube):
        
        if((increment + 1)%sizeOfRadius == 0):
            newCube[6 * sizeOfSideOfCube - 1 - counterOfSwaps] = cube[increment]
            counterOfSwaps = counterOfSwaps + 1
        increment = increment + 1
    
    #3rd rearranges
    increment = 2 * sizeOfSideOfCube
    counter = 0
    
    while (increment < 3 * sizeOfSideOfCube): 
        newCube[increment] = cube[2 * sizeOfSideOfCube + (((increment%sizeOfRadius) + 1) * sizeOfRadius) - (counter / sizeOfRadius + 1)]
        increment = increment + 1
        counter = counter + 1
    
    
    #4th pulls from 5
    increment = 3 * sizeOfSideOfCube
    counterOfSwaps = 0
    while (increment < 4 * sizeOfSideOfCube):
        if((increment)%sizeOfRadius == 0):
            newCube[4 * sizeOfSideOfCube - 1 + sizeOfRadius - counterOfSwaps] = cube[increment]
            counterOfSwaps = counterOfSwaps + 1
        increment = increment + 1
    
    #5th face gets from 2nd face
    increment = 4 * sizeOfSideOfCube
    counterOfIncrements = 0
    while (counterOfIncrements < sizeOfRadius):
        newCube[sizeOfSideOfCube - 1 + (sizeOfRadius * (counterOfIncrements + 1))] = cube[increment]
        counterOfIncrements = counterOfIncrements + 1
        increment = increment + 1
    
    
    #6th face gets from 4th
    increment = 6 * sizeOfSideOfCube - 1
    counterOfIncrements = 0
    while (counterOfIncrements < sizeOfRadius):
        newCube[4 * sizeOfSideOfCube - (sizeOfRadius * (counterOfIncrements + 1))] = cube[increment]
            
        counterOfIncrements = counterOfIncrements + 1
        increment = increment - 1
    
    
    
    return newCube









def checkForFull(cube):
    
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    
    
    #check first face for full
    increment = 1
    firstIntChecker = cube[0]
    while(increment < sizeOfSideOfCube):
        
        
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        
        increment = increment + 1
    
    #check 2nd face for full
    increment = sizeOfSideOfCube + 1
    secondIntChecker = cube[sizeOfSideOfCube]
    while(increment < 2 * sizeOfSideOfCube):
        
        
        
        if(not(secondIntChecker == cube[increment])):
            return False
        
        
        increment = increment + 1
    
    #check 3rd face for full
    increment = 2 * sizeOfSideOfCube + 1
    thirdIntChecker = cube[2 * sizeOfSideOfCube]
    while(increment < 3 *sizeOfSideOfCube):
        
        
        
        if(not(thirdIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    #check 4th face for full
    increment = 3 * sizeOfSideOfCube + 1
    fourthIntChecker = cube[3 * sizeOfSideOfCube]
    while(increment < 4 * sizeOfSideOfCube):
        
        
        
        if(not(fourthIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    #check 5th face for full
    increment = 4 * sizeOfSideOfCube + 1
    fifthIntChecker = cube[4 * sizeOfSideOfCube]
    while(increment < 5 * sizeOfSideOfCube):
        
        
        
        if(not(fifthIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    #check 6th face for full
    increment = 5 * sizeOfSideOfCube + 1
    sixthIntChecker = cube[5 * sizeOfSideOfCube]
    while(increment < 6 * sizeOfSideOfCube):
        
        
        
        if(not(sixthIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    
    return True











def checkForSpots(cube):                ####    done
    
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    
    if(sizeOfRadius == 2):
        return False
    
    #check 1st half of 1st face for equal
    increment = 0
    firstIntChecker = cube[0]
    while(increment < ((sizeOfSideOfCube - 1)/2)):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    #checks middle of first face
    increment = (sizeOfSideOfCube - 1)/2
    firstFaceCenter = cube[increment]
    if(firstFaceCenter == firstIntChecker):
        return False
    
    
    #check 2nd half of 1st face for equal
    increment = ((sizeOfSideOfCube - 1)/2) + 1
    while(increment < sizeOfSideOfCube):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    
    
    
    #######   begin checking second face
    
    
    #check 1st half of 2nd face for equal
    increment = sizeOfSideOfCube
    firstIntChecker = cube[sizeOfSideOfCube]
    while(increment < (sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2))):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    #checks middle of 2nd face
    increment = sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    secondFaceCenter = cube[increment]
    if(secondFaceCenter == firstIntChecker or secondFaceCenter == firstFaceCenter):
        return False
    
    
    #check 2nd half of 2nd face for equal
    increment = (sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)) + 1
    while(increment < 2 * sizeOfSideOfCube):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    
    
    
    
    
    #######   begin checking third face
    
    
    #check 1st half of 3rd face for equal
    increment = 2 * sizeOfSideOfCube
    firstIntChecker = cube[2 * sizeOfSideOfCube]
    while(increment < (2 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2))):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    #checks middle of 3rd face
    increment = 2 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    thirdFaceCenter = cube[increment]
    if(thirdFaceCenter == firstIntChecker or thirdFaceCenter == firstFaceCenter or thirdFaceCenter == secondFaceCenter):
        return False
    
    
    #check 2nd half of 3rd face for equal
    increment = (2 *sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)) + 1
    while(increment < 3 * sizeOfSideOfCube):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
        
        
        
        
        
        
        #######   begin checking 4th face
    
    
    
    #check 1st half of 4th face for equal
    increment = 3 * sizeOfSideOfCube
    firstIntChecker = cube[3 * sizeOfSideOfCube]
    while(increment < (3 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2))):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    #checks middle of 4th face
    increment = 3 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    fourthFaceCenter = cube[increment]
    if(fourthFaceCenter == firstIntChecker or fourthFaceCenter == firstFaceCenter or fourthFaceCenter == secondFaceCenter or fourthFaceCenter == thirdFaceCenter):
        return False
    
    
    #check 2nd half of 4th face for equal
    increment = (3 *sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)) + 1
    while(increment < 4 * sizeOfSideOfCube):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    
    
    
    #######   begin checking 5th face
    
    
    
    #check 1st half of 5th face for equal
    increment = 4 * sizeOfSideOfCube
    firstIntChecker = cube[4 * sizeOfSideOfCube]
    while(increment < (4 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2))):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    #checks middle of 5th face
    increment = 4 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    fifthFaceCenter = cube[increment]
    if(fifthFaceCenter == firstIntChecker or fifthFaceCenter == firstFaceCenter or fifthFaceCenter == secondFaceCenter or fifthFaceCenter == thirdFaceCenter or fifthFaceCenter == fourthFaceCenter):
        return False
    
    
    #check 2nd half of 5th face for equal
    increment = (4 *sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)) + 1
    while(increment < 5 * sizeOfSideOfCube):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    
    
    
    
    #######   begin checking 5th face
    
    
    
    
    
    #check 1st half of 6th face for equal
    increment = 5 * sizeOfSideOfCube
    firstIntChecker = cube[5 * sizeOfSideOfCube]
    while(increment < (5 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2))):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    #checks middle of 6th face
    increment = 5 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    sixthFaceCenter = cube[increment]
    if(sixthFaceCenter == firstIntChecker or sixthFaceCenter == firstFaceCenter or sixthFaceCenter == secondFaceCenter or sixthFaceCenter == thirdFaceCenter or sixthFaceCenter == fourthFaceCenter or sixthFaceCenter == fifthFaceCenter):
        return False
    
    
    #check 2nd half of 6th face for equal
    increment = (5 *sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)) + 1
    while(increment < 6 * sizeOfSideOfCube):
        
        if(not(firstIntChecker == cube[increment])):
            return False
        
        increment = increment + 1
    
    
    
    
    
    
    
    return True







def checkForCross(cube):                #######    working on this one now
    
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    if(sizeOfRadius == 2):
        return False
    
    
    
    ####    check first face for crosses    ###
    
    
    
    # check for center for 1st face
    firstFaceCenterPosition = (sizeOfSideOfCube - 1)/2
    firstFaceCenterValue = cube[firstFaceCenterPosition]
    
    #throw in if statement comparing centers on all of the rest of the faces
    
    
    # check for horizontal for 1st face
    increment = 1
    while(increment < (sizeOfRadius - 1)/2 + 1):
        
        
        if(not(firstFaceCenterValue == cube[firstFaceCenterPosition + increment] == cube[firstFaceCenterPosition - increment])):
            return False
        
        increment = increment + 1
    
    
    
    # check for vertical for 1st face
    increment = (sizeOfRadius - 1)/2
    while(increment < sizeOfSideOfCube):
        if(not(cube[increment] == firstFaceCenterValue)):
            return False
        increment = increment + sizeOfRadius
    
    
    #check to see that center of 1st face is different that first increment in face
    increment = 0
    firstValueInFace = cube[increment]
    if(firstFaceCenterValue == firstValueInFace):
        return False
    
    
    # check amount of cube[increment] values in 1st face     should = 4((sizeOfRadius - 1)/2)^2
    counter = 0
    while(increment < sizeOfSideOfCube):
        
        if(firstValueInFace == cube[increment]):
            counter = counter + 1
        
        increment = increment + 1
    
    if(not(counter == 4 * (((sizeOfRadius - 1)/2)**2))):
        return False
    
    
    
    
    
    ####    check second face for crosses    ###
    
    
    
    # check for center for 2nd face
    secondFaceCenterPosition = sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    secondFaceCenterValue = cube[secondFaceCenterPosition]
    
    #if statement comparing centers
    if(secondFaceCenterValue == firstFaceCenterValue):
        return False
    
    
    # check for horizontal for 2nd face
    increment = 1
    while(increment < (sizeOfRadius - 1)/2 + 1):
        
        
        if(not(secondFaceCenterValue == cube[secondFaceCenterPosition + increment] == cube[secondFaceCenterPosition - increment])):
            return False
        
        increment = increment + 1
    
    
    
    # check for vertical for 2nd face
    increment = sizeOfSideOfCube + ((sizeOfRadius - 1)/2)
    while(increment < 2 * sizeOfSideOfCube):
        if(not(cube[increment] == secondFaceCenterValue)):
            return False
        increment = increment + sizeOfRadius
    
    
    #check to see that center of 2nd face is different that first increment in face
    increment = sizeOfSideOfCube
    firstValueInFace = cube[increment]
    if(secondFaceCenterValue == firstValueInFace):
        return False
    
    
    # check amount of cube[increment] values in 2nd face     should = 4((sizeOfRadius - 1)/2)^2
    counter = 0
    while(increment < 2 * sizeOfSideOfCube):
        
        if(firstValueInFace == cube[increment]):
            counter = counter + 1
        
        increment = increment + 1
    
    if(not(counter == 4 * (((sizeOfRadius - 1)/2)**2))):
        return False
    
    
    
    
    
    
    ####    check third face for crosses    ###
    
    
    
    # check for center for 3rd face
    thirdFaceCenterPosition = 2 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    thirdFaceCenterValue = cube[thirdFaceCenterPosition]
    
    #if statement comparing centers
    if(thirdFaceCenterValue == firstFaceCenterValue or thirdFaceCenterValue == secondFaceCenterValue):
        return False
    
    
    # check for horizontal for 3rd face
    increment = 1
    while(increment < (sizeOfRadius - 1)/2 + 1):
        
        
        if(not(thirdFaceCenterValue == cube[thirdFaceCenterPosition + increment] == cube[thirdFaceCenterPosition - increment])):
            return False
        
        increment = increment + 1
    
    
    
    # check for vertical for 3rd face
    increment = 2 * sizeOfSideOfCube + ((sizeOfRadius - 1)/2)
    while(increment < 3 * sizeOfSideOfCube):
        if(not(cube[increment] == thirdFaceCenterValue)):
            return False
        increment = increment + sizeOfRadius
    
    
    #check to see that center of 3rd face is different that first increment in face
    increment = 2 * sizeOfSideOfCube
    firstValueInFace = cube[increment]
    if(thirdFaceCenterValue == firstValueInFace):
        return False
    
    
    # check amount of cube[increment] values in 3rd face     should = 4((sizeOfRadius - 1)/2)^2
    counter = 0
    while(increment < 3 * sizeOfSideOfCube):
        
        if(firstValueInFace == cube[increment]):
            counter = counter + 1
        
        increment = increment + 1
    
    if(not(counter == 4 * (((sizeOfRadius - 1)/2)**2))):
        return False

    
    
    
    
    
    ####    check fourth face for crosses    ###
    
    
    
    # check for center for 4th face
    fourthFaceCenterPosition = 3 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    fourthFaceCenterValue = cube[fourthFaceCenterPosition]
    
    #if statement comparing centers
    if(fourthFaceCenterValue == firstFaceCenterValue or fourthFaceCenterValue == secondFaceCenterValue or fourthFaceCenterValue == thirdFaceCenterValue):
        return False
    
    
    # check for horizontal for 4th face
    increment = 1
    while(increment < (sizeOfRadius - 1)/2 + 1):
        
        
        if(not(fourthFaceCenterValue == cube[fourthFaceCenterPosition + increment] == cube[fourthFaceCenterPosition - increment])):
            return False
        
        increment = increment + 1
    
    
    
    # check for vertical for 4th face
    increment = 3 * sizeOfSideOfCube + ((sizeOfRadius - 1)/2)
    while(increment < 4 * sizeOfSideOfCube):
        if(not(cube[increment] == fourthFaceCenterValue)):
            return False
        increment = increment + sizeOfRadius
    
    
    #check to see that center of 4th face is different that first increment in face
    increment = 3 * sizeOfSideOfCube
    firstValueInFace = cube[increment]
    if(fourthFaceCenterValue == firstValueInFace):
        return False
    
    
    # check amount of cube[increment] values in 4th face     should = 4((sizeOfRadius - 1)/2)^2
    counter = 0
    while(increment < 4 * sizeOfSideOfCube):
        
        if(firstValueInFace == cube[increment]):
            counter = counter + 1
        
        increment = increment + 1
    
    if(not(counter == 4 * (((sizeOfRadius - 1)/2)**2))):
        return False
    
    
    
    
    
    ####    check fifth face for crosses    ###
    
    
    
    # check for center for 5th face
    fifthFaceCenterPosition = 4 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    fifthFaceCenterValue = cube[fifthFaceCenterPosition]
    
    #if statement comparing centers
    if(fifthFaceCenterValue == firstFaceCenterValue or fifthFaceCenterValue == secondFaceCenterValue or fifthFaceCenterValue == thirdFaceCenterValue or fifthFaceCenterValue == fourthFaceCenterValue):
        return False
    
    
    # check for horizontal for 5th face
    increment = 1
    while(increment < (sizeOfRadius - 1)/2 + 1):
        
        
        if(not(fifthFaceCenterValue == cube[fifthFaceCenterPosition + increment] == cube[fifthFaceCenterPosition - increment])):
            return False
        
        increment = increment + 1
    
    
    
    # check for vertical for 5th face
    increment = 4 * sizeOfSideOfCube + ((sizeOfRadius - 1)/2)
    while(increment < 5 * sizeOfSideOfCube):
        if(not(cube[increment] == fifthFaceCenterValue)):
            return False
        increment = increment + sizeOfRadius
    
    
    #check to see that center of 5th face is different that first increment in face
    increment = 4 * sizeOfSideOfCube
    firstValueInFace = cube[increment]
    if(fifthFaceCenterValue == firstValueInFace):
        return False
    
    
    # check amount of cube[increment] values in 5th face     should = 4((sizeOfRadius - 1)/2)^2
    counter = 0
    while(increment < 5 * sizeOfSideOfCube):
        
        if(firstValueInFace == cube[increment]):
            counter = counter + 1
        
        increment = increment + 1
    
    if(not(counter == 4 * (((sizeOfRadius - 1)/2)**2))):
        return False
    
    
    
    
    
    ####    check sixth face for crosses    ###
    
    
    
    
    
    # check for center for 6th face
    sixthFaceCenterPosition = 5 * sizeOfSideOfCube + ((sizeOfSideOfCube - 1)/2)
    sixthFaceCenterValue = cube[sixthFaceCenterPosition]
    
    #if statement comparing centers
    if(sixthFaceCenterValue == firstFaceCenterValue or sixthFaceCenterValue == secondFaceCenterValue or sixthFaceCenterValue == thirdFaceCenterValue or sixthFaceCenterValue == fourthFaceCenterValue or sixthFaceCenterValue == fifthFaceCenterValue):
        return False
    
    
    # check for horizontal for 5th face
    increment = 1
    while(increment < (sizeOfRadius - 1)/2 + 1):
        
        
        if(not(sixthFaceCenterValue == cube[sixthFaceCenterPosition + increment] == cube[sixthFaceCenterPosition - increment])):
            return False
        
        increment = increment + 1
    
    
    
    # check for vertical for 5th face
    increment = 5 * sizeOfSideOfCube + ((sizeOfRadius - 1)/2)
    while(increment < 6 * sizeOfSideOfCube):
        if(not(cube[increment] == sixthFaceCenterValue)):
            return False
        increment = increment + sizeOfRadius
    
    
    #check to see that center of 5th face is different that first increment in face
    increment = 5 * sizeOfSideOfCube
    firstValueInFace = cube[increment]
    if(sixthFaceCenterValue == firstValueInFace):
        return False
    
    
    # check amount of cube[increment] values in 5th face     should = 4((sizeOfRadius - 1)/2)^2
    counter = 0
    while(increment < 6 * sizeOfSideOfCube):
        
        if(firstValueInFace == cube[increment]):
            counter = counter + 1
        
        increment = increment + 1
    
    if(not(counter == 4 * (((sizeOfRadius - 1)/2)**2))):
        return False
    
    
    
    
    
    return True



















