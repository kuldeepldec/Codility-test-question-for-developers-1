# This is codility solution for finding Find value that occurs in odd number of elements

from collections import Counter

def solution(seq):
    c=Counter(seq)   #forming a dictionary
    for key, value in c.items(): #calculating odd value in an array and returning key
        if value%2==1:
            return key
            
     
    

   
l = [9,3,9,3,9,7,9]

print solution(l)

