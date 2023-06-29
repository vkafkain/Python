def main():
    time = input("What time is it?")
    numericTime = convert(time)
    
    if numericTime >= 7 and numericTime <= 8:
        print("breackfast time!") 
    elif numericTime >=12 and numericTime <= 13:
        print("lunch time!")
    elif numericTime >= 18 and numericTime <= 19:
        print("dinner time!")

def convert(time):
    hours, minutes = time.split(":") 
    result = (int(hours) + int(minutes)/60)
    return result   

main()