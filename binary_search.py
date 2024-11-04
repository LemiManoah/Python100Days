#using Recursion


# def binary_search(arr, low, high, target ):
#     """
#     Implements binary search algorithm to find target in a sorted array.
#     """
#     if high >= low:
#         mid = (high + low) // 2
        
#         #if the target is the middle element of the array
#         if arr[mid] == target:
#             return mid
        
#         #if the target is smaller than the middle element of the array, then it exists in the low section  of the array
#         if arr[mid] > target:
#             return binary_search(arr, low, mid - 1, target)
        
#         #if the target is larger than the middle element of the array, then it exists in the high section of the array
#         else:
#             return binary_search(arr, mid + 1, high, target)
        
#     #if the target is not found in the array, return -1
#     else:
#         return -1

#test array
# arr = [ 2, 3, 4, 10, 40 ]
# target = 10
#function call
# result = binary_search(arr, 0, len(arr)-1, target);

# if result != -1:
#     print(f"the target value is present at index: {result}");
# else:
#     print("the target value index does not exist in the list");
    
 
 
 # Iterative Binary Search Function 
 # It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, target):
    #low is the leftmost index of array
    low= 0;
    #high is the rightmost index of array
    high = len(arr)-1;
    
    #initialize mid as the middle index of array
    mid= 0;
    
    #while low is less than or equal to high
    while low <= high:
        mid = (low + high)//2
    
        #check if target is less than target
        if arr[mid] > target:
            high = mid - 1;
        
        #check if target is more than target
        elif arr[mid] < target:
            low = mid + 1;
        
        #target is present at mid
        else:
            return mid;
        
    return -1;
      

# Test array
arr = [ 2, 3, 4, 10, 40 ]
target = 10
 
# Function call
result = binary_search(arr, target)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


            
   