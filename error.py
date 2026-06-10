data = []
def safe_mean(data):
    try:
        return sum(data) / len(data)
    except ZeroDivisionError:
        print("The data list is empty. Cannot compute mean.")
        return None 
    except len(data) == 0:
        print("The data list is empty. Cannot compute mean.")
        return None 

    except TypeError:
        print("Data should be a list of numbers.")
        return None
    
    return sum(data) / len(data)

print(safe_mean(data))


