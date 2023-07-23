# Name: Benjamin Porter, ID: 010371941
# Traveling Salesman Project - WGU C950 Data Structures and Algorithms 2
from truck import Truck
from route import calculate_route
from route import snapshot


class Main:
    #  Load in Trucks
    truck1 = Truck('Truck 1', ['1', '13', '14', '15', '16', '19', '29', '34', '7', '39', '20', '21'])
    truck2 = Truck('Truck 2', ['3', '18', '36', '10', '11', '12', '23', '24', '37', '38', '5', '2', '33'])
    truck3 = Truck('Truck 3', ['27', '35', '30', '4', '8', '17', '22', '40', '6', '25', '26', '32', '31', '28', '9'])

    truck1Vals = calculate_route(truck1, '08:00:00')
    truck1End = truck1Vals[1]
    truck2Vals = calculate_route(truck2, '08:00:00')
    truck3Vals = calculate_route(truck3, truck1End)

    menu = """WGUPS Package Tracker: 
    1. End of Day Report - Print All Package Status and Total Mileage
    2. Search a Single Package Status at a specified Time
    3. Get All Package Status at a specified Time
    Enter '0' to close application""" + "\n"

    userInput = input(menu)

    while userInput != '0':
        if userInput == '1':
            for e in range(40):
                index = str(e + 1)
                snapshot('23:59:59', index)
            truck1.print()
            truck2.print()
            truck3.print()
            print("Total Miles Today: " + str((truck1.miles + truck2.miles + truck3.miles)) + '\n')
        elif userInput == '2':
            inputPackage = input('Type a PackageID (1-40): ')
            inputTime = input('Select Time of Snapshot (HH:MM:SS):')
            snapshot(inputTime, inputPackage)
        elif userInput == '3':
            selectedTime = input('Select Time of Snapshot (HH:MM:SS): ')
            for e in range(40):
                index = str(e + 1)
                snapshot(selectedTime, index)
        userInput = input(menu)
