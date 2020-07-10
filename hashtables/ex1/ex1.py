# Create dictionary
# Loop through weights:
#   Each weight is a dictionary key.  Value is a list containing the weight's index.
#   For duplicate weights, indices are appended onto the list.

# Loop through weights:
#   Check to see if an entry for (limit - weight) exists
#       If yes:
#            return index for each weight
# Return None <- loop ends without finding a combination that works

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create dictionary with weights as keys and list of indices as values
    weight_dict = {}
    for i, weight in enumerate(weights):
        # If the package's weight is new
        if weight not in weight_dict:
            weight_dict[weight] = [i]
        
        # If the package's weight is the same as a prior one's
        else:
            weight_dict[weight].append(i)
    
    # Loop through weights and calculate what the other weight needs 
    # to be to match the limit.
    # Then check if that weight exists in our dictionary of weights
    #       If yes, then get and return the indices
    for weight in weights:
        
        other_weight = limit - weight

        if other_weight in weight_dict:
            
            # Case of packages with different weights
            if weight != other_weight:
                indices = weight_dict[weight][0], weight_dict[other_weight][0]
                return max(indices), min(indices)

            # Case of packages with identical weights
            else:
                return weight_dict[weight][1], weight_dict[weight][0]
    
    return None