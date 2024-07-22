def canreachdestination (a,b,c,d,t): 
    #calculate the distance
    distance = abs(c-a) and abs(d-b)
    
    if t<distance: 
        print("Y")
        
    if t>distance: 
        print("N")
        
    else: 
        #Check if the difference is even
        if (t-distance)%2 == 0: 
            return("Y")
        if (t-distance)%2 == 1: 
            return("N")
        
        #If 𝑡>distance t>distance, check if (𝑡−distance)%2==0 (t−distance)%2==0. If true, return "Y", otherwise return "N"
        #to check if excess energy can be used without any remaining 