class trainbookingsystem:
    def __init__(self,name,seats,fare):
        self.name= name
        self.seats = seats
        self.fare = fare
    def getStatus(self):
        print(f"Name of Train is {self.name}")
        print(f"No of seats available in train {self.name} are {self.seats}")
    def getFareInfo(self):
        print(f"Fair for train {self.name} is {self.fare}")
        
    def bookingTicket(self):
        if self.seats>0:
            print(f"Your ticket is confirmed, seat no is {self.seats}")
            self.seats=self.seats-1
        else:
            print("All seats are booked")
        
        def cancellation(self,seatno):
            self.seats = [1,2,3,4,5,6]



train = trainbookingsystem("Rajdhani 140523",6,40)
train.getStatus()
train.getFareInfo()
train.bookingTicket()
train.getStatus()
train.bookingTicket()
train.getStatus()
train.bookingTicket()
train.getStatus()
train.bookingTicket()
