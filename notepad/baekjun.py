# n x n 보드
# 같은 숫자가 인접해 있다면 이동, 더한다. 이동한 쪽으로 정렬

board_size = int(input())
board = []
raw_board = [input().split() for size in range(board_size)]
for element in raw_board:
    new_element = list(map(int, element))
    board.append(new_element)
print(board)

for row in range(board_size):
    for col in range(board_size):
        if (col <= (board_size - 3)) and (board[row][col] == board[row][col + 1]):
            board[row][col] = board[row][col] + board[row][col + 1]
            board[row][col + 1] = board[row][col + 2]
            board[row][col + 2] = 0
        elif (row <= (board_size - 3)) and (board[row][col] == board[row + 1][col]):
            board[row][col] = board[row][col] + board[row + 1][col]
            board[row + 1][col] = board[row + 2][col]
            board[row + 2][col] = 0

print(board)