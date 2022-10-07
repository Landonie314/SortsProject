# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:42:02 2022
source: geeksforgeeks.org

@author: Landon, Alvin, Aidan
"""
import random
from datetime import datetime as dt
from tkinter import Tk # for copy to clipboard

RAND_FLOOR = 0
RAND_CEIL = 10000

RAND_LARGE_FLOOR = 10**50
RAND_LARGE_CEIL = 10**51

ARR_SIZES = (100, 1000, 10000)#, 100000)

def invokeTimed(func, *args):
    startTime = dt.now()
    funcResult = func(*args)
    stopTime = dt.now()
    elapsed = stopTime - startTime
    return (elapsed.total_seconds(), funcResult)
    

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
        
#merge sort
def mergeSort(array):
    arr = list(array)
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        L = mergeSort(L)
 
        # Sorting the second half
        R = mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
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
# merge sort worst case array, i think??? this is stupid
arrays_max_compare = [[i%(n+1) for i in range(0,(n+2)*(n+1)//2,(n+2)//2)][:n] for n in ARR_SIZES]
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
    'name': 'Merge Sort',
    'func': mergeSort,
    'best': arrays_sorted,
    'worst': arrays_max_compare, # ?????
    'average': arrays_avg
    }
]

results = []
cases = ("best", "average", "worst")

for i in range(len(ARR_SIZES)):
    table = [str(ARR_SIZES[i])+"\t"+'\t'.join([c.capitalize() for c in cases])]
    print('\n=== N={0} ===\n'.format(ARR_SIZES[i]))
    for s in sorts:
        print(s['name'].upper())
        row_results = []
        row_results.append(s['name'])
        for case in cases:
            print("Timing {0} {1} case with {2} elements...".format(s['name'], case, ARR_SIZES[i]))
            elapsedTime = invokeTimed(s['func'], s[case][i])[0]
            row_results.append(str(elapsedTime))
            print("Elapsed time:", elapsedTime, "seconds\n")
        table.append('\t'.join(row_results))
    results.append('\n'.join(table))

final_result = '\n\n'.join(results)
print(final_result)
print('Writing to out.txt...')
with open('out.txt', 'w') as f:
    f.write(final_result)
print('Done!')
print('Also copying to clipboard...')
copyToClipboard(final_result)
print('Results copied to clipboard, can now be pasted to Excel.')
