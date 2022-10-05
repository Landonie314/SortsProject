# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:42:02 2022
source: geeksforgeeks.org

@author: Landon, Alvin, Aidan
"""
import numpy as np
import random
import time

RAND_FLOOR = 0
RAND_CEIL = 10

def invokeTimed(func, *args):
    startTime = time.time()
    funcResult = func(*args)
    stopTime = time.time()
    return (stopTime - startTime, funcResult)
    

def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]       
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return
        
def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])    
        
        #used for radix sort
def countingSort(arr, exp1):
    n = len(arr)
    # The output array elements that will have sorted arr
    output = [0] * (n)
    # initialize count array as 0
    count = [0] * (10)
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i]/exp1)
        count[int((index)%10)] += 1
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]
    # Build the output array
    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[ int((index)%10) ] - 1] = arr[i]
        count[int((index)%10)] -= 1
        i -= 1
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
        
        #used for heap sort
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 # See if left child of root exists and is
 # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 # See if right child of root exists and is
 # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 # Change root, if needed
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
  # Heapify the root.
        heapify(arr, n, largest)
# The main function to sort an array of given size
 
def heapSort(arr):
    n = len(arr)
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 # One by one extract elements
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)
        

#generate the arrays
array100 = np.random.randint(RAND_FLOOR,RAND_CEIL,100)
array1000 = np.random.randint(RAND_FLOOR,RAND_CEIL,1000)
array10000 = np.random.randint(RAND_FLOOR,RAND_CEIL,10000)
array100000 = np.random.randint(RAND_FLOOR,RAND_CEIL,100000)

    
print (array100)
    
