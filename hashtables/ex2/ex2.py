#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# use a dictionary with source as key and destination as value
# loop through it, the first key is None
# while the destination is not None
#   use the destination as the key for the next flight source

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here


    # Loop through our list of tickets and construct our dictionary.
    # We can also record the start and end points as we make the dictionary
    flight_dict = {}

    start = None
    end = None

    for tick in tickets:
        flight_dict[tick.source] = tick.destination

        if tick.source == 'NONE':
            start = tick.destination
            print('start', start)


    route = [0] * length
    route[0] = start

    for i in range(0, length - 1):
        
        next_flight = flight_dict[route[i]]

        route[i+1] = next_flight

    return route
