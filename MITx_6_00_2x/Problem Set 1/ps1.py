###########################
# 6.00.2x Problem Set 1: Space Cows

import time
from ps1_partition import get_partitions

#================================
# Part A: Transporting Space Cows
#================================


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    text_file = open(filename, 'r')

    for line in text_file:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Copy the dictionary. That way we won't change it.
    cows_copy = [(k, v) for k, v in dict.items(cows)]
    weight_loaded = 0
    # Sort cows by weight for the greedy heuristic
    cows_sorted = sorted(cows_copy, key=lambda cow: cow[1], reverse=True)
    cows_left = cows_sorted[:]
    cows_loaded, trips_with_cows = [], []
    # Add cows to trip until limit is reached, remove those cows from
    # cows that are left to load.
    while cows_left != []:
        for cow in cows_sorted:
            if weight_loaded + cow[1] <= limit:
                cows_loaded.append(cow[0])
                weight_loaded += cow[1]
                cows_left.remove(cow)
        trips_with_cows.append(cows_loaded)
        cows_loaded = []
        weight_loaded = 0
        cows_sorted = cows_left[:]
    return trips_with_cows


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    transports = get_partitions(cows.keys())
    legal_transports = []
    # Check all single trips for a transport.
    for transport in transports:
        # If the load is higher than the limit for a single trip, the whole
        # transport is invalid.
        legal_trips = []
        total_weight_of_trip = 0
        for trip in transport:
            total_weight_of_trip = 0
            for cow in trip:
                total_weight_of_trip += cows[cow]
            if total_weight_of_trip <= limit:
                legal_trips.append(trip)
            else:
                break
        # All trips of the transport are within the weight limit.
        if len(legal_trips) == len(transport):
            legal_transports.append(legal_trips)
    # Pick the transport with lowest amount of trips
    best_transport = sorted(legal_transports, key=lambda x: len(x))
    return best_transport[0]


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start_greedy = time.time()
    greedy_result = greedy_cow_transport(cows, limit)
    end_greedy = time.time()
    start_brute = time.time()
    brute_result = brute_force_cow_transport(cows, limit)
    end_brute = time.time()
    greedy_time = (end_greedy - start_greedy)
    brute_time = (end_brute - start_brute)
    difference_time = abs(greedy_time - brute_time)

    print('Number of trips for:\n  |---> greedy: {}\n  |---> brute: {}'.format(
        len(greedy_result), len(brute_result)))
    print('Time elapsed for:\n  |---> greedy: {}\n  |---> brute: {}\n  |---> Difference: {}'.format(
        greedy_time, brute_time, difference_time))


"""
    Here is some test data for you to see the results of your algorithms with.
    Do not submit this along with any of your answers. Uncomment the last two
    lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
#cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
limit = 10

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()
