from unittest import result


count = 0 
while count <= 5:
  print (count)
  count = count + 1
print ('exit while loop\n')
print ('*' * 50)

# Program to find the factors of a number
val = int(input('\nEnter a number which you want a factor: '))
print ('The factors of ',val,' are: ')
for i in range(1, val+1):
  if val % i == 0:
    print (i, '\n')
print ('*' * 50)

# programme to check mean of a result
marks = { 'amit' : 90, 'ram' : 70, 'jadu' : 85, 'kumaar' : 55 }
print(f'The origianl dictionary(marks) is : \n {str(marks)}')
res = 0
for val in marks.values() :
  res+=val
res = res / len(marks)
print(f'Avarage marks is (the computed mean) is : {res} \n')
print ('*' * 50)

# Programme to Binary search on list
def binarySearch(arr, i, r, s) :

  while i <= r:
    mid = 1 + (r - 1) // 2

    # check if s is present at mid
    if arr[mid] == s:
      return mid
    # if s is greater ignore left half 
    elif arr[mid] < s:
      i = mid + 1

# if we reach here, then the element 
# was not present
  return -1

# Driver code
arr = [10,20,30,40,50]
s = 30

# Function call
result = binarySearch(arr, 0, len(arr) - 1, s)

if result != -1:
  print(f'Element {s} is present at index {result}')
else:
  print(f'Element is not present in array')