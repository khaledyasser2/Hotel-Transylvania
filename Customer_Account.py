from Reservations_Manager import *
from Reservation import *
class Customer_Account:
    reservationNums = []
    name=""
    password=""
    username="yamom"

    def __init__(self,name,password,username):
        self.name=name
        self.password=password
        self.username=username
    
    def reserveRoom(self,room,day):
        id=Reservation.generateID(room,day)
        res=Reservation(id,room,self.name,day)
        self.reservationNums.append(id)
        Reservations_Manager.reservations[id]=res
        Reservations_Manager.rooms[room].remove(day)

    def cancelReservation():
        pass

#jeff=Customer_Account("Jeff","123","JeffTheMan")
#print(Reservations_Manager.reservations)
#print(Reservations_Manager.rooms)
#jeff.reserveRoom(21,"10/21")
#print(Reservations_Manager.reservations)
#print(Reservations_Manager.rooms)