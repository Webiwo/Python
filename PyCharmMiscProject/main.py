# CODE FOR UNIT TESTING

def add_five_to_num(num=0):
    try:
        if num:
            return round(float(num), 2) + 5
        else:
            return "Enter a number"
    except ValueError as err:
        return err
