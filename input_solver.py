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
	#print(S_max)

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
	#print(k_max)

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
		# l is the list of stresses, h is the list of happinesses
		l = []
		h = []
		for _ in range(p * (p - 1) // 2):
			n = np.random.randint(1_000, 99_000) / 1000 # why this
			s += n
			l.append(n)

			happiness = np.random.randint(20_000, 80_000) / 1000
		# Find the worst and best happiness in a breakout room
			if worst_happiness > happiness:
				worst_happiness = happiness
			if best_happiness < happiness:
				best_happiness = happiness

			h.append(happiness)
		l = [el * k_max / s for el in l]

		# Find the worst and best stress in a breakout room
		for stress in l:
			if worst_stress < stress:
				worst_stress = stress
			if best_stress > stress:
				best_stress = stress
		#print(l) # list of stresses
		#print(sum(l)) # about equal to k_max
		#print(h)
		partition_stress.append(l)
		partition_happiness.append(h)
		rest_of_edges += len(l) # right now, this represents the number of edges IN all breakout rooms

	#print("Best Stress, Worst Stress: ", worst_stress, best_stress)

	total_edges = (students * (students - 1)) // 2

	rest_of_edges = total_edges - rest_of_edges # Now this makes sense (sum of edges NOT in breakout rooms)

	rest_of_edge_tuples = [] # Compute (h_ij, s_ij) where ratio s_ij/h_ij is really big
	for _ in range(rest_of_edges):
		coin_flip = np.random.randint(0, 2)
		if coin_flip == 0:
			new_worst_stress = np.random.randint(worst_stress * 1000 * 1.1, 100_000) / 1000
			new_happiness = np.random.randint(best_happiness * 1000, min(98_000, best_happiness * 1000 * 1.3)) / 1000
			rest_of_edge_tuples.append((new_worst_stress, new_happiness))
		else:
			new_best_stress = np.random.randint(best_stress * 0.2 * 1000, best_stress * 1.3 * 1000) / 1000

			while str(new_best_stress) == "0.0":
				new_best_stress = np.random.randint(best_stress * 0.2 * 1000, best_stress * 1.3 * 1000) / 1000

			new_happiness = np.random.randint(0, worst_happiness * 1000 * 0.8) / 1000

			rest_of_edge_tuples.append((new_best_stress, new_happiness))
	#print(rest_of_edge_tuples)


	permute = np.array([i for i in range(students)])
	np.random.shuffle(permute)

	it = 0 # This is an index that we increment every time we add a student

	# fill_it_in is a matrix of student pairings that will contain i, j, h_ij, s_ij info
	fill_it_in = [["X" for j in range(students)] for i in range(students)]

	# mapping from student number to breakout room number
	output_ans = {}

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

		for student in con_students:
			# student is in breakout room i
			output_ans[student] = i

		nut = 0 # nut is the index of the corresponding happiness/stress of a pairing in a breakout room
		for j in range(len(con_students)): # ShUt Up DeAn
			for k in range(j + 1, len(con_students)):
				#print(con_students[j], con_students[k])
				q = "{0} {1} {2} {3}".format(con_students[j], con_students[k], h[nut], '%.3f' % s[nut])
				ans.append(q)
				fill_it_in[con_students[j]][con_students[k]] = q
				nut += 1
		#print(ans)
		#print(con_students)

	# Writing to output file
	output_f = open(str(students) + ".out", "w")
	for i_love_zhang_dean in range(students):
		output_f.write(str(i_love_zhang_dean) + " " + str(output_ans[i_love_zhang_dean]) + "\n")
	output_f.close()

	# Marco is the smartest human being alive
	# Now we're filling in info for the edges that go between breakout rooms

	errthing = 0 #Index for edges between breakout rooms
	for i in range(students): # oh my god dean shut up
		for j in range(i + 1, students):
			#print(i, j, fill_it_in[i][j])
			if fill_it_in[i][j] == "X":
				yy, yu = rest_of_edge_tuples[errthing]
				last_str = "{0} {1} {2} {3}".format(i, j, yu, yy)
				fill_it_in[i][j] = last_str
				errthing += 1

	#f = open("input" + str(students) + ".txt", "w")
	f = open(str(students) + ".in", "w")
	#print(str(S_max))
	f.write(str(students) + "\n")
	f.write(str(S_max + 1) + "\n")
	for i in range(students):
		for j in range(i + 1, students):
			#print(i, j, fill_it_in[i][j])
			f.write(fill_it_in[i][j] + "\n")
	f.close()

	return students

def main():
	generate_output(10)
	generate_output(20)
	generate_output(50)

if __name__ == '__main__':
	main()
