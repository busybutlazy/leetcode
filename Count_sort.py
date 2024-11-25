

def counting_sort(arr):
    # Initialize count array with zeros
    count = [0] * 101  # since the range is 0 to 100

    # Count occurrences of each element in the input array
    for num in arr:
        count[num] += 1
    print(count)
    # Modify count array to store the actual position of elements
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    print("after sum",count)
    # Create the output array
    output = [0] * len(arr)

    # Build the output array
    for num in arr:
        print("num=",num)
        print("count[num] - 1=",count[num] - 1)

        
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1, 5, 10, 0, 100]
arr=[1,1,4,2,1,3]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)