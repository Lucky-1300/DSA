
## 🟢 50 Easy DSA Array Questions

### 1. Basic Traversal

# 1. Print all elements of an array.
# arr = [5, 6, 2, 3]
# print(arr)
# 2. Print the array in reverse order.
# arr = [5, 6, 2, 3]
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i], end=" ")

# 3. Find the length of an array without using a built-in length function.
# arr = [5, 6, 2]
# count = 0
# for i in range(len(arr)):
#     count += 1
# print(count)
    
# 4. Find the sum of all elements in an array.
# arr = [5, 6, 2, 3]
# sum = 0
# for i in range(len(arr)):
#     sum = sum + arr[i]
# print(sum)
    
# 5. Find the average of all elements in an array.
# arr = [10, 20, 30]
# count = 0
# sum = 0
# for i in range(len(arr)):
#     count += 1
#     sum += arr[i]
#     average = (sum//count)
# print(average)



### 2. Maximum & Minimum


# 6. Find the largest element in an array.
# arr = [5, 9, 2, 7,-1]
# max = arr[0]
# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
# print(max)

# 7. Find the smallest element in an array.
# arr = [5, 9, 2, 7,-1]
# min = arr[0]
# for i in range(len(arr)):
#     if arr[i] < min:
#         min = arr[i]
# print(min)
# 8. Find the second largest element in an array.
# arr = [5, 9, 2, 7]
# max = arr[0]
# sec_max = arr[0]
# for i in range(1,len(arr)):
#     if arr[i] > max:
#         sec_max = max
#         max = arr[i]
#     elif arr[i] > sec_max and arr[i] != sec_max:
#         sec_max = arr[i]
# print(sec_max)
# 9. Find the second smallest element in an array.
# arr = [5, 9, 2, 7]
# min = arr[0]
# sec_min = arr[0]
# for i in range(1,len(arr)):
#     if arr[i] < min:
#         sec_min = min
#         min = arr[i]
#     elif arr[i] < sec_min and arr[i] != sec_min:
#         sec_min = arr[i]
# print(sec_min)
# 10. Find the difference between the maximum and minimum elements.
# arr = [5, 9, 2, 7]

# min = arr[0]
# max = arr[0]
# for i in range(1,len(arr)):
#     if arr[i] > max:
#         max = arr[i]
#     if arr[i] < min:
#         min = arr[i]
            
# print(max-min)
    

### 3. Even & Odd

# 11. Count the number of even elements.
# arr = [1, 2, 4, 7, 8]
# count = 0
# for i in range(len(arr)):
#     if arr[i] % 2==0:
#         count+=1
# print(count)
# 12. Count the number of odd elements.
# arr = [1, 2, 4, 7, 8]
# count = 0
# for i in range(len(arr)):
#     if arr[i] % 2!=0:
#         count+=1
# print(count)
# 13. Print all even elements.
# arr = [1, 2, 4, 7, 8]

# for i in range(len(arr)):
#     if arr[i] % 2==0:
#         print(arr[i],end=" ")
        

# 14. Print all odd elements.
# arr = [1, 2, 4, 7, 8]

# for i in range(len(arr)):
#     if arr[i] % 2!=0:
#         print(arr[i],end=" ")

# 15. Find the sum of all even elements.
# arr = [1, 2, 4, 7, 8]
# sum = 0
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         sum += arr[i]
# print(sum)
# 16. Find the sum of all odd elements.
# arr = [1, 2, 4, 7, 8]
# sum = 0
# for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#         sum += arr[i]
# print(sum)

### 4. Positive & Negative

# 17. Count positive numbers in an array.
# arr = [-2, 5, -7, 8, 3]
# count = 0
# for i in range(len(arr)):
#     if arr[i] > 0:
#         count += 1
# print(count)

# 18. Count negative numbers in an array.
# arr = [-2, 5, -7, 8, 3]
# count = 0
# for i in range(len(arr)):
#     if arr[i] < 0:
#         count += 1
# print(count)

# 19. Count zeros in an array.
# arr = [0, 5, 0, 2, 0]
# count = 0
# for i in range(len(arr)):
#     if arr[i] == 0:
#         count+=1
# print(count)

# 20. Print all positive numbers.
# arr = [-2, 5, -7, 8, 3]
# for i in range(len(arr)):
#     if arr[i] > 0:
#         print(arr[i],end=" ")
# 21. Print all negative numbers.
# arr = [-2, 5, -7, 8, 3]
# for i in range(len(arr)):
#     if arr[i] < 0:
#         print(arr[i],end=" ")

# 22. Find the sum of positive numbers.
# arr = [-2, 5, -7, 8, 3]
# sum = 0
# for i in range(len(arr)):
#     if arr[i] > 0:
#         sum += arr[i]
# print(sum)
# 23. Find the sum of negative numbers.
# arr = [-2, 5, -7, 8, 3]
# sum = 0
# for i in range(len(arr)):
#     if arr[i] < 0:
#         sum += arr[i]
# print(sum)

### 5. Searching

# 24. Search for a given element in an array.
# arr = [5, 8, 2, 9]
# target = 8
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found")
# 25. Find the index of a given element.
# arr = [5, 8, 2, 9]
# target = 2
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)
        
# 26. Find the first occurrence of an element.
# arr = [5, 2, 8, 2, 9]
# target = 2
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)
#         break

# 27. Find the last occurrence of an element.
# arr = [5, 2, 8, 2, 9]
# target = 2
# last = -1
# for i in range(len(arr)):
#     if arr[i] == target:
#         last = i
# print(last)


        
# 28. Count how many times a given element occurs.
# arr = [2, 5, 2, 8, 2]
# count = 0
# target = 2
# for i in range(len(arr)):
#     if arr[i] == target:
#         count += 1
# print(count)
# 29. Check whether an array contains a particular element.
# arr = [5, 8, 2, 9]
# target  =  7
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found")
#     else:
#        print("not found")
#        break

### 6. Reverse & Swap

# 30. Reverse an array without using a built-in reverse function.
# arr = [1, 2, 3, 4, 5]

# for i in range(len(arr)-1,-1,-1):
#     print(arr[i],end=" ")



# 31. Swap the first and last elements of an array.
# 32. Swap two given positions in an array.
# 33. Reverse the first half of an array.
# 34. Reverse the second half of an array.

### 7. Duplicates

# 35. Find duplicate elements in an array.
# arr = [1, 2, 3, 2, 4, 1]
# for i in range(len(arr)):
#     if arr[i] == arr[i]:
#         print(arr[i])
        
# 36. Count duplicate elements.
# 37. Remove duplicate elements from an array.
# 38. Check whether an array contains duplicates.
# 39. Find the first repeating element.

### 8. Sorting Basics

# 40. Sort an array in ascending order without using a built-in sorting function.
# arr = [5, 2, 8, 1, 3]

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]
# print(arr)

# 41. Sort an array in descending order without using a built-in sorting function.
# arr = [5, 2, 8, 1, 3]

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] < arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]
# print(arr)
# 42. Find the smallest element after sorting.
# arr = [5, 2, 8, 1, 3]


# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]
# # print(arr)
# min = arr[0]
# print(min)
        
    

# 43. Find the largest element after sorting.
# arr = [5, 2, 8, 1, 3]


# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]
# # print(arr)
# max = arr[-1]
# print(max)
# 44. Find the second largest element using sorting.
# arr = [5, 2, 8, 1, 3]


# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]
# # print(arr)
# max = arr[-2]
# print(max)

### 9. Simple Array Manipulation

# 45. Insert an element at a given position.
# arr=[1, 2, 4, 5]
# position= 2
# element= 3
# for i in range(len(arr)):
#     arr[2] = 3
# print(arr)
# 46. Delete an element from a given position.
# 47. Move all zeros to the end of the array.
# 48. Move all negative numbers to the beginning of the array.

# 49. Merge two arrays into one array.
# 50. Find the common elements between two arrays.
