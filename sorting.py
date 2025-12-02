# arr = [2,4,3,1]
# n = len(arr)
# for i in range(n):
#     for j in range(0,n - i - 1):
#         if arr[j] > arr[j +1]:
#             arr[j], arr[j +1] = arr[j +1],arr[j]
    

# print(arr)


# def bubble_sort(arr):
#     # Get the number of elements in the list
#     n = len(arr)

#     # Outer loop runs 'n' times (one pass per element)
#     for i in range(n):

#         # Inner loop: compare each pair of adjacent items
#         # The range gets smaller each pass because the largest
#         # elements settle at the end of the list
#         for j in range(0, n - i - 1):

#             # Compare the current element with the next element
#             if arr[j] > arr[j + 1]:

#                 # Swap them if they are in the wrong order
#                 # Python allows swapping in a single line
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

#     # Return the sorted list
#     return arr


# # Test the function
# print(bubble_sort([5, 2, 9, 1, 5, 6]))








# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i] ,arr[min_index] = arr[min_index],arr[i]
#     return arr
# print(selection_sort([5, 2, 9, 1, 5, 6]))

