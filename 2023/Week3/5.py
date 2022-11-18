# Water exists in three states - solid, liquid, and gaseous. 
# Based on the temperature of the water given as an integer in the input, 
# determine the state of water. The temperature will be given in 
# Celsius degrees.

def water_phase_1(temp):
    '''
    (number) -> string
    Returns a string corresponding to the state of water at temp degrees
    celsius
    '''
    if temp > 100:
        return "Steam"
    elif temp > 0:
        return "Liquid"
    else:
        return "Ice, ice, baby"
    
def water_phase_2(temp):
    '''
    (number) -> string
    Returns a string corresponding to the state of water at temp degrees
    celsius
    '''
    
    if temp <= 0:
        return "Ice, ice, baby"
    elif degrees <= 100:
        return "Liquid"
    else:
        return "Steam"

def water_phase_3(temp):
    '''
    (number) -> string
    Returns a string corresponding to the state of water at temp degrees
    celsius
    '''
    
    state = "Ice, ice, baby"
    if degrees > 100:
        state = "Steam"
    elif degrees > 0:
        state = "Liquid"
    # why don't I need an else?
    
    return state
    

degrees = int(input("Enter a temperature in Celsius: "))

print(water_phase_1(degrees))
print(water_phase_2(degrees))
print(water_phase_3(degrees))
