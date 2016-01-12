# ShippingCalculator.py
# by __________
# Uses a function to determine total cost of online order
##################################################################
# Shipping:                                                     ##
##################################################################
#   All orders under $20 (.01 - 19.99) have a shipping of $5    ##
#   Orders between $20 and $50 (20.00 - 49.99) shipping of $10  ##
#   Orders over $50 (50.00 - 99.99) have a shipping of $15      ##
#   Orders $100 or more get free shipping                       ##
#   NOTE:                                                       ##
#       If any order amounts are 0 or less,                     ##
#           amount will be 0                                    ##
##################################################################

# define the getTotalCost() function
def getTotalCost(cost):
    """ returns total cost with shipping applied """
    shipping = 0
    # Get shipping

    # Calculate total cost

    total = cost + shipping

    print("cost = {} shipping = {} total cost = {}".format(
        cost, shipping, total))

    # return total cost
    return total

    
