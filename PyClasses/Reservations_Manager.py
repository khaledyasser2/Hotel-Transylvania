class Reservations_Manager:
    reservations={}
    rooms={21:["10/21",2,3,4,5]}

    def showAvailableRooms():
        return [k for (k,v) in Reservations_Manager.rooms if len(v) != 0]
    
    
