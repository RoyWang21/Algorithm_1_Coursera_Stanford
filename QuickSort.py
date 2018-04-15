def sort(A, n, comp):
	if n == 1:
		return A, comp
	elif n == 0:
		return [], comp
	else:
		comp += n - 1 # compute the # of comparisons at the current sort, as n - 1
		A, p = choosepivot(A, n) # choose the pivot
		A, i = partition(A, n) # move the pivot to the rightful position i

		# print(f"sort left: {A[ : i - 1]}")
		C, comp = sort(A[: i - 1], i - 1, comp) # recursively sort the left part, keep tracking of comp

		# print(f"sort right: {A[i : n]}")
		D, comp = sort(A[i : n], n - i, comp) # sort the right part

		# print(f"C = {C}; D = {D}\n")
		return C + [p] + D, comp # concat the lists together.

def choosepivot(A, n):

	## Method 1: Always choose the first item as pivot:
	# p = A[0]

	## Method 2: Always choose the final item as pivot:
	# p = A[n - 1]
	# A[0], A[n - 1] = A[n - 1], A[0]

	## Method 3: Choose median of three items (first, mid, final) as pivot
	Medianlst = [A[0], A[n - 1], A[(n + 1) // 2 - 1]]
	p = sorted(Medianlst)[1]
	if p == A[n - 1]:
		A[0], A[n - 1] = A[n - 1], A[0]
	elif p == A[(n + 1) // 2 - 1]:
		A[0], A[(n + 1) // 2 - 1] = A[(n + 1) // 2 - 1], A[0]

	return A, p

def partition(A, n):
	p = A[0]
	i = 1
	for j in range(0, n):
		if A[j] < p:
			A[j], A[i] = A[i], A[j]
			i += 1
	A[0], A[i - 1] = A[i - 1], A[0]
	# print(f"A = {A}; p = {p}; i = {i}")
	return A, i

#----------------------------------------------------------


unsorted = []

# while True:
# 	temp = input("Input data, press space to end: ")
# 	if temp == " ":
# 		break
# 	else:
# 		unsorted.append(int(temp))

with open('QuickSort.txt') as file:
   for line in file:
       unsorted.append(int(line))

comp = 0
sorted, comp = sort(unsorted, len(unsorted), comp)
print(sorted, f"comparisons = {comp}")