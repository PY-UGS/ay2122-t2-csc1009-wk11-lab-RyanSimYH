class Calculator:
    def __init__(self):
        self.input1 = 0.0
        self.input2 = 0.0

    def getInput(self):
        # obtain user input and convert it to a float
        print("Please Enter 2 values seperated by a new line")
        self.input1 = float(input())
        self.input2 = float(input())
    def adder(self):
        return self.input1 + self.input2 # perform addition to the 2 values and return for printing
    def subtractor(self):
        return self.input1 - self.input2 # perform subtraction to the 2 values and return for printing
    def mutiplier(self):
        return self.input1 * self.input2 # perform multiplication to the 2 values and return for printing
    def divider(self):
        return self.input1 / self.input2 # perform division to the 2 values and return for printing
    def clear(self):
        # reset both inputs to 0
        self.input1 = 0.0
        self.input2 = 0.0

calResults = Calculator()
calResults.getInput()
print("Addition:", calResults.adder()) # print the result for the addition
print("Subtraction", calResults.subtractor()) # print the result for the subtraction
print("Mutiplication", calResults.mutiplier()) # print the result for the multiplication
print("Division", calResults.divider()) # print the result for the division
calResults.clear() # reset the values
