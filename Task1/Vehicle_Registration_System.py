class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
            
        def update_owner(self, new_owner): #added update_owner method
            if new_owner != self.owner: #check that the owner isn't the already existing owner
                self.owner = new_owner #change the owner to the one provided
            else: #owner is same
                 print("That owner is the same as the current owner. No updated done.") #notify user
        
        def display_vehicle(self): #added display method
            print(f"\nVehicle Registration Number: {self.registration_number}") #print the registration number
            print(f"Vehicle Type: {self.type}") #print the vehicle type
            print(f"Vehicle Owner: {self.owner}") #print the vehicle owner

vehicle_list = [Vehicle('456229931038', 'Sedan', 'John Smith'),
                Vehicle('934567238771', 'Pickup', 'Julie Jones'),
                Vehicle('688431289975', 'SUV', 'Jerrod Falkner'),
                Vehicle('831264762186', 'Sedan', 'Jane Smith'),
                Vehicle('721351651354', 'Sedan', 'Julie Jones')] #List of vehicles

print("Registered Vehicles:") #heading for the current list of vehicles
for vehicle in vehicle_list: #iterate through the vehicle list
    vehicle.display_vehicle() #call the iterated vehicle's display method

print("\nChanging Vehicles' Owner to new owner Jerry Jones\n") #Heading to notify user of change to ownership
for vehicle in vehicle_list: #iterate through the list of vehicles
    vehicle.update_owner('Jerry Jones') #update the owner to the new owner

print("\nNew Vehicle Registrations:") #Heading for updated list of Vehicles
for vehicle in vehicle_list: #iterate through the list of vehicles
    vehicle.display_vehicle() #call the iterated vehicle's display method