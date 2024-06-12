DEGREE = "\u00B0"
SECONDS_PER_DEGREE = 60 * 60

def pad_zeroes(number):
    num_string = str(number)
    if len(num_string) < 2:
        return '0' + num_string
    else:
        return num_string

def dms(degrees_float):
    degrees_int = int(degrees_float)
    mins = int((degrees_float - degrees_int) * 60)
    secs = int((degrees_float - degrees_int - (mins / 60)) * SECONDS_PER_DEGREE)

    return (f"{degrees_int}{DEGREE}"
            f"{pad_zeroes(mins)}'"
            f'{pad_zeroes(secs)}"')
    
