# main.py
# Add an import statement for the Vehicle class
from vehiclePackage.vehicleClass import * 

if __name__ == "__main__":
    # Instantiate an object of type Vehicle
    myCorvette = Vehicle("Car", 120) # Trigger a call to constructor
    myCorvette.printType()           # Invoking the method on the object
    
    # Invoke the getter for maximum speed, store the return value in a variable
    # Print that out
    
    speed = myCorvette.getSpeed()
    print("Maximum Speed:", speed)
    
    # Instantiate another Vehicle object. You can name it
    myAudi = Vehicle("Car")   # myAudi is an object of type Vehicle
    myAudi.printType()
    speed = myAudi.getSpeed()
    print("Maximum Speed:", speed)
    
    # I want a list of 3 Vehicles: Car, Boat, Space Ship
    # You can pick the names and properties
    
    myVehicles = [Vehicle("Honda Pilot", 100), Vehicle("Speed Boat", 50), Vehicle("Space Ship", 4000)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
    