board = {1: '_', 2: '_', 3: '_', 4: '_', 5: '_', 6: '_', 7: '_', 8: '_', 9: '_'}


def print_board():
	print(f'{board[1]} {board[2]} {board[3]}')
	print(f'{board[4]} {board[5]} {board[6]}')
	print(f'{board[7]} {board[8]} {board[9]}')


players = {'x': [], 'o': []}


rule_win = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	[1, 4, 7],
	[2, 5, 8],
	[3, 6, 9],
	[1, 5, 9],
	[3, 5, 7]
]


def find_winner(sign):
	board_lay = set(players[sign])
	winner = bool([True for rule in rule_win if len(board_lay.intersection(rule)) == 3])
	return winner


def check_sign(cell, sign):
	board[cell] = sign
	players[sign].append(cell)


def game():
	sign = 'x'
	current_step = 1
	while True:
		print_board()
		cell = input(f'Введите номер ячейки от 1 до 9, цифра 0 оканчивает игру, текущий ход у {sign}: ')
		if cell == 'o':
			print('Конец игры')
			break
		elif cell in list(map(str, range(1, 10))):
			if board[int(cell)] == '_':
				check_sign(int(cell), sign)
			else:
				print('Ячейка занята, введите другую')
				continue

			if find_winner(sign):
				print(f'Победитель {sign}')
				print_board()
				print(f'Конец игры')
				break
			else:
				if current_step == 9:
					print('Ничья')
					break
				else:
					current_step += 1
			sign = 'o' if sign == 'x' else 'x'
		else:
			print(f'Неправильный ввод')
			print(f'Введите номер ячейки от 1 до 9, цифра 0 оканчивает игру, текущий ход у {sign}: ')
			continue


game()
