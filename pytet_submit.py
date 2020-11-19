from matrix import *
from random import *
def draw_matrix(m):
	array = m.get_array()
	for y in range(m.get_dy()):
		for x in range(m.get_dx()):
			if array[y][x] == 0:
				print("□", end='')
			elif array[y][x] == 1:
				print("■", end='')
			else:
				print("XX", end='')
		print()

def rotate(what_type):
	global arrayBlk_ALL
	for m in range(0,7):
		for n in range(0,4):
			if arrayBlk_ALL[m][n] == what_type:
				index1 = m
				index2 = n
	if index2==3:
		return arrayBlk_ALL[index1][0]
	else:
		return arrayBlk_ALL[index1][index2+1]


def unrotate(what_type):
	global arrayBlk_ALL
	for m in range(0,7):
		for n in range(0,4):
			if arrayBlk_ALL[m][n] == what_type:
				index1 = m
				index2 = n
	if index2==0:
		return arrayBlk_ALL[index1][3]
	else:
		return arrayBlk_ALL[index1][index2 -1]


arrayBlk_ALL =[
	
	[
	[[1, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ]],
	[[0, 1, 1 ], [ 1, 1, 0 ], [ 0, 0, 0 ]],	
	[[0, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 1 ]],	
	[[0, 0, 0 ], [ 0, 1, 1 ], [ 1, 1, 0 ]]	
	],

	[
	[[1, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ]],
	[[0, 1, 1 ], [ 0, 1, 0 ], [ 0, 1, 0 ]],	
	[[0, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 1 ]],	
	[[0, 1, 0 ], [ 0, 1, 0 ], [ 1, 1, 0 ]]
	],

	[
	[[0, 0, 1 ], [ 1, 1, 1 ], [ 0, 0, 0 ]],
	[[0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 1 ]],	
	[[0, 0, 0 ], [ 1, 1, 1 ], [ 1, 0, 0 ]],	
	[[1, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ]]	
	],

	[
	[[0, 1, 0 ], [ 1, 1, 0 ], [ 1, 0, 0 ]],
	[[1, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 0 ]],	
	[[0, 0, 1 ], [ 0, 1, 1 ], [ 0, 1, 0 ]],	
	[[0, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 1 ]]	
	],

	[
	[[0, 1, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ]],
	[[0, 1, 0 ], [ 0, 1, 1 ], [ 0, 1, 0 ]],	
	[[0, 0, 0 ], [ 1, 1, 1 ], [ 0, 1, 0 ]],	
	[[0, 1, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ]]	
	],

	[
	[[ 1, 1 ], [ 1, 1 ]],
	[[ 1, 1 ], [ 1, 1 ]],
	[[ 1, 1 ], [ 1, 1 ]],
	[[ 1, 1 ], [ 1, 1 ]]
	],
	
	[
	[[ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ]],
	[[ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ]],
	[[ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ]],
	[[ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ]]
	]
]

###
### initialize variables
###     
def which_block():
	global arrayBlk_ALL
	
	Block_num = randint(0,6)
	
	return arrayBlk_ALL[Block_num][0]

arrayBlk = which_block()


###seven block###

### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False
w_Possible = True

arrayScreen = [
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:

	key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
	if key == 'q':
		print('Game terminated...')
		break
	elif key == 'a': # move left
		left -= 1
		w_Possible = True
	elif key == 'd': # move right
		left += 1
		w_Possible = True
	elif key == 's': # move down
		top += 1
		w_Possible = True
	elif key == 'w': # rotate the block clockwise
		if w_Possible ==True:
			arrayBlk = rotate(arrayBlk)
			currBlk = Matrix(arrayBlk)
			print("w_Possible")
		elif w_Possible == False:
			arrayBlk = unrotate(arrayBlk)
			currBlk = Matrix(arrayBlk)
			print("w_imPossible")

	elif key == ' ':
		while tempBlk.anyGreaterThan(1) == False:
			top += 1
			tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
			tempBlk = tempBlk + currBlk
	else:
		print('Wrong key!!!')
		continue

	tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
	tempBlk = tempBlk + currBlk
	if tempBlk.anyGreaterThan(1):

		if key == 'a': # undo: move right
			left += 1
		elif key == 'd': # undo: move left
			left -= 1
		elif key == 's': # undo: move up
			top -= 1
			newBlockNeeded = True
		elif key == 'w': # undo: rotate the block counter-clockwise
			if w_Possible == True:
				arrayBlk = unrotate(arrayBlk)
				currBlk = Matrix(arrayBlk)
				w_Possible = False

			elif w_Possible == False:
				arrayBlk = rotate(arrayBlk)
				currBlk = Matrix(arrayBlk)

		elif key == ' ': # undo: move up
			newBlockNeeded = True
			top -= 1
		tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
		tempBlk = tempBlk + currBlk
	oScreen = Matrix(iScreen)
	oScreen.paste(tempBlk, top, left)
	draw_matrix(oScreen); print()

	if newBlockNeeded:
		iScreen = Matrix(oScreen)
		top = 0
		left = iScreenDw + iScreenDx//2 - 2
		newBlockNeeded = False
		w_Possible = True
		arrayBlk = which_block()
		currBlk = Matrix(arrayBlk)
		tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
		tempBlk = tempBlk + currBlk
		if tempBlk.anyGreaterThan(1):

			print('Game Over!!!')
			break
        
		oScreen = Matrix(iScreen)
		oScreen.paste(tempBlk, top, left)
		draw_matrix(oScreen); print()
        
###
### end of the loop
###
