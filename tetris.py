from matrix import *
from random import *
from enum import Enum
#import LED_display as LMD 

class TetrisState(Enum):
	Running = 0
	NewBlock = 1
	Finished = 2
### end of class TetrisState():

class Tetris():
	nBlockTypes = 0
	nBlockDegrees = 0
	setOfBlockObjects = 0
	iScreenDw = 0   # larget enough to cover the largest block

	@classmethod
	def init(cls, setOfBlockArrays):
		Tetris.nBlockTypes = len(setOfBlockArrays)
		Tetris.nBlockDegrees = len(setOfBlockArrays[0])
		Tetris.setOfBlockObjects = [[0] * Tetris.nBlockDegrees for _ in range(Tetris.nBlockTypes)]
		arrayBlk_maxSize = 0
		for i in range(Tetris.nBlockTypes):
			if arrayBlk_maxSize <= len(setOfBlockArrays[i][0]):
				arrayBlk_maxSize = len(setOfBlockArrays[i][0])
		Tetris.iScreenDw = arrayBlk_maxSize     # larget enough to cover the largest block

		for i in range(Tetris.nBlockTypes):
			for j in range(Tetris.nBlockDegrees):
				Tetris.setOfBlockObjects[i][j] = Matrix(setOfBlockArrays[i][j])
		return
		
	def createArrayScreen(self):
		self.arrayScreenDx = Tetris.iScreenDw * 2 + self.iScreenDx
		self.arrayScreenDy = self.iScreenDy + Tetris.iScreenDw
		self.arrayScreen = [[0] * self.arrayScreenDx for _ in range(self.arrayScreenDy)]
		for y in range(self.iScreenDy):
			for x in range(Tetris.iScreenDw):
				self.arrayScreen[y][x] = 1
			for x in range(self.iScreenDx):
				self.arrayScreen[y][Tetris.iScreenDw + x] = 0
			for x in range(Tetris.iScreenDw):
				self.arrayScreen[y][Tetris.iScreenDw + self.iScreenDx + x] = 1

		for y in range(Tetris.iScreenDw):
			for x in range(self.arrayScreenDx):
				self.arrayScreen[self.iScreenDy + y][x] = 1

		return self.arrayScreen
		
	def __init__(self, iScreenDy, iScreenDx):
		self.iScreenDy = iScreenDy
		self.iScreenDx = iScreenDx
		self.idxBlockType = 0
		self.idxBlockDegree = 0
		arrayScreen = self.createArrayScreen()
		self.iScreen = Matrix(arrayScreen)
		self.oScreen = Matrix(self.iScreen)
		self.justStarted = True
		
		return

	def printScreen(self):
		array = self.oScreen.get_array()

		for y in range(self.oScreen.get_dy()-Tetris.iScreenDw):
			for x in range(Tetris.iScreenDw, self.oScreen.get_dx()-Tetris.iScreenDw):
				if array[y][x] == 0:
					print("□", end='')
                    #LMD.set_pixel(y, 19-x, 0)
				elif array[y][x] == 1:
					print("■", end='')
                    #LMD.set_pixel(y, 19-x, 4)
				else:
					print("XX", end='')
                    #continue
			print()

	def deleteFullLines(self): # fully implemented!!!
		for_delete = self.oScreen.get_array()
		check_full = 0
		for i in range(24):
			check_full += for_delete[31][i]
		
		if check_full == 24:
			for m in range(31,-1,-1):
				for n in range(4,20):
						for_delete[m+1][n] = for_delete[m][n]
			for i in range(4,20):
				for_delete[0][i] =0
		
		
		return Matrix(for_delete)

	def accept(self, key):  #fully implemented!!

		if self.justStarted == True:
			self.top = 0
			self.left = Tetris.iScreenDw + self.iScreenDx//2 - 2	
			self.justStarted = False
			self.state = TetrisState.Running


		if len(key) ==2 and key.isdigit() ==True:
			self.retain_key = key            #여기서 구한 retain_key는 가장 밑에 NewBlock if문을 돌때 idxblockType 로 사용하게 됩니다.

		if self.state == TetrisState.NewBlock:
			if self.tempBlk.anyGreaterThan(1)==True:
				self.state = TetrisState.Finished
				return self.state 

		self.state = TetrisState.Running
		
		if key == 'a':
			self.left = self.left -1
		elif key == 'd':
			self.left = self.left +1
		elif key == 's':
			self.top += 1
		elif key == ' ':
			while self.tempBlk.anyGreaterThan(1)==False:
				self.top +=1
				self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
				self.tempBlk = self.tempBlk + self.currBlk
		elif key == 'w':
				self.idxBlockDegree  = (1+self.idxBlockDegree) %4

		self.currBlk = Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree]
		self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
		self.tempBlk = self.tempBlk + self.currBlk
		self.oScreen = Matrix(self.iScreen)
		self.oScreen.paste(self.tempBlk, self.top, self.left);
	
		
		if self.tempBlk.anyGreaterThan(1):
			if key =='a':
				self.left = self.left +1
			elif key == 'd':
				self.left = self.left -1
			elif key == 'w':
				self.idxBlockDegree  = self.idxBlockDegree-1
			elif key == 's' or ' ':
				self.top = self.top -1
				self.state = TetrisState.NewBlock
			
			self.currBlk = Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree]
			self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())
			self.tempBlk = self.tempBlk + self.currBlk
			self.oScreen = Matrix(self.iScreen)
			self.oScreen.paste(self.tempBlk, self.top, self.left)
			print()

	
		if self.state == TetrisState.NewBlock:
			self.iScreen = self.deleteFullLines()
			self.top =0
			self.left = Tetris.iScreenDw + self.iScreenDx//2 - 2
			self.idxBlockType = int(self.retain_key)
			self.currBlk = Tetris.setOfBlockObjects[self.idxBlockType][self.idxBlockDegree]

			self.tempBlk = self.iScreen.clip(self.top, self.left, self.top+self.currBlk.get_dy(), self.left+self.currBlk.get_dx())

			self.tempBlk = self.tempBlk + self.currBlk
			self.oScreen = Matrix(self.iScreen)
			self.oScreen.paste(self.tempBlk,self.top,self.left)
			print()


		return self.state
		
#	
### end of class Tetris():
   # 
