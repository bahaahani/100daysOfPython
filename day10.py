# function with output
def format_name():
    first_name = input("What is your first name? ").title()
    last_name = input("What is your last name? ").title()
    full_name = first_name + " " + last_name
    print(full_name)
    return full_name

format_name()

def format_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False