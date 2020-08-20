# Program displays the maximum and minimum value using for loop

#marks = [56,43,65,42,73, 51, 24]
#maxmark=marks[0]
#for i in marks:
    #if i>maxmark :
     #maxmark=i
#print(maxmark)
 
marks = [56,43,65,24,73, 51, 42]
minmark=marks[0]
maxmark=marks[0]
for i in marks:
    if i<minmark :
     minmark=i
    if i>maxmark  :
     maxmark=i
print(minmark)
print(maxmark)
print("Difference is ", maxmark-minmark)
 
