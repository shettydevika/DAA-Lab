import time
from numpy.random import randint
import matplotlib.pyplot as plt

def mergesort(array):
    if len(array)>1:
       
        r=len(array)//2
        L=array[:r]
        M=array[r:]
        mergesort(L)
        mergesort(M)
        i=j=k=0
       
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=M[j]
                j+=1
            k+=1
           
        while i<len(L):
            array[k]  =L[i]
            i+=1
            k+=1
        while j<len(M):
            array[k]=M[j]
            j+=1
            k+=1
           
def partition(array,low,high):
    pivot=array[high]  
    i=low-1
    for j in range(low,high):
       if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1

def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
       
def selectionsort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step])

def read_input():
    a=[]      
    n=int(input("Enter the number of tv channels:"))
    print("enter the number of viewers:")
    for i in range(0,n):
        l=int(input())
        a.append(l)
               
    return a
elements=list()
times=list()
global labeldata
print("1.Merge sort 2. Quick sort 3. Selection sort")
ch=int(input("Enter the choice:"))
if(ch==1):
    array=read_input()
    mergesort(array)
    labeldata="Merge Sort"
    print("Sorted array is:")
    print(array)
elif ch==2:
    array=read_input()
    size=len(array)
    labeldata="Quick Sort"
    quicksort(array,0,size-1)
    print("Sorted array is:")
    print(array)
if(ch==3):
    array=read_input()
    size=len(array)
    labeldata="Selection sort"
    selectionsort(array,size)
    print("sorted array is")
    print(array)
print("-----------------Running time analysis------------------")
for i in range(1,11):
    array=randint(0,1000*i,1000*i)
    start=time.time()
    if ch==1:
        mergesort(array)
    elif ch==2:
        quicksort(array,0,size-1)
    else:
        size=len(array)
        selectionsort(array,size)
    end=time.time()
    print(len(array),"elements sorted by",labeldata,end-start)
    elements.append(len(array))
    times.append(end-start)
plt.xlabel('list length')
plt.ylabel('time complexity')
plt.plot(elements,times,label=labeldata)
plt.grid()
plt.legend()
plt.show()