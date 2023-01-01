from Reservations_Manager import *
class Staff_Account:
    password=""

    def check_in(id):
        Reservations_Manager.reservations.pop(id)
    
    def check_out(room):
        pass