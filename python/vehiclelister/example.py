#class or module code
class  vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
            
            
    def display_info(self):
       print("vehicle_name:",self.name)
       print("vehicle_speed:",self.max_speed)
       print("vehicle_mileage:",self.mileage)
        

#example codes:
#from vehiclelister import vehicle  
#tesela = vehicle("tesela",200,10)
#tesela.display_info()






#example code 2
#from vehiclelister import vehicle 
tesela = vehicle("tesela",200,10)
honda = vehicle("honda",300,30)
x = 1
vehicles = [tesela,honda]
for car in vehicles:
    print("car:",x)
    x += 1
    car.display_info()
    print("")