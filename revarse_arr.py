def rev_arr(lis):
	#print(lis)
	start = 0
	end = len(lis) - 1
	while start <= end:
		lis[start],lis[end] = lis[end],lis[start]
		start = start + 1
		end = end - 1
	return lis	
	
lis = [1,2,3,4,5]		
print(f'before reversing list: {lis}')
print(f'after reversing list')
print(rev_arr(lis))

# time compaxity is linear big o of n --> o(n)
