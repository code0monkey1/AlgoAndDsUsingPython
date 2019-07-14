
class LogicGate():
     def __init__(self,n):
         self.label=n
         self.output=None
         print("The ",self.label," logic gate has been initiated")

     def getLabel(self):
         return self.label

     def getOutput(self):
         print("Entering GEt OUtpout Block")
         self.output= self.performGateLogic()
         return self.output


class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA=None
        self.pinB=None

    def getPinA(self):
        return int(input("Enter the value of pin A : "))

    def getPinB(self):
        return int(input("Enter the value of pin B : "))


class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin=None

    def getPin(self):
        return int(input("Enter the value of pin  : "))

class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        pinA=self.getPinA()
        pinB=self.getPinB()

        if pinB==1 and pinA==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        print("Performing ",self.label," logic ")
        self.pinA = self.getPinA()
        self.pinB = self.getPinB()

        if self.pinB == 1 or self.pinA == 1:
            return 1
        else:
            return 0

class NotGage(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        print("Performing ", self.label, " logic ")
        self.pin=self.getPin()
        if self.pin==1:
            return 0
        else :
            return 1

def main():
    myAndGate=AndGate("AndGate")
    print( myAndGate.getOutput())

    orGate=OrGate("MyOrGate")
    print((orGate.getOutput()))

    notGate=NotGage("MyNotGate")
    print(notGate.getOutput())

main()