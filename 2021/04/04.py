from typing import Text
from typing import List
from typing import Generator


def read_input_file(path: Text) -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield line


def mark_boards(boards, number) -> List[List[List[Text]]]:
    for board in boards:
        for row_index, row in enumerate(board):
            for column_index, column in enumerate(row):
                if board[row_index][column_index] == number:
                    board[row_index][column_index] += '.'
    return boards


def get_boards(raw_text: Text) -> List[List[List[Text]]]:
    boards = [board.split('\n') for board in raw_text.split('\n\n')]
    boards_processed = [[line.split() for line in board if line] for board in boards]
    return boards_processed


def is_board_winner(board):
    match_indexes = []
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            if board[row_index][column_index].endswith('.'):
                match_indexes.append((row_index, column_index))

    xs = [index[0] for index in match_indexes]
    ys = [index[1] for index in match_indexes]
    if any([(xs.count(index) == len(board)) for index in range(len(board))]):
        return True
    if any([(ys.count(index) == len(board)) for index in range(len(board))]):
        return True
    return False


def count_sum_of_unmarked_numbers(board):
    score = 0
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            if not board[row_index][column_index].endswith('.'):
                score += int(board[row_index][column_index])
    return score


class Done(Exception):
    pass


def main():
    numbers = None
    boards = []
    boards_raw_text = ''
    for line in read_input_file("test_input.txt"):
        if numbers is None:
            numbers = line.split(',')
            continue

        boards_raw_text += line

    boards = get_boards(boards_raw_text)

    for number in numbers:
        mark_boards(boards, number)
        for board in boards:
            if is_board_winner(board):
                print(int(number) * count_sum_of_unmarked_numbers(board))


def main_part_two():
    numbers = None
    boards = []
    boards_raw_text = ''
    for line in read_input_file("input.txt"):
        if numbers is None:
            numbers = line.split(',')
            continue

        boards_raw_text += line

    boards = get_boards(boards_raw_text)

    winner_boards = []
    try:
        for number in numbers:
            mark_boards(boards, number)
            for index, board in enumerate(boards):
                if is_board_winner(board):
                    if index not in winner_boards:
                        winner_boards.append(index)
                        if len(winner_boards) == len(boards):
                            raise Done
    except Done:
        print(int(number) * count_sum_of_unmarked_numbers(board))


if __name__ == "__main__":
    # main()
    main_part_two()
