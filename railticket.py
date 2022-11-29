class Train:
    def __init__(self,  name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare
        
    def getInfo(self):
        print(f"The name of Train is : {self.name}")    
        print(f"Seats avilable in the train : {self.seats}")
        
    def getFare(self):
        print(f"The fare of his Train is : RS.{self.fare}") 
        
    def bookTicket(self):
        if(self.seats>0):
            print(f"your ticket has been booked! seat no. is {self.seats}")       
            self.seats=self.seats-1
        else:
            print(f"Sorry this train is full !")    

Status = Train("vande express","250", "145")
Status.getInfo()    
Status.getFare()
        
        