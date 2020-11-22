#!/usr/bin/env python3
import numpy as np
import sys
from parse import *
from utils import *
import random

def generate_output(students):
	k = np.random.randint(1, students)
	
	fin = students
	partitions = []
	while fin > 0:		
		iter_size = np.random.randint(1, fin + 1)	
		fin -= iter_size
		partitions.append(iter_size)

	
	S_max = np.random.randint(0, 100000) / 1000
	print(S_max)

	k = len(partitions)
	print(partitions)

	k_max = S_max / k
	print(k_max)

	#
	for p in partitions:
		s = 0
		l = []
		for i in range(p * (p - 1) // 2):
			n = np.random.randint(0, 100000) / 1000
			s += n
			l.append(n)
		l = [el * k_max / s for el in l]
		
		print(l)
		print(sum(l))	

	return students

def main():
	print(10)
	generate_output(10)
	generate_output(20)
	generate_output(50)

if __name__ == '__main__':
	main()
