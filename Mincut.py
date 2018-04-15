import random
import sys

def find_rand_edge(G1):	
	temp = random.randint(1, (num - len(G1))) # Generate a rand among all edges in the 2d array G1
	row = 0
	for x in [len(y) - 1 for y in G1]: # run down rows of G1 (expect the first entry of each row (thus -1)) to find which vertices the chosen edge connects to
		temp -= x
		if temp <= 0:
			return [G1[row][0], G1[row][x + temp]] # the chosen edge connects to vertices as shown
		row += 1

def merge_vertices(G1,choice): # merge the vertices of v2 row into v1 row
	v1, v2 = int(choice[0]), int(choice[1])
	for z in range(G1[v1 - 1].count(v2)):			
		G1[v1 - 1].remove(v2) # remove the self-loop between v1 and v2 in v1 row

	for x in G1[v2 - 1]: # move the vertices in v2 row into v1 row
		if x != v1 and x != v2:
			#print(f"x = {x}, v1 = {v1}")
			G1[v1 - 1].append(x)
	G1[v2 - 1].clear() # remove v2 row except the header v2

	for y in range(len(G1)): # replace v2 with v1 in every row of G
		if v2 in G1[y]:
			for z in range(G1[y].count(v2)):			
				G1[y].remove(v2)
				G1[y].append(v1)
	G1[v2 - 1].append(v2)
	return G1

#--------------------------------------------------
mincut = sys.maxsize
G_original = []
temp = []

# with open('SampleCut.txt','r') as f:
with open('kargerMinCut.txt','r') as f:
	G_original=[x.strip().split('\t') for x in f] # The original file is separated by tab, need to parse it

for iter in range(50):

	G1 = [[int(num) for num in item] for item in G_original] # convert the matrix of CHAR to INT

	num = sum(len(x) for x in G1)

	left_len = [len(y) - 1 for y in G1]
	# print(G1)
	while left_len[2] > 0:
		num = sum(len(x) for x in G1)
		choice = find_rand_edge(G1)
		choice.sort()
		#print(f"  Choose: Vertex_1 = {choice[0]}, Vertex_2 = {choice[1]}")

		G1 = merge_vertices(G1, choice)

		left_len = [len(y) - 1 for y in G1]
		left_len.sort()
		left_len.reverse()

	print(f"-- Cut number for iteration {iter} = {left_len[0]}")

	if mincut > left_len[0]:
		mincut = left_len[0]

print(f"----- Mincut = {mincut}")