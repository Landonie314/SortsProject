# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:42:02 2022
source: geeksforgeeks.org

@author: Landon, Alvin, Aidan
"""
import random
import time
from tkinter import Tk # for copy to clipboard

RAND_FLOOR = 0
RAND_CEIL = 10000

RAND_LARGE_FLOOR = 10**50
RAND_LARGE_CEIL = 10**51

ARR_SIZES = (100, 1000, 10000)#, 100000)

def invokeTimed(func, *args):
    startTime = time.time()
    funcResult = func(*args)
    stopTime = time.time()
    return (stopTime - startTime, funcResult)
    

def bubbleSort(array):
    arr_copy = list(array)
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(arr_copy)-1, 0, -1):
        for i in range(n):
            if arr_copy[i] > arr_copy[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                arr_copy[i], arr_copy[i + 1] = arr_copy[i + 1], arr_copy[i]       
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            break
    return arr_copy
        
def selectionSort(arr):
    array = list(arr)
    size = len(arr)
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    return array
        
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
    for i in range(0,n):
        arr[i] = output[i]

# So, apparently, this radix implementation is
# directly translated from a C++ version of it available
# online. It's in the data structures project we did last year,
# almost verbatim. But because C++ is type safe and Python is not,
# max1/exp DOES NOT get rounded down to 0, and will continue to add digits
# until floating point becomes so imprecise that it defaults to 0.
 
# Method to do Radix Sort
def radixSort(array):
    arr = list(array)
    # Find the maximum number to know number of digits
    max1 = max(arr)
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1//exp > 0: # Kids, always remember: This is Python. Don't assume a type-safe paradigm.
        countingSort(arr,exp)
        exp *= 10
    return arr
        
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
 
def heapSort(array):
    arr = list(array)
    n = len(arr)
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 # One by one extract elements
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)
    return arr
        


#generate the arrays
def genArray(count,floor=RAND_FLOOR,ceil=RAND_CEIL):
    return [random.randint(floor,ceil) for i in range(count)]

print("Generating arrays...")
arrays_avg = [genArray(s) for s in ARR_SIZES]
# create sorted versions of all average arrays
arrays_sorted = [radixSort(a) for a in arrays_avg]
# create descending-order arrays from sorted versions
arrays_reversed = [list(a) for a in arrays_sorted]
for a in arrays_reversed: a.reverse()
# radix sort best/worst case arrays (single digits vs many digits)
arrays_small = [[j%10 for j in i] for i in arrays_avg]
arrays_large = [genArray(s,RAND_LARGE_FLOOR,RAND_LARGE_CEIL) for s in ARR_SIZES]
# heap sort best/worst case arrays (homogeneous vs completely heterogeneous)
arrays_distinct = [list(range(s)) for s in ARR_SIZES]
arrays_identical = [[random.randint(RAND_FLOOR,RAND_CEIL)]*s for s in ARR_SIZES]
print("Arrays generated.")


def copyToClipboard(content): # ol' reliable, stolen from the internet
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(content)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

# for excel formatting & best/worst case specification
sorts = [
    {
    'name': 'Bubble Sort',
    'func': bubbleSort,
    'best': arrays_sorted,
    'worst': arrays_reversed,
    'average': arrays_avg
    },
    {
    'name': 'Selection Sort',
    'func': selectionSort,
    'best': arrays_sorted,
    'worst': arrays_reversed,
    'average': arrays_avg
    },
    {
    'name': 'Radix Sort',
    'func': radixSort,
    'best': arrays_small,
    'worst': arrays_large,
    'average': arrays_avg
    },
    {
    'name': 'Heap Sort',
    'func': heapSort,
    'best': arrays_identical,
    'worst': arrays_distinct,
    'average': arrays_avg
    }
]

results = []
temp = []
for size in ARR_SIZES:
    temp.append("Average case ({0})".format(size))
    temp.append("Best case ({0})".format(size))
    temp.append("Worst case ({0})".format(size))
results.append('\t' + '\t'.join(temp))

for s in sorts:
    print('\n===',s['name'].upper(),'===\n')
    row_results = []
    row_results.append(s['name'])
    for i in range(len(ARR_SIZES)):
        for case in ('average', 'best', 'worst'):
            print("Timing {0} {1} case with {2} elements...".format(s['name'], case, ARR_SIZES[i]))
            elapsedTime = invokeTimed(s['func'], s[case][i])[0]
            row_results.append(str(elapsedTime))
            print("Elapsed time:", elapsedTime, "seconds\n")
    results.append('\t'.join(row_results))

final_result = '\n'.join(results)
print(final_result)
print('Writing to out.txt...')
with open('out.txt', 'w') as f:
    f.write(final_result)
print('Done!')
print('Also copying to clipboard...')
copyToClipboard(final_result)
print('Results copied to clipboard, can now be pasted to Excel.')
