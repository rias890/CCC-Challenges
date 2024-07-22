inputtime = input("Enter the time Fiona left (HH:MM): ")
rushhour = input("Is there rush hour? (yes/no): ")

# Split input time into hours and minutes
hours, minutes = map(int, inputtime.split(":"))

if rushhour == "no":
    # Non-rush hour: Add 2 hours to departure time
    hours += 2
    if hours >= 24:
        hours -= 24  # Wrap around if exceeding 24 hours
    
    # Print formatted arrival time
    print(f"{hours:02}:{minutes:02}")

elif rushhour == "yes":
    if (7 <= hours <= 10) or (15 <= hours <= 19):
        # Rush hour: Calculate arrival time with half-speed travel
        newhours = hours*1.5  # 1.5 times the normal hours
        if newhours >= 24:
            newhours -= 24  # Wrap around if exceeding 24 hours
        
        # Adjust minutes based on departure time
        if minutes == 0:
            minutes = 30
        elif minutes == 20:
            minutes = 0
        elif minutes == 40:
            minutes = 30
        
        # Print formatted arrival time
        print(f"{int(newhours):02}:{minutes:02}")

    else:
        print("Invalid input for rush hour. Please enter 'yes' or 'no'.")
else:
    print("Invalid input for rush hour. Please enter 'yes' or 'no'.")
