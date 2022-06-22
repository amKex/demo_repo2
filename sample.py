count = 0 
while count <= 5:
  print (count)
  count = count + 1
print ('exit while loop\n')
print ('*' * 50)

#Program to find the factors of a number
val = int(input('\nEnter a number which you want a factor: '))
print ('The factors of ',val,' are: ')
for i in range(1, val+1):
  if val % i == 0:
    print (i)
print ('*' * 50)

#programme to check mean of a result
marks = { 'amit' : 90, 'ram' : 70, 'jadu' : 85, 'kumaar' : 55 }
print(f'The origianl dictionary(marks) is : \n {str(marks)}')
res = 0
for val in marks.values() :
  res+=val
res = res / len(marks)
print(f'Avarage marks is (the computed mean) is : {res}')
