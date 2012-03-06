#!usr/bin/env python
import sys

def main():
	i = raw_input("Enter Puzzle:     **(for blanks, use '0') \n")
	array = []
	for k in i:
		array.append(k)
	if len(array) != 9:
		raise BadPuzzleInput
	puzzle = []
	puzzle.append(array)
	n = 0
	while n < 8:
		i = raw_input()
		array = []
		for k in i:
			array.append(k)
		if len(array) != 9:
			raise BadPuzzleInput
		puzzle.append(array)
		n += 1
	puzzleString = ''	
	for arr in range(0,9):
		for str in range(0,9):
			puzzleString += puzzle[arr][str]
			
	solve(puzzleString)
		
def finalize(solution):
	puzzle = []
	puzzleHelp = []
	count = 0
	for i in range(81):
		puzzleHelp.append(solution[i])
		count += 1
		if count % 9 == 0:
			puzzle.append(puzzleHelp)
			puzzleHelp = []
			count = 0
	display(puzzle)
		
		
def display(puzzle):
	x = 0
	for array in puzzle:
		returnString = ' '
		for n in range(0,9):
			if n == 2 or n == 5:
				if array[n] == '0':
					returnString += 'X | '
				else:
					returnString += str(array[n] + ' | ')
			else: 
				if array[n] == '0':
					returnString += 'X '
				else:
					returnString += str(array[n] + ' ')
		if x == 2 or x == 5:
			print returnString
			print '-------+-------+-------'
		else:
			print returnString
		x += 1
	
def solve(puzzle):
	"""formatPuzzle = []
	for array in range(0,9):
		for string in range(0,9):
			formatPuzzle.append(puzzle[array][string])
	print formatPuzzle]"""
	blank = puzzle.find('0')
	if blank == -1:
		finalize(puzzle)
	
	usedNumbers = set()
	for num in range(81):
		if row(blank, num) or col(blank, num) or block(blank, num):
			usedNumbers.add(puzzle[num])
			
	for num in '123456789':
		if num not in usedNumbers:
			solve(puzzle[:blank]+num+puzzle[blank+1:])

def row(i,j):
	return (i/9 == j/9)
	
def col(i,j):
	return (i-j)%9 == 0

def block(i,j):
	return (i/27 == j/27 and i%9/3 == j%9/3)
						
if __name__ == "__main__":
	main()