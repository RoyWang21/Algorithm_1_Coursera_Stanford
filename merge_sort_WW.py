def merge(leftpart, rightpart):
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
		elif leftpart[i] < rightpart[j]:
			mergelst.append(leftpart[i])
			i += 1
		elif leftpart[i] >= rightpart[j]:
			mergelst.append(rightpart[j])
			j += 1
	print(f"mergelist = {mergelst}")
	return mergelst

def sort(lst): # recursively merge the sorted parts
	print(lst)
	if len(lst) < 2:
		return lst
	else:
		div = len(lst) // 2 # divide the lst in two halves, if the len(lst) is odd number, the left half is the smaller one
		return merge(sort(lst[0 : div]), sort(lst[div : ])) # merge the sorted parts, which come from merges

#--------------------------------------------------------------

unsorted = []

while True:
	temp = input("Input data, press space to end: ")
	if temp == " ":
		break
	else:
		unsorted.append(int(temp))

# Implement error return here, if the array has no number in it.
#if not unsorted: 
sorted = sort(unsorted)
print(sorted)
#else:
	#print("No data input!")


