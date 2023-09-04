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
