def print3largest(arr):
    arr_size = len(arr)
    
    # There should be atleast three elements
    if arr_size < 3:
        print("Invalid Input")
        return
    
    third = first = second = float('-inf')
    
    for i in range(arr_size):
        # If current element is greater than first
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        
        # If arr[i] is in between first and second then update second
        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]
        
        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]

    print("Three largest elements are", first, second, third)

def print2largest(arr, arr_size):

    # Sort the array in descending order
    arr.sort(reverse=True)

    # Start from second last element as first
    # element is the largest
    for i in range(1, arr_size):

        # If the element is not
        # equal to largest element
        if (arr[i] != arr[0]):
            print("The second largest element is", arr[i])
            return

    print("There is no second largest element")