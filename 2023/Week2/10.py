# See the Week 3 question sheet
def fluid_flow_mode(speed, length, viscosity, flow_situation):
    """
    (float, float, float, str)->str
    Returns the mode of the flow based on the calculation of the Reynolds number
    """
    # Calculate Reynolds Number
    reynolds = speed * length / viscosity
    
    # Find flow mode
    if flow_situation == "pipe":
        
        if reynolds < 2000:
            mode = "laminar"
        elif reynolds <= 4000:
            mode = "transitional"
        else:
            mode = "turbulent"
            
    else:
        if reynolds < 500000:
            mode = "laminar"
        else:
            mode = "turbulent"
    
    return mode

# An alternative implementation
def fluid_flow_mode_alt(speed, length, viscosity, flow_situation):
    """
    (float, float, float, str)->str
    Returns the mode of the flow based on the calculation of the Reynolds number
    """

    # calculate Reynolds number
    reynolds_num = (speed * length) / viscosity

    mode = "turbulent"
    
    # find flow mode
    if flow_situation == "pipe":
        
        if reynolds_num < 2000:
            mode = "laminar" 
        elif reynolds_num <= 4000:
            mode = "transitional"
            
    else:
        
        # flow_situation == plate
        if reynolds_num < 5e5:
            mode = "laminar"
    
    # Bonus question: why do we not need else statements in the nested ifs?
    return mode


speed = 13.4
length = 800
viscosity = 1.2
flow_sit = "pipe"

print(fluid_flow_mode(speed, length, viscosity, flow_sit))
print(fluid_flow_mode_alt(speed, length, viscosity, flow_sit))