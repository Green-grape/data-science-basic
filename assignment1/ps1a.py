###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import operator;

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
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
    # TODO: Your code here
    ret={};
    f=open(filename, 'r');
    lines=f.readlines();
    for line in lines:
        cow, weight=line.split(",");
        ret[cow]=int(weight[0]);
    f.close();
    return ret;

# Problem 2
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
    # TODO: Your code here

    #itemgetter에 인덱스를 집어넣음
    cur_cows=sorted(cows.items(),key=operator.itemgetter(1),reverse=True);
    ret=[];
    cur_weight=0;
    cur_transport=[];
    for cow in cur_cows:
        if(cur_weight+cow[1]>limit):
            ret.append(cur_transport);
            cur_transport=[];
            cur_weight=0;
        cur_weight+=cow[1];
        cur_transport.append(cow[0]);
    if(len(cur_transport)>0): ret.append(cur_transport);
    return ret;

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
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
    # TODO: Your code here
    partitions=get_partitions(cows.items());
    ret=[0]*(len(cows.items())+1);
    for p in partitions:
        isBreak=False;
        for cows in p:
            cur_weight=0;
            for cow in cows:
                cur_weight+=cow[1];
                if(cur_weight>limit): 
                    isBreak=True;
                    break;
            if(isBreak):break;
        if(len(ret)>len(p) and isBreak==False): ret=p;
    return ret;
        
# Problem 4
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
    # TODO: Your code here
    cows=load_cows("ps1_cow_data.txt");
    start=time.time();
    ret1=greedy_cow_transport(cows);
    end=time.time();
    take1=end-start;

    start=time.time();
    ret2=brute_force_cow_transport(cows);
    end=time.time();
    take2=end-start;

    print(f"greedy_cow_transport() take: {take1}, trip:{len(ret1)}\n");
    print(f'brute_force_cow_transport() take: {take2}, trip:{len(ret2)}')


if __name__=="__main__":
    compare_cow_transport_algorithms();
