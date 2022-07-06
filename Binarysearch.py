from pyexpat import native_encoding
import random
import time

def linear_search(l,target):
    for i in range(len(l)):
        if(l[i]==target):
            return i
    return -1
def binary_search(l,target,low=None,high=None):
    if low==None:
        low=0
    if high==None:
        high=len(l)-1
    if high<low:
        return -1
    mid=(low+high)//2
    if(l[mid]==target):
        return mid
    elif(l[mid]>target):
        return binary_search(l,target,low,mid-1)
    else:
        return binary_search(l,target,mid+1,high)
if __name__=="__main__":
    #l=[1,2,3,4,5]
    #target=5
    length=1000
    sorted_list=set()
    while(len(sorted_list)<length):
        sorted_list.add(random.randint(-2*length,2*length))
    sorted_list=sorted(list(sorted_list))
    start=time.time()
    for target in sorted_list:
        linear_search(sorted_list,target)
    end=time.time()
    print("for linear search,time is ",(end-start)/length,"seconds")
    start=time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end=time.time()
    print("for binary search,time is ",(end-start)/length,"seconds")

