class Reservation:
    reservationNumber=0
    roomNum=0
    customer=""
    day=""
    fee=0
    id=""

    def __init__(self,resNum,room,name,day):
        self.reservationNumber=resNum
        self.roomNum=room
        self.customer=name
        self.day=day
        self.fee=self.calculateFee()
        self.id=Reservation.generateID(room,day)

    def generateID(roomNum,day):
        return str(roomNum)+day
    
    def calculateFee(self):
        return self.roomNum*2


r1 = Reservation(1,5,"a","10/21")
#print(r1.id)