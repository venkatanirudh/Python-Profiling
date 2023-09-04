"""
def leb_cal_2a(n):
    c=0                                       # Initializing sum
    for k in range(n+1):                      # Iterating from 0 to n
        if(k%2!=0):                           # To determine whether to sub or add 
            #print("Subtract at index",k)
            c-=1/((2*k)+1)                    
        else:
            #print("Add at index",k)
            c+=1/((2*k)+1)
    return(c)
n=int(input())
print(leb_cal_2a(n))
"""

def leibniz_formula(n):
    # Initializing sum
    t_sum = 0
    # Iterating from 0 to n
    for k in range (n+1):
        # Calculate each value using the formula
        val  = 1/((2*k)+1)
        # Determine whether k is even or odd before subtracting or adding.
        if(k%2 != 0):     # k is Odd, Subract
            t_sum -= val 
        else:             # k is Even, Add
            t_sum += val
    return t_sum

# Get user input for n
n=int(input("Enter the value of n: "))
# Display the result
print("Result : " ,leibniz_formula(n))
