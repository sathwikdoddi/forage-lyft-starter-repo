from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        sum = 0
        for tire in self.tire_wear:
            sum += tire
        return sum >= 3