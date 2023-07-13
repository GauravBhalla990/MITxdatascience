###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
import os
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

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
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
    bigw = list(cows.values())
    names = []
    bigws = []
    flycows = []
    all_trips = []

    # bubble sort algorithm to order cow weights in descending order of weight
    for i in range(len(bigw)):
        for j in range(len(bigw) - 1):
            if (bigw[j] < bigw[j + 1]):
                tmp = bigw[j]
                bigw[j] = bigw[j + 1]
                bigw[j + 1] = tmp

    # unique weight values list of cows
    val = bigw[0]
    bigws.append(val)
    for i in range(len(bigw)): 
        if bigw[i] != val:
            val = bigw[i]
            bigws.append(val)

    # gets sorted list of cows in descending order of weight
    for i in range(len(bigws)):
        curr = bigws[i]
        for key in cows:
            if (cows[key] == curr):
                names.append(key)
            

    #allocating cows to trips on spaceship
    dynms = names[:] # dynamic cow name list that will be updated
    
    for i in range(len(cows)):
        flycows = []
        if (names[i] in dynms):
            flycows.append(names[i])
            dynms.remove(names[i])
            wt = bigw[i]
        for j in range(i + 1, len(cows)):
            if (names[j] in dynms) and (((wt + bigw[j]) <= limit)):
                flycows.append(names[j])
                dynms.remove(names[j])
                wt += bigw[j]
        if(flycows):
            all_trips.append(flycows)
    
    
    return all_trips




        

        

    


        
    


        


# Problem 2
def brute_force_cow_transport(cows,limit=10):
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
    bigw = list(cows.values())
    names = list(cows.keys())
    bigws = [] #special/unique weight values
    all_trips = []

    # revise this code
    #get list of minimum trips
    cowsum = 0
    dynms = names[:] # dynamic cow name list that will be updated
    rmcows = []
    partcws = []

    for partition in get_partitions(names):
        #if gg, Aucks are aucking
        if not(dynms):
            break
        # reaches end of partition level and no gg, reset cows + trips
        else:
            for k in range(len(partcws)):
                dynms.append(partcws[k])
            all_trips = []
            partcws = []
        
        #each partition level
        for i in range(len(partition)):
            cowsum = 0
            rmcows = []
            #each paritition in a level
            for j in range(len(partition[i])):
                #if other successful partition has cow, break
                # not sure this first if statement is necessary
                # was thinking that if other sub partition in the same level had that cow, 
                # but not possible because all sub partitions contain all possible cows
                if(partition[i][j] not in dynms):
                    for k in range(len(rmcows)):
                        dynms.append(rmcows[k])
                        partcws.remove(rmcows[k])
                    break
                if(cowsum <= limit):
                    cowsum += cows[partition[i][j]]
                    dynms.remove(partition[i][j])
                    rmcows.append(partition[i][j])
                    partcws.append(partition[i][j])
                if(cowsum > limit): # if partition not good, reset
                    #adding back cows that need to fly
                    for k in range(len(rmcows)):
                        dynms.append(rmcows[k])
                        partcws.remove(rmcows[k])
                    break
                # otherwise if partition is good and in last part of partition
                elif(j == len(partition[i]) - 1):
                    all_trips.append(partition[i])
    return all_trips
    
        


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
    cows = load_cows(os.path.dirname(os.path.abspath(__file__)) + "\ps1_cow_data.txt")
    limit=10
    print(cows)

    start = time.time()
    ## code to be timed
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print("Greedy Time: " + str(end - start))

    start = time.time()
    ## code to be timed
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print("Brute Force Time: " + str(end - start))




"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""
compare_cow_transport_algorithms()



