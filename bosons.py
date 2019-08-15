import unittest

def animate(speed,string):
	
	def update(l,idx,dir):#this changes the needed cells for the next iteration.
		#updates [ string[idx+speed] or string[idx-speed] or both ] if allowed
		if dir =='R':
			if idx+speed<len(l):
				if l[idx+speed] =='.' or l[idx+speed]=='R':
					l[idx+speed]='R'
				elif l[idx+speed]=='L': #conflict
					l[idx+speed]='B'
				#elif l[idx+speed]=='B': -> no need for update
		if dir =='L':
			if idx-speed>=0:
				if l[idx-speed] =='.' or l[idx-speed]=='L':
					l[idx-speed]='L'
				elif l[idx-speed]=='R': #conflict
					l[idx-speed]='B'
				#elif l[idx-speed]=='B': -> no need for update
	
	def colorX(listOfStrings): #colors all non empty places 'X'
		for i in range(len(listOfStrings)):
			temp=list(listOfStrings[i])
			for j in range(len(temp)):
				if temp[j]!='.':
					temp[j]='X'
			listOfStrings[i]="".join(temp)
		return listOfStrings

	L=len(string)
	final=[]
	final.append(string) #append the initial config as is.
	if (string.count('.')==L):
		return final
	temp_str=string
	
	iteration=[]
	#print("Temp_Str ",temp_str)-> use to see direction at all time points
	while(iteration.count('.')!=L):
		iteration=['.' for _ in range(L)]
		for i in range(len(temp_str)):
			if temp_str[i]=='R':
				update(iteration,i,'R')
			elif temp_str[i]=='L': 
				update(iteration,i,'L')
			elif temp_str[i]=='B': #update both ends if possible
				update(iteration,i,'L')
				update(iteration,i,'R')
		
		temp_str="".join(iteration)
		final.append(temp_str)
		#print("Temp_Str ",temp_str)-> use to see direction at all time poi
	
	return colorX(final)

class TestAnimate(unittest.TestCase):
	def test_animate_test0(self):
		test0=2, "..R...."
		self.assertEqual(animate(test0[0],test0[1]), 
		[ "..X....","....X..","......X","......." ])	
	def test_animate_test1(self):
		test1=3, "RR..LRL"
		self.assertEqual(animate(test1[0],test1[1]), 
		["XX..XXX",".X.XX..","X.....X","......."])
	def test_animate_test2(self):
		test2=2, "LRLR.LRLR"
		self.assertEqual(animate(test2[0],test2[1]), 
		["XXXX.XXXX","X..X.X..X",".X.X.X.X.",".X.....X.","........."])
	def test_animate_test3(self):
		test3=10, "RLRLRLRLRL"
		self.assertEqual(animate(test3[0],test3[1]), 
		["XXXXXXXXXX",".........."])
	def test_animate_test4(self):
		test4=1, "..."
		self.assertEqual(animate(test4[0],test4[1]), 
		["..."])
	def test_animate_test5(self):
		test5=1, "LRRL.LR.LRR.R.LRRL."
		self.assertEqual(animate(test5[0],test5[1]), 
		["XXXX.XX.XXX.X.XXXX.",
		"..XXX..X..XX.X..XX.",
		".X.XX.X.X..XX.XX.XX",
		"X.X.XX...X.XXXXX..X",
		".X..XXX...X..XX.X..",
		"X..X..XX.X.XX.XX.X.",
		"..X....XX..XX..XX.X",
		".X.....XXXX..X..XX.",
		"X.....X..XX...X..XX",
		".....X..X.XX...X..X",
		"....X..X...XX...X..",
		"...X..X.....XX...X.",
		"..X..X.......XX...X",
		".X..X.........XX...",
		"X..X...........XX..",
		"..X.............XX.",
		".X...............XX",
		"X.................X",
		"..................."])
	
if __name__ == '__main__': 
	unittest.main() 
	
	

