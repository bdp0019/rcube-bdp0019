import random


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




