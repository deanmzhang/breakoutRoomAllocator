#!/usr/bin/env python3
import numpy as np
import sys
from parse import *
from utils import *
import random

def generate_output(students):
	print(f'Given {students} students:')
	k = np.random.randint(1, students)

	# random S_max
	S_max = np.random.randint(20_000, 100_000) / 1000
	print(S_max)

	# make partitions
	fin = students
	partitions = []
	while fin > 3:
		iter_size = np.random.randint(1, (fin + 3) // 2)
		fin -= iter_size
		partitions.append(iter_size)

	partitions.append(fin)
	k = len(partitions)
	print(partitions)

	# max stress per room
	k_max = S_max / k
	print(k_max)

	worst_stress = 0
	best_stress = 101
	worst_happiness = 101
	best_happiness = 0
	# make list of stresses between every student in a partition
	rest_of_edges = 0

	partition_happiness = []
	partition_stress = []
	for p in partitions:
		s = 0
		l = []
		h = []
		for _ in range(p * (p - 1) // 2):
			n = np.random.randint(1_000, 99_000) / 1000 # why this
			s += n
			l.append(n)
			
			juul_pod = np.random.randint(20_000, 80_000) / 1000
			if worst_happiness > juul_pod:
				worst_happiness = juul_pod
			if best_happiness < juul_pod:
				best_happiness = juul_pod

			h.append(juul_pod)
		l = [el * k_max / s for el in l]
		
		for nigga in l:
			if worst_stress < nigga:
				worst_stress = nigga
			if best_stress > nigga:
				best_stress = nigga
		print(l) # list of stresses
		print(sum(l)) # about equal to k_max
		print(h)
		partition_stress.append(l)
		partition_happiness.append(h)
		rest_of_edges += len(l)
	
	print("Best Stress, Worst Stress: ", worst_stress, best_stress)
	
	total_edges = (students * (students - 1)) // 2
	
	rest_of_edges = total_edges - rest_of_edges
	
	rest_of_edge_tuples = []
	for _ in range(rest_of_edges):
		coin_flip = np.random.randint(0, 2)
		if coin_flip == 0:
			new_worst_stress = np.random.randint(worst_stress * 1000 * 1.1, 100_000) / 1000
			new_happiness = np.random.randint(best_happiness * 1000, best_happiness * 1000 * 1.6) / 1000
			rest_of_edge_tuples.append((new_worst_stress, new_happiness))
		else:
			new_best_stress = np.random.randint(best_stress * 0.2 * 1000, best_stress * 1.3 * 1000) / 1000
			new_happiness = np.random.randint(0, worst_happiness * 1000 * 0.8) / 1000
			rest_of_edge_tuples.append((new_best_stress, new_happiness))
	print(rest_of_edge_tuples)

	
	permute = np.array([i for i in range(students)])
	np.random.shuffle(permute)

	it = 0

	fill_it_in = [["X" for j in range(students)] for i in range(students)]
	
	ans = []
	for i in range(len(partitions)):
		num_students = partitions[i]
		s = partition_stress[i]
		h = partition_happiness[i]
		con_students = []
		for j in range(num_students):
			con_students.append(permute[it])
			it += 1
		con_students.sort()

		nut = 0		
		for j in range(len(con_students)):
			for k in range(j + 1, len(con_students)):
				print(con_students[j], con_students[k])
				q = "{0} {1} {2} {3}".format(con_students[j], con_students[k], h[nut], '%.3f' % s[nut])
				ans.append(q)
				fill_it_in[con_students[j]][con_students[k]] = q
				nut += 1
		print(ans)
		print(con_students)

	errthing = 0
	for i in range(students):
		for j in range(i + 1, students):
			print(i, j, fill_it_in[i][j])
			if fill_it_in[i][j] == "X":
				yy, yu = rest_of_edge_tuples[errthing]	
				last_str = "{0} {1} {2} {3}".format(i, j, yu, yy)
				fill_it_in[i][j] = last_str 
				errthing += 1

	f = open("input" + str(students) + ".txt", "w")
	print(str(S_max))
	f.write(str(students) + "\n")
	f.write(str(S_max + 1) + "\n")
	for i in range(students):
		for j in range(i + 1, students):
			print(i, j, fill_it_in[i][j])
			f.write(fill_it_in[i][j] + "\n")
	f.close()
	
	
	return students

def main():
	generate_output(10)
	generate_output(20)
	generate_output(50)

if __name__ == '__main__':
	main()
