SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼긩'
DRAW = '비겼긩'
LOSE = '졌긩ㅠ'

mine = '가위'
yours = '바위'

if mine == yours:
	result = DRAW
	
else:
	if mine == SCISSOR:
		if yours == ROCK:
			result = LOSE
		else:
			result = WIN
	elif mine == ROCK:
		if yours == PAPER:
			result = LOSE
		else:
			result = WIN
	elif mine == PAPER:
		if yours == SCISSOR:
			result = LOSE
		else:
			result = WIN
	else:
		print('이상하긔')
		
print(result)
