# This is codility solution for Rotate an array to the right by a given number of steps.

def solution(A, K):
    
    K = K % len(A)
    if (len(A) == 0 or len(A) == 1 or K == 0):
        return A;
    else:
        return A[K:]+A[:K] 
    


    
l=[-5,100,11,14,16]
rotation=4
print solution(l,rotation)

