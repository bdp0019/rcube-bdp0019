import unittest
import RCube.dispatch as RCube


class dispatchTest(unittest.TestCase):


#dispatch() Analysis
#    input -> via parameter named parm; python dict, mandatory, arrives validated
#    processing -> happy path: routes parm from HTTP quesry string to specific code ('scramble')
#                sad path: taken of 'op' dict key is missing or is not 'scramble'
#output -> normal operation: return result determined by the 'op' key
#            abnormal operation: return {'status':'error: meaningful'}

    def test100_010_ShouldIndicateErrorConditionalMissingOp(self):
        inputParm = {}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])

    
    def test100_020_ShouldIndicateErrorOpIsMissing(self):
        inputParm = {'op'}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])
        
    def test100_020_ShouldIndicateErrorOpIsSetToSomethingNotScramble(self):
        inputParm = {'op'=='init'}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])
        
        
        #normal operation
        
    
        
        
        
    
        
        #GoodTest
    def test100_920_ShouldReturnScrambledCubeOfSizeThreeMissingSize(self):
        inputParm = {'op' :'scramble'}
        result = RCube.dispatch(inputParm)
        finalResult = result['cube']
        self.assertEquals(len(finalResult), 3*3*6)
        
        #GoodTest
    def test100_930_ShouldReturnScrambledCubeOfSize2(self):
        inputParm = {'op' :'scramble', 'size' : 2}
        result = RCube.dispatch(inputParm)
        finalResult = result['cube']
        self.assertEquals(len(finalResult), 2*2*6)
        
        #GoodTest
    def test100_940_ShouldReturnScrambledCubeOfSize30(self):
        inputParm = {'op' :'scramble', 'size' : 30}
        result = RCube.dispatch(inputParm)
        finalResult = result['cube']
        self.assertEquals(len(finalResult), 30*30*6)
        
        #GoodTest
    def test100_950_ShouldReturnErrorOfSizeTooBig(self):
        inputParm = {'op' :'scramble', 'size' : 31}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])
        
        #GoodTest
    def test100_960_ShouldReturnErrorOfSizeTooSmall(self):
        inputParm = {'op' :'scramble', 'size' : 1}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])
        
    #GoodTest
    def test100_970_ShouldReturnScrambledCubeBackwardsParm(self):
        inputParm = {'size' : 2, 'op' :'scramble'}
        result = RCube.dispatch(inputParm)
        finalResult = result['cube']
        self.assertEquals(len(finalResult), 2*2*6)

    #GoodTest
    def test100_980_TestToSeeThatThereAreSameAmountOfColorsOnCube(self):
        inputParm = {'op' :'scramble', 'size' : 2}
        result = RCube.dispatch(inputParm)
        finalResult = result['cube']
        appearancesOf1 = finalResult.count(1)
        appearancesOf6 = finalResult.count(6)
        self.assertEquals(appearancesOf1, appearancesOf6)

        
    def test100_981_ShouldReturnStatusScrambled(self):
        inputParm = {'op' :'scramble', 'size' : 2}
        result = RCube.dispatch(inputParm)
        finalResult = result['status']
        self.assertEquals('scrambled', finalResult)
        
        
    #notFinished
    def test100_990_TestToCheckThatThereIsACenterSquareForEveryColor(self):
        inputParm = {'size' : 1, 'op' :'scramble'}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])
        
    #notFinished
    def test100_991_TestToCheckThatThereAreFourCornerForEachColor(self):
        inputParm = {'size' : 1, 'op' :'scramble'}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])
        
        
        
        #tests for rotate in dispatch
        
    def test101_000_ShouldReturnErrorDueToNoCube(self):
        inputParm = {'op' :'rotate', 'face' : "F"}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])
        
        
        
    def test101_001_ShouldReturnErrorDueToNoFace(self):
        inputParm = {'op' :'rotate', 'cube' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6]}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])
        
        
    def test101_001_ShouldReturnErrorDueToInvalidFace(self):
        inputParm = {'op' :'rotate', 'cube' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6], 'face' : "Y"}
        result = RCube.dispatch(inputParm)
        self.assertEquals('error:',result['status'][0:6])
        
        
    
    
    
    

        #example given in requirements
    def test101_001_ShouldReturnRotatedCubeFaceF(self):
        inputParm = {'op' :'rotate', 'cube' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6], 'face' : "F"}
        result = RCube.dispatch(inputParm)
        finalResult = result['cube']
        cube = [1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 2, 5, 2, 2, 5, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 6, 4, 4, 6, 4, 4, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 2, 2, 2, 6, 6, 6, 6, 6, 6]
        self.assertEquals(cube, finalResult)
        
    def test101_002_ShouldReturnRotatedCubeFaceFbackwards(self):
        inputParm = {'op' :'rotate', 'cube' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 2, 5, 2, 2, 5, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 6, 4, 4, 6, 4, 4, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 2, 2, 2, 6, 6, 6, 6, 6, 6], 'face' : "F'"}
        result = RCube.dispatch(inputParm)
        finalResult = result['cube']
        cube = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        self.assertEquals(cube, finalResult)
        
        
        
        
    def test101_003_ShouldReturnRotatedAsStatus(self):
        inputParm = {'op' :'rotate', 'cube' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6], 'face' : "F"}
        result = RCube.dispatch(inputParm)
        finalResult = result['status']
        self.assertEquals('rotated', finalResult)
        
        
        
    def test101_004_ShouldReturnRotatedCubeFaceU(self):
        inputParm = {'op' :'rotate', 'cube' : [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6], 'face' : "U"}
        result = RCube.dispatch(inputParm)
        finalResult = result['cube']
        cube = [2, 2, 2, 1, 1, 1, 1, 1, 1, 3, 3, 3, 2, 2, 2, 2, 2, 2, 4, 4, 4, 3, 3, 3, 3, 3, 3, 1, 1, 1, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        self.assertEquals(cube, finalResult)
        
        
    def test101_005_ShouldReturnRotatedCubeFaceUbackwards(self):
        inputParm = {'op' :'rotate', 'cube' : [2, 2, 2, 1, 1, 1, 1, 1, 1, 3, 3, 3, 2, 2, 2, 2, 2, 2, 4, 4, 4, 3, 3, 3, 3, 3, 3, 1, 1, 1, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6], 'face' : "U'"}
        result = RCube.dispatch(inputParm)
        finalResult = result['cube']
        cube = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        self.assertEquals(cube, finalResult)
        
        
        
        
    