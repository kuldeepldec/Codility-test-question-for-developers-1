# This is codility solution for finding zeros in binary representation of an integer
# with 1 in both sides of a binary gap

alist=[]        #declaring list
def solution(N):    #function for binary to decimal
    while(True):
        remi=N%2
        qut=N//2
        if (qut==0):
            alist.append(1)
            alist.reverse()
            break
        alist.append(int(remi))   
        N=qut    
   
    count = 0
    prev = 0
    count2=0
    for i in range(0,len(alist)): #reading list and finding binary gap
       
        if alist[i]==1:
            count2=count2+1
       
        if count2>0 and alist[i] == 0:
            count += 1
           
        if count>0 and count>prev and alist[i]==1:
            prev=count
            count=0
     
        if count>0 and alist[i]==1:
            count=0
        
    
    return prev

print solution(51712)
