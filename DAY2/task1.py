#Python program to compute compound interest
 
p = float(input("Enter the principal amount : "))
 
t = float(input("Enter the number of years : "))
 
r = float(input("Enter the rate of interest : "))
 
ci =  p * (pow((1 + r / 100), t)) 
 
print("Compound interest : {}",ci)