#This program creates a function called generate which generates  list of 3x3 matrices which cycle between null (x) and not null (0 or 1) components.
#----------
#Variables: (list variables and what they do here)
#NoM: Number Of Matrices you which to create
#system: a list conatining all of the matrices
#row: a variable whose numerical value dictates which row of the matrix you are on
#column: a variable whose numerical value dictates which column of the matrix you are on
#number_one: counts the number of elements in the matrix that have the value of 1

## Jonas adds a new random comment
 #adding new stuff again (2)
#----------
#Updates: (When people edit the code make a note here)
#28/01/20 (12:22)(Greg): I have created this program
#28/01/20 (12;56)(Greg): This program now generates NoM number of 3x3 matrices whose elements are only 0
#28/01/20 (13:17)(Greg): this program now generates NoM number of 3x3 matrices whose elements alternate between 0 and x 
#28/01/20 (15:55)(Greg): this program now generates NoM number of 3x3 matrices whose elements alternate between 0/1 and x such there are only ever two 1's 
#-----------
#Tasks:


import numpy as np
import random

def generate(NoM):
    system=[]
    for count in range(0,NoM):
        matrix=[]
        number_one=0                    # counts the number of 1's in the matrix
        for row in range (0,3):         # this loop generates each row of our matrix
            matrix.append([])           # creates a blank row
            for column in range (0,3):  # this loop appends either 0 or x to our rows (ie creates the columns)
                if column ==0:  
                    if row==0:
                        element=random.randint(0,1)         #__________________________
                        matrix[row].append(element)         # this places a 0 in the top left most corner
                        if element == 1:
                            number_one=number_one+1
                    else:
                        if matrix[row-1][column] !="x":     # this section calculates the value for the first element in each column by
                            matrix[row].append("x")         # looking at the element above it ans swapping it (ie x -> 0 an 0 -> x)
                        else:
                            if number_one <= 1:             
                                element=random.randint(0,1)
                                if element==1:
                                    number_one=number_one+1
                            else:
                                element=0
                            matrix[row].append(element)     #__________________________
                else:                                       # this section calculates the value of the other elements by looking at the element
                    if matrix[row][column-1] !="x":         # in the column to the left and alternating it (ie x -> 0 an 0 -> x)
                        matrix[row].append("x")
                    else:
                        if number_one <= 1:
                            element=random.randint(0,1)
                            if element==1:
                                number_one=number_one+1
                        else:
                            element=0
                        matrix[row].append(element)          #__________________________  
        if number_one == 0:
            matrix[2][0]=1                                   # this section here converts the last two elements into 1's or the final element into  
            matrix[2][2]=1                                   # a 1 if there are not a total of two elements labelled one in the matrix
        if number_one == 1:
            matrix[2][2]=1
        system.append(matrix)                                # this then appends our 3x3 matrix to the list of matrices
    return system 

#This piece of code appears twice. The first section says that if we have not reached the maximum number of 1's per matrix then it randomly generates 
# the next element. If this element is a 1 it adds one to a count so that we can keep track of the number of 1s to make sure we only have two in the 
# matrix. If we have reached the maximum number of 1's then it sets the next element to 0

#if number_one <= 1:
    #element=random.randint(0,1)
    #if element==1:
        #number_one=number_one+1
#else:
    #element=0
#matrix[row].append(element)    
