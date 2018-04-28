import random
import math


#takes size as paramater. Returns a list representing the scrambled cube
def scramble(size):
    numberOfElementsOnCube = 6*size^2
    elementsStillInCubeChecker = []
    actualElementsInCube = []
    instancesOfOneColorOnCube = size^2
    loopCounter = 0
    
    #fills in cube with -1 for all elements
    for i in range(numberOfElementsOnCube):
        actualElementsInCube.append(-1)
    
    #fills up a mock cube with the number of the index. Cube is same size of original to ensure that a space is not modified twice
    for i in range(numberOfElementsOnCube):
        elementsStillInCubeChecker.append(i)
    
    #fills up 1/6 of the cube with one color: 1/6 filled total
    while (loopCounter < size^2):
        elementOnCubeToBeReplaced = random.randint(0, numberOfElementsOnCube)
        
        if elementOnCubeToBeReplaced in elementsStillInCubeChecker:
            indexOfElement = elementsStillInCubeChecker.index(elementOnCubeToBeReplaced)
            actualElementsInCube[indexOfElement] = 1
            del elementsStillInCubeChecker[indexOfElement]
            loopCounter + 1
    
    #fills up 1/6 of cube with second color: 2/6 filled total
    while (loopCounter < size^2):
        elementOnCubeToBeReplaced = random.randint(0, numberOfElementsOnCube)
        
        if elementOnCubeToBeReplaced in elementsStillInCubeChecker:
            indexOfElement = elementsStillInCubeChecker.index(elementOnCubeToBeReplaced)
            actualElementsInCube[indexOfElement] = 2
            del elementsStillInCubeChecker[indexOfElement]
            loopCounter + 1
    
    #fills up 1/6 of the cube with third color: 3/6 filled total
    while (loopCounter < size^2):
        elementOnCubeToBeReplaced = random.randint(0, numberOfElementsOnCube)
        
        if elementOnCubeToBeReplaced in elementsStillInCubeChecker:
            indexOfElement = elementsStillInCubeChecker.index(elementOnCubeToBeReplaced)
            actualElementsInCube[indexOfElement] = 3
            del elementsStillInCubeChecker[indexOfElement]
            loopCounter + 1
    
    #fills up 1/6 of the cube with fourth color: 4/6 filled total
    while (loopCounter < size^2):
        elementOnCubeToBeReplaced = random.randint(0, numberOfElementsOnCube)
        
        if elementOnCubeToBeReplaced in elementsStillInCubeChecker:
            indexOfElement = elementsStillInCubeChecker.index(elementOnCubeToBeReplaced)
            actualElementsInCube[indexOfElement] = 4
            del elementsStillInCubeChecker[indexOfElement]
            loopCounter + 1
    
    #fills up 1/6 of the cube with fifth color: 5/6 filled total
    while (loopCounter < size^2):
        elementOnCubeToBeReplaced = random.randint(0, numberOfElementsOnCube)
        
        if elementOnCubeToBeReplaced in elementsStillInCubeChecker:
            indexOfElement = elementsStillInCubeChecker.index(elementOnCubeToBeReplaced)
            actualElementsInCube[indexOfElement] = 5
            del elementsStillInCubeChecker[indexOfElement]
            loopCounter + 1
    
    #fills up 1/6 of the cube with sixth color: 6/6 filled total
    while (loopCounter < size^2):
        elementOnCubeToBeReplaced = random.randint(0, numberOfElementsOnCube)
        
        if elementOnCubeToBeReplaced in elementsStillInCubeChecker:
            indexOfElement = elementsStillInCubeChecker.index(elementOnCubeToBeReplaced)
            actualElementsInCube[indexOfElement] = 6
            del elementsStillInCubeChecker[indexOfElement]
            loopCounter + 1
    
    
    
    return actualElementsInCube









def rotateFbackwards(cube):
    
    print(cube)
    
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
    
    
    print(newCube)
    
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











def checkForCross(cube):                #######    working on this one now
    
    sizeOfWholeCube = len(cube)
    sizeOfSideOfCube = sizeOfWholeCube / 6
    sizeOfRadius = int(math.sqrt(sizeOfSideOfCube))
    
    if(sizeOfRadius%2 == 0):
        return False
    
    
    
    #check first face for crosses
    increment = 0
    while(increment < sizeOfSideOfCube):
        
        ####do math here
        
        increment = increment + 1
    
    #check 2nd face for crosses
    increment = sizeOfSideOfCube
    while(increment < 2 * sizeOfSideOfCube):
        
        ####do math here
        
        increment = increment + 1
    
    #check 3rd face for crosses
    increment = 2 * sizeOfSideOfCube
    while(increment < 3 *sizeOfSideOfCube):
        
        ####do math here
        
        increment = increment + 1
    
    #check 4th face for crosses
    increment = 3 * sizeOfSideOfCube
    while(increment < 4 * sizeOfSideOfCube):
        
        ####do math here
        
        increment = increment + 1
    
    #check 5th face for crosses
    increment = 4 * sizeOfSideOfCube
    while(increment < 5 * sizeOfSideOfCube):
        
        ####do math here
        
        increment = increment + 1
    
    #check 6th face for crosses
    increment = 5 * sizeOfSideOfCube
    while(increment < 6 * sizeOfSideOfCube):
        
        ####do math here
        
        increment = increment + 1
    
    
    
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
