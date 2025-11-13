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


