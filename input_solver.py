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

	print(partitions)

	return students

def main():
	print(10)
	generate_output(10)
	generate_output(20)
	generate_output(50)

if __name__ == '__main__':
	main()
