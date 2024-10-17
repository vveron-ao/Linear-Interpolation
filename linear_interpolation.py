#The purpose of the program will predict where the ISS is above earth at any given time through linear interpolation.
#Below is part 1 of the linear interpolation program. 
#We calculated the slope and y-intercept to result in the formula for p (ISS distance from Houston). 
#This formula can be used to find the value of p at any given time (t).

#Below are the defined variables, using these variables we can calculate the slope. (For users' reference.)
# t = 10, p = 2,028 kilometers
# t = 55, p = 23,028 kilometers

from math import *
#Assign the t variable a value of 25. This represents the position at time of 25 minutes.
t = 25

#The formula to calculate the (p) value to determine where the ISS is above Earth at any given time.
p = (1400 / 3) * t + (23028 - (1400 / 3) * 55)

#We are printing the desired output when the position is at a time of 25 minutes.
print("Part 1: ")
print(f"For t = {t} minutes, the position p = {p} kilometers")

#Below is part 2 of the linear interpolation program. 
#This part of the program will determine the value of t at 300 minutes which is the distance from Houston.
#We used the linear equation from part one.
t = 300
p = (1400 / 3) * t + (23028 - (1400 / 3) * 55)

#Find circumference using the radius of 6745 km.
c = 2 * pi * 6745

#To avoid finding the total distance traveled we use % to find the distance the ISS is from Houston.
#Find the distance from Houston by using modulo division to get the remainder.
p = p % c

#The desired output for when time is at 300 minutes coming from Houston.
print("Part 2: ")
print(f"For t = {t} minutes, the position p = {p} kilometers")

#End program: Linear Interpolation.