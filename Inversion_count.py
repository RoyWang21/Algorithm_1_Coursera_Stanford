def count(A):
	if len(A) == 1:
		return A, 0
	else:
		div = len(A) // 2
		mergedleft, x = count(A[0 : div])
		mergedright, y = count(A[div :])
		mergedboth, z = SplitInv(mergedleft + mergedright, len(A))
		return mergedboth, x + y + z

def SplitInv(A, n):
	leftpart = A[: n // 2]
	rightpart = A[n // 2 :]
	Inv = 0
	print(f"leftpart = {leftpart}, rightpart = {rightpart}.")
	mergelst = []
	i = 0
	j = 0
	for k in range(len(leftpart) + len(rightpart)):
		if i == len(leftpart): # when the left part is entirely sorted in mergelst, append the rest of the rightpart in mergelst
			mergelst.extend(rightpart[j:])
			break
		elif j == len(rightpart): # when the right part is entirely sorted in mergelst, append the rest of the leftpart in mergelst
			mergelst.extend(leftpart[i:])
			break
		elif leftpart[i] < rightpart[j]: # when the element i in leftpart is smaller and get inserted in mergelst
			mergelst.append(leftpart[i])
			i += 1
		elif leftpart[i] >= rightpart[j]: # when the element j in rightpart is smaller and get inserted in mergelst
			mergelst.append(rightpart[j])
			j += 1
			Inv += len(leftpart) - i
			print(f"Inversion = {Inv}")
	print(f"mergelist = {mergelst}")
	return mergelst, Inv

#----------------------------------------------

unsorted = []

#with open('IntegerArray.txt') as file:
#    for line in file:
#        unsorted.append(int(line))

while True:
	temp = input("Input data, press space to end: ")
	if temp == " ":
		break
	else:
		unsorted.append(int(temp))

sortedlst, Inv = count(unsorted)
print(f"The count of inversion for {unsorted} is {Inv}.")
