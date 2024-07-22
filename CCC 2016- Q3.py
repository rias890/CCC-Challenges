#So we have a problem description which requires us to take in a string and determine the 
#maximum charcater amount of the palindromes within it 
# #how do we do this? 
# 1. Define a function (done)
# 2. Ensure that string lengths of one are equal to themself (done)
# 3. Must also create a current string. Why? 
# 4. Must check if the string 
# 4. Iterate through the string 
# 5. Print out the number of palindromes 


def longestPalindrome(s): 
    if len(s) == 1: 
        print(len(s))
    res = ""
    for i in range (len(s)): 
        for j in range (len(s)): 
            str = s[i : j+1]
            if isValid(str) and len(str)> len(res): 
                res = str 
    return len(res)

def isValid(s): 
    left = 0 
    right = len(s)-1 
    
    while left <= right: 
        if s[left] != s[right]: 
            return False 
        left += 1 
        right -= 1 
    return True 

s = input()
print(longestPalindrome(s))
            