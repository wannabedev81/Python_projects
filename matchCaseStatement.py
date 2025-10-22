## usecase of this technique: 
## to make long if statements more readable

def month_of_the_year(month):
    match month:
        case 1: 
            return "It is January"
        case 2: 
            return "It is February"
        case 3: 
            return "It is March"
        case 4: 
            return "It is April"
        case 5: 
            return "It is May"
        case _:
            return "no valid month"
    
print(month_of_the_year(3))

def is_autumn(month):
    match month:
        case "September" | "October" | "November":  ## | represents OR selector
            return True
        case "January":
            return False
        case _:
            return False
print(is_autumn("October"))
print(is_autumn("April"))


