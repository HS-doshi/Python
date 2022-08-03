"""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).

"""

def computepay(h,r):
    
    if h>40:        
        p = (h-40)*r*1.5 + (40*r)
        
    else:
        p = h*r
        
    return p

hrs = input("Enter Hours:")
h=float(hrs)

rate = input("Enter Rate : ")
r=float(rate)

p = computepay(h,r)
print("Pay",p)
