#Q1. Maximum and minimum of an array using minimum number of comparisonsa

arr = [5, 2, 8, 1, 9, 3]

min_val = arr[0]
max_val = arr[0]

for i in range(1, len(arr)):
    current_element = arr[i]
    if current_element > max_val:
       max_val = current_element
    if current_element < min_val:
       min_val = current_element


print("Maximum value:", max_val)
print("Minimum value:", min_val)




# Q2. Array Reverse

arr = [10, 20, 30, 40, 50]
start = 0
end = len(arr) - 1

while(end > start):

   arr[start] , arr[end] = arr[end] , arr[start]

   start += 1
   end -= 1

print(arr)


# Q3. Maximum Subarray

arr = [2, -3, 4, -1, 5]

current_max = 0 
global_max = arr[0]

for i in range(len(arr)):
      current_max += arr[i]
      if current_max > global_max:
         global_max = current_max
      if current_max < 0:
         current_max = 0

print("Maximum Subarray Sum:", global_max)


# Q4. Contains Duplicate

arr = [1, 2, 3, 2, 5]

def contains_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False  

print(contains_duplicate(arr))



# Q5. Print all even numbers in an array

arr = [1,2,3,4,5,6]

even_list = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even_list.append(arr[i])

print(even_list)



# Q6.Print all odd numbers in an array

arr = [1,2,3,4,5,6,7]

odd_list = []

for i in range(len(arr)):
    if arr[i] % 2 != 0:
        odd_list.append(arr[i])

print(odd_list)


# 7.Find the Majority Element

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
def find_majority_element(arr):
    count = {}
    majority_count = len(arr) // 2

    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

        if count[num] > majority_count:
            return num

    return None

print(find_majority_element(arr))



# Q8. Longest Prefix that is also Suffix

arr = "ababcababc"

def longest_prefix_suffix(arr):
    n = len(arr)
    lps = [0] * n
    length = 0
    i = 1

    while i < n:
        if arr[i] == arr[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps[-1]

print(longest_prefix_suffix(arr))


#9 Check if an Array is Sorted (Non-decreasing)
arr = [1, 2, 3, 4, ]

is_sorted = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")


#10. Move all zeros to the end of the array
arr = [0, 1, 0, 3, 12]
non_zero_index = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[non_zero_index] = arr[i]
        non_zero_index += 1

while non_zero_index < len(arr):
    arr[non_zero_index] = 0
    non_zero_index += 1

print(arr)











     




