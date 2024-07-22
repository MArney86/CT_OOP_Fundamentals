class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
            
        def update_owner(self, new_owner):
            if new_owner != self.owner:
                self.owner = new_owner
        
        def display_vehicle(self):
            print(f"\nVehicle Registration Number: {self.registration_number}")
            print(f"Vehicle Type: {self.type}")
            print(f"Vehicle Owner: {self.owner}")

vehicle_list = [Vehicle('456229931038', 'Sedan', 'John Smith'),
                Vehicle('934567238771', 'Pickup', 'Julie Jones'),
                Vehicle('688431289975', 'SUV', 'Jerrod Falkner'),
                Vehicle('831264762186', 'Sedan', 'Jane Smith'),
                Vehicle('721351651354', 'Sedan', 'Julie Jones')]

print("Registered Vehicles:")
for vehicle in vehicle_list:
    vehicle.display_vehicle()

print("\nChanging Vehicles' Owner to new owner Jerry Jones\n")
for vehicle in vehicle_list:
    vehicle.update_owner('Jerry Jones')

print("\nNew Vehicle Registrations:")
for vehicle in vehicle_list:
    vehicle.display_vehicle()     