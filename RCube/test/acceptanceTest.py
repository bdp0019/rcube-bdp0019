import json
import unittest
import httplib

class acceptanceTest(unittest.TestCase):


    def setUp(self):
        self.ERROR = "error"
        self.MICROSERVICE_URL = "127.0.0.1"
        self.MICROSERVICE_PORT = 5000
        self.MICROSERVICE_PATH = "/rcube?"


    def rcube(self, queryString):
        try:
            theConnection = httplib.HTTPConnection(self.MICROSERVICE_URL, self.MICROSERVICE_PORT)
            theConnection.request("GET", self.MICROSERVICE_PATH + queryString)
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse
        except Exception as e:
            return "exception raised: " + str(e)
    
    def string2dict(self, httpResponse):
        jsonString = httpResponse.replace("'", "\"")
        unicodeDictionary = json.loads(jsonString)
        result = {}
        for element in unicodeDictionary:
            result[str(element)] = str(unicodeDictionary[element])
        return result



#--------------------------------------------
#    Acceptance Tests
#---------------------------------------------
#    100 rcube 
#    Boundary Value Analysis
#    Analysis:
#        input: http://...myURL... /rcube?<op>[<size>]
#            op -> string, .eq. 'scramble', mandatory, unvalidated, 
#            size -> string, integer, .GT. 1 and .LE. 30, optional, unvalidated
#
#        outputs:    string, dictionary, mandatory, validated
#            happy output: dictionary contains 'cube' and 'status'
#            sad output: disctionary contains only 'status'
#
#        Happy Path
#            input:
#                1. valid op, missing size
#                2. valid op, valid size
#                3. valid size, valid op
#            output:
#                string of dictionary containing 'cube' and 'status'
#
#        Sad Path: 
#            input: 
#                1.valid op, size below bound
#                2.valid op, size above bound
#                3.valid op, non-int size
#                4.invalid op
#                5.missing op
#            output:
#                string of dictionary containing only 'status'


    def test100_900_ShouldReturnErrorOnMissingOp(self):
        queryString = ""
        resultString = self.rcube(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('error:', resultDict['status'][0:6])


    def test100_910_ShouldReturnErrorOnOpNotScramble(self):
        queryString = "op=init"
        resultString = self.rcube(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('error:', resultDict['status'][0:6])
        
        #
    def test100_920_ShouldReturnScrambledCubeOfSizeThreeMissingSize(self):
        queryString = "op=scramble"
        resultString = self.rcube(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('scrambled', resultDict['status'])
        
        #
    def test100_930_ShouldReturnScrambledCubeOfSize2(self):
        queryString = "op=scramble&size=2"
        resultString = self.rcube(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('scrambled', resultDict['status'])
        
        #
    def test100_940_ShouldReturnScrambledCubeOfSize30(self):
        queryString = "op=scramble&size=30"
        resultString = self.rcube(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('scrambled', resultDict['status'])
        
        #
    def test100_950_ShouldReturnErrorOfSizeTooBig(self):
        queryString = "op=scramble&size=32"
        resultString = self.rcube(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('error:', resultDict['status'][0:6])
        
        #
    def test100_960_ShouldReturnErrorOfSizeTooSmall(self):
        queryString = "op=scramble&size=1"
        resultString = self.rcube(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('error:', resultDict['status'][0:6])
        
    #
    def test100_970_ShouldReturnScrambledCubeBackwardsParm(self):
        queryString = "size=2&op=scramble"
        resultString = self.rcube(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('scrambled', resultDict['status'])

















