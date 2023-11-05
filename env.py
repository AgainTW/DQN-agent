import numpy as np

class enviroment:
	def __init__(self):
		self.env = []
		self.wall = []

	def initial(self, setini):
		#	setini[0]：環境長	setini[1]：環境寬
		self.env = np.full((setini[0]+2, setini[1]+2), False, dtype=bool)
		self.wall = np.full((setini[0]+2, setini[1]+2), False, dtype=bool)

		#	包邊 w
		for j in range(setini[1]+2):
			self.wall[0][j] = 1
			self.wall[setini[0]+1][j] = 1
		for i in range(setini[0]+2):
			self.wall[i][0] = 1
			self.wall[i][setini[1]+1] = 1

	def set_wall(self, wall):
		for i in wall:
			if( i[1]>=np.size(self.env,1) or i[0]>=np.size(self.env,0) ): print("error",i)
			else:	self.wall[ i[1]+1 ][ i[0]+1 ] = 1

	def play(self):
		for i in range(np.size(self.env,0)):
			for j in range(np.size(self.env,1)):
				if(self.wall[i][j]):	print("w", end=" ")
				elif(self.env[i][j]):	print("■", end=" ")
				else:	print("□", end=" ")
			print("")

def agent_play_env_full(x, y, env):
	print(x,y)
	x_bound = np.size(env.env,1)
	y_bound = np.size(env.env,0)
	for i in range(np.size(env.env,0)):
		for j in range(np.size(env.env,1)):
			if(i==y+1 and j==x+1):	print("a", end=" ")
			elif(env.wall[i][j]):	print("w", end=" ")
			elif(env.env[i][j]):	print("■", end=" ")
			else:	print("□", end=" ")
		print("")

def agent_play_env(x, y, env):
	x_bound = np.size(env.env,1)
	y_bound = np.size(env.env,0)
	for i in range(-1,2,1):
		for j in range(-1,2,1):
			if( (j+x+1)>=x_bound or (i+y+1)>=y_bound ): print("error",i+x,j+j, end=" ")
			elif(i==0 and j==0):	print("a", end=" ")
			elif(env.wall[y+i+1][x+j+1]):	print("w", end=" ")
			elif(env.env[y+i+1][x+j+1]):	print("■", end=" ")
			else:	print("□", end=" ")
		print("")

def agent_wall_test(x, y, env):
	x_bound = np.size(env.env,1)
	y_bound = np.size(env.env,0)
	if( (x+1)>=x_bound or (y+1)>=y_bound ): return 2
	elif(env.wall[y+1][x+1]==1):	return 1
	else:	return 0

class agent:
	def __init__(self):
		self.locx = -1
		self.locy = -1
		self.env = 0

	def initial(self, env):
		self.env = env
		self.locx = 0
		self.locy = 0

	def set_loc(self, y, x):
		flag = agent_wall_test(x, y, self.env)
		if(flag==1):	print("wall_error")
		elif(flag==2):	print("bound_error")
		else:
			self.locx = x
			self.locy = y

	def loc_test(self, y, x):
		flag = agent_wall_test(x, y, self.env)
		if(flag==1):
			print("wall_error")
		elif(flag==2):	
			print("bound_error")
		return flag

	def go_right(self):
		self.locx += 1

	def go_left(self):
		self.locx -= 1

	def go_up(self):
		self.locy -= 1

	def go_down(self):
		self.locy += 1

	def go(self,do):
		if(do==1):	
			flag = self.loc_test(self.locy-1, self.locx)
			if(flag==0):	self.go_up()
		elif(do==2):
			flag = self.loc_test(self.locy+1, self.locx)
			if(flag==0):	self.go_down()
		elif(do==3):
			flag = self.loc_test(self.locy, self.locx-1)
			if(flag==0):	self.go_left()
		elif(do==4):
			flag = self.loc_test(self.locy, self.locx+1)
			if(flag==0):	self.go_right()

	def play(self):
		print("Location：", self.locx, self.locy)
		agent_play_env(self.locx, self.locy, self.env)

	def full_play(self):
		print("Location：", self.locx, self.locy)
		agent_play_env_full(self.locx, self.locy, self.env)		

# 環境初始化
env6 = enviroment()
env6.initial([10,10])
wall = np.array( [ [5, 0], [5, 1], [7, 5], [7, 6], [8, 6], [9, 6] ] )
wall2 = np.array( [ [2, 5], [2, 6], [2, 7], [2, 8], [2, 9] ] )
wall3 = np.array( [ [1, 1], [1, 2], [2, 1], [2, 2] ] )
env6.set_wall( wall )
env6.set_wall( wall2 )
env6.set_wall( wall3 )

# agent初始化
ag6 = agent()
ag6.initial(env6)
ag6.set_loc(0, 0)

env6.play()

'''
a = enviroment()
setini = [10,10]
a.initial(setini)
wall = np.array( [ [5, 0], [5, 1] ] )
a.set_wall( wall )
a.play()

b = agent()
b.initial(a)
b.set_loc(0, 4)
b.full_play()
b.go(2)
b.full_play()
b.go(2)
b.full_play()
b.go(4)
b.full_play()
b.go(4)
b.full_play()
b.go(1)
b.full_play()
b.go(1)
b.full_play()
b.go(3)
b.full_play()
b.go(3)
b.full_play()
'''