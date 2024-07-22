N = int(input("Enter a n"))

k = int(input("Enter a k"))

list = []

counter = 0

if 1 <= N <= 10000 and 0 <= k <= 5:
    while counter<=k:
        w = x = 10**(k-counter)*N
        list.append(w)
        counter = counter+1
        
        
    sum = sum(list)
    print(sum)

  

        
    