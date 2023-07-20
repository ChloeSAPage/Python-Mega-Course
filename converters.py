def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert (feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

def km_to_miles(km):
    return km / 1.6