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