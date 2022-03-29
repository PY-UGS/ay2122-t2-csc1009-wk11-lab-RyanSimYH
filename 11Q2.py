class clockTime:
    def __init__(self):
        self.Hour = 0
        self.Minute = 0
        self.Second = 0

    def setHours(self): # set the stored hour value based on user input
        while True:
            print("Please input the hour (0 - 23)")
            self.Hour = int(input()) # obtain input from user
            if 0<= self.Hour <=23: #verify user input and prompt if not valid
                break
            else:
                print("Invalid input Please enter a number between 0 to 23")

    def setMinute(self): # set the stored minute value based on user input
        while True:
            print("Please input the Minute (0 - 59)")
            self.Minute = int(input())
            if 0<= self.Minute <=59: #verify user input and prompt if not valid
                break
            else:
                print("Invalid input Please enter a number between 0 to 59")

    def setSecond(self): # set the stored second value based on user input
        while True:
            print("Please input the Second (0 - 59)")
            self.Second = int(input())
            if 0<= self.Second <=59: #verify user input and prompt if not valid
                break
            else:
                print("Invalid input Please enter a number between 0 to 59")

    def setTime(self):
        self.setHours()
        self.setMinute()
        self.setSecond()

    def showTime(self):
        print("The Time Stored is: ",self.Hour,":",self.Minute,":",self.Second)


clock = clockTime()
clock.setTime()
clock.showTime()