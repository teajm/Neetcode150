import math
#generic array for testing binary searches.
test = {
        'inputs':{
            'nums': [-1,0,1,2,3,5,9,12],
            'target': 9
        }
        ,'output':{
            'position': 3
        }
}
#test for Koko eating bananas problem
testNanners ={
    'inputs':{
        'piles': [3,6,7,11],
        'h' : 4
    }
}
#test for 2D matrix problem
test2dMatrix ={
    'inputs':{
        'matrix': [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 
        'target': 34
    }
}
#test for find min in rotated array proble,
testFindMin ={
    'inputs':{
        'nums': [3,4,5,1,2]
    }
}



def brute_search(nums, target):
    #brute force search
    #position = 0
    print(nums)
    print(target)
    for i in range(0, len(nums)):
        
        if nums[i] == target:
            return i
            
        if i == len(nums):
            return -1

#************** EASY #**************
def binary_search(nums,target):
    #simple binary search!
    #need to find midpoint of the length of cards as starting check
    hi = len(nums) - 1
    lo = 0
    while hi >= lo:
        #find midpoint
        mid = (hi + lo ) // 2
        #work through cases
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            hi = mid - 1
        elif nums[mid] > target:
            lo = mid + 1
    #not found in array!
    return -1

#************** MEDIUM #**************


def rotated_binary_search(nums,target):
    #find a value in a given rotated binary array.
    #rotated means that the center is shifted in the array
    #by some number we don't know.
    #rotated looks like this: [3,4,5,1,2]
    #in numeric order, but not L-R across the array.
    #the zero point is shifted.

    # len(nums) - 1, because for ex list= [1,2,3,4], len(list) = 4, list(4) out of bounds.
    hi = len(nums) -1
    lo = 0
    while hi >= lo:
        #find midpoint
        mid = (hi + lo ) // 2
        #work through cases
        #target found. we're good.
        if nums[mid] == target:
            return mid
        #can't determine if rotation has happened or not? 
        if nums[lo] <= nums[mid]:
            #nums[lo] < target < nums[mid]
            if nums[lo] <= target <=nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] <= target <=nums[hi]:
                lo = mid + 1
            else:
                hi = mid -1
    #not found in array!
    return -1


def minEatingSpeed(piles, h):
        #n nanners, 
        #guards back in h hours.

        #piles is the lsit of bananas, ith pile has piles[i] bananas.

        #k = bananas per hour, every hour a pile is selected and k bananas are eaten.
        # if piles[i] has less than k bananas, piles[i] becomes 0.
        #find and return k such that she can eat all bananas in h hours.
        #piles = [3,6,7,11] 4 = 8
        # k = 4...  6 - 4 = 2, k = 1, 2 - 4 = 0, k = 2. done.
                    # 3 - 4 = 0 k = 3, done. 7 -4 , 3 - 4 k = ... etc.
    low = 0
    high = max(piles)
    while high >= low:
        k = (high + low) // 2
        if sum(math.ceil(1.0 * pile / k) for pile in piles) > h:
            low = k + 1
        else:
            high = k -1
    return low


def searchMatrix(matrix, target):
    #search a 2D matrix for a given val.
    #2d matrix is in order such that each the last element of a row 
    #is less than the first element of the next row
    #(in complete numeric order)
    ROWS,COL = len(matrix), len(matrix[0])
    top, bot = 0 , ROWS - 1
    #determine which row the value could possibly be in
    while bot >= top:
        #find midpoint
        mid = (top + bot) // 2
        #check the "mid" row's highest value to see if it's larger than it
        #if it's larger, shift the bottom to mid + 1
        if target > matrix[mid][COL - 1]:
            top = mid + 1
        #check the mid row's lowest value to see if it's smaller than it, 
        #if it is, shift the top down to the mid - 1
        elif target < matrix[mid][0]:
            bot = mid - 1
        #it's within these boundaries, break the loop.
        else:
            break


    if not (top <= bot):
        return False
        
    #now that we have the row, search the elements of the row!
    low, high = 0, COL - 1
    row = (top + bot ) // 2
    while low <= high:
        mid = (low + high) // 2
        #target found!
        if target == matrix[row][mid]:
            return True
        #mid is too high, move high to mid - 1
        elif target < matrix[row][mid]:
            high = mid - 1
        #mid is too low, move low to mid + 1
        elif target > matrix[row][mid]:
            low = mid + 1
        
    return False


def findMin(nums):
    #find minimum value in a rotated array.
    #rotated looks like this: [3,4,5,1,2]
    #in numeric order, but not L-R across the array.
    #the zero point is shifted.
        low = 0
        high = len(nums) - 1
        #set current min to inf to start.
        current_min = float("inf")
        #basic binary search stuff
        while low <= high:
            mid = (low + high) // 2
            #find the current minimum between nums and the prev current min.
            current_min = min(nums[mid],current_min)
            #end of the array is less than the middle,
            # means the minimum exists at the end of the array
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                #we've gone too far!
                high = mid - 1
            #find minimum between the last current min to compare L/R
        return min(current_min,nums[low])


#Printing functions for debug.
#print(brute_search(**test['inputs']) == test['output'])
#print(binary_search(**test['inputs']) == test['output'])
#print(rotated_binary_search(**test['inputs']) == test['output'])
# print(minEatingSpeed(**testNanners['inputs']))
# print(searchMatrix(**test2dMatrix['inputs']))
# print(findMin(**testFindMin['inputs']))
