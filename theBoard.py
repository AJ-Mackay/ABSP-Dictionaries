theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

theBoard['mid-M'] = 'X'
theBoard['top-L'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['top-M'] = 'O'
theBoard['low-R'] = 'X'
theBoard['top-R'] = 'O'

printBoard(theBoard)
