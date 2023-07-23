import datetime
import copy
from read_csv import map_csv
from read_csv import create_matrix

distances = create_matrix()  # 2D Matrix (List containing lists) of the data found in 'distanceData.csv'
packages = map_csv()  # Hashmap Object containing a Key-Value Pair of [packageID, package] found in 'inputs.csv'
original_list = copy.deepcopy(packages)  # Copy of Hashmap used in snapshot function
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
pack_9_update = datetime.datetime(year, month, day, 10, 20, 0)


# Main Algorithm (Req A) - Greedy Algorithm O(N^2) Where N is an integer from 1-16
def calculate_route(current_truck, start_time):
    current_location = 0  # start at HUB
    package_9_flag = False

    if isinstance(start_time, str):  # Makes sure the input is not already datetime before converting to datetime
        (hrs, mins, secs) = start_time.split(':')
        start_time = datetime.datetime(year, month, day, int(hrs), int(mins), int(secs))

    current_time = start_time

    for key in current_truck.set:  # Update each package on the truck with a start time when truck leaves HUB
        packages.get(key).update(9, start_time)
        packages.get(key).update(8, 'en route')

    for deliveries in range(len(current_truck.set)):  # Outer Loop represents each delivery made for the given truck
        local_minimum = None
        current_delivery = ''
        for key in current_truck.set:  # Inner Loop calculates a Local Minimum
            destination_index = int(packages.get(key).get()[11])
            miles_to_destination = float(distances[current_location][destination_index])
            if key == '9' and current_time < pack_9_update:  # Prevents Package 9 from being delivered before update
                miles_to_destination = local_minimum
            if local_minimum is None or local_minimum > miles_to_destination:
                local_minimum = float(miles_to_destination)
                current_delivery = key

        # Local Min is determined, so we drive to that location
        current_truck.miles += local_minimum
        calc_time = (60 / 18) * local_minimum
        current_time += datetime.timedelta(minutes=calc_time)

        # When the current time becomes 10:20am, the address for packageID: 9 becomes '410 S State S'
        if (current_time >= pack_9_update) and package_9_flag is False:
            packages.get('9').update(1, '410 S State St')
            packages.get('9').update(11, '19')
            package_9_flag = True

        # Delivery is Made, update package delivered, update location, remove packageID from truck
        packages.get(current_delivery).update(8, 'delivered')
        packages.get(current_delivery).update(10, current_time)
        current_location = int(packages.get(current_delivery).get()[11])
        if current_delivery is not None:
            current_truck.remove(current_delivery)

    # drive back to HUB
    current_truck.miles += float(distances[current_location][0])
    return current_truck.miles, current_time


def snapshot(selected_time, input_package):
    (hrs, mins, secs) = selected_time.split(':')
    selected_time = datetime.datetime(year, month, day, int(hrs), int(mins), int(secs))
    departure_time = packages.get(input_package).get()[9]
    delivery_time = packages.get(input_package).get()[10]
    # Status: en route
    if departure_time < selected_time < delivery_time:
        transit_package = copy.deepcopy(original_list.get(input_package))
        transit_package.update(8, 'en route')
        transit_package.update(9, departure_time)
        if input_package == '9' and selected_time >= pack_9_update:  # because Package 9's address is known
            transit_package.update(1, '410 S State St')
            transit_package.update(11, '19')
        transit_package.print()
    # Status: Delivered
    elif selected_time >= delivery_time:
        packages.get(input_package).print()
    # Status : at HUB
    else:
        original_list.get(input_package).print()
    print('\n')
