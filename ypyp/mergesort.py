def merge(L):
	print('splitting the list would give',L)
	if len(L) > 1:
		m = len(L)//2
		left = L[:m]
		right = L[m:]

		merge(left)
		merge(right)
		i = 0
		j = 0
		k = 0

		while i<len(left) and j<len(right):
			if left[i] <= right[j]:
				L[k] = left[i]
				i = i+1
			else:
				L[k] = right[j]
				j = j+1
			k = k+1
		while i<len(left):
			L[k] = left[i]
			i = i+1
			k = k+1
		while j<len(right):
			L[k] = right[j]
			j = j+1
			k = k+1
		print('merging the list would give ',L)

L = [2,5,7,4]
merge(L)
print(L)
