import random


def minesweeper_map(input_str):

    lines = input_str.split("\n")[1:-1]
    height, width = len(lines), len(lines[0])

    # Converts the string to a matrix representation
    matrix = [[lines[i][j]
               for j in range(1, width - 1)] for i in range(height)]

    # Function to count the number of mines adjacent to a given cell
    def count_mines(i, j):
        mine_count = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                ni, nj = i + x, j + y
                if 0 <= ni < height and 0 <= nj < width - 2:
                    if matrix[ni][nj] == '*':
                        mine_count += 1
        return mine_count

    # Constructs the output matrix
    output_matrix = [[' ' for _ in range(width - 2)] for _ in range(height)]
    for i in range(height):
        for j in range(width - 2):
            if matrix[i][j] == '*':
                output_matrix[i][j] = '*'
            else:
                count = count_mines(i, j)
                output_matrix[i][j] = str(count) if count > 0 else ' '

    # Converts the output matrix to the output string format
    output_lines = ['+' + '-' * (width - 2) + '+']
    for row in output_matrix:
        output_lines.append('|' + ''.join(row) + '|')
    output_lines.append('+' + '-' * (width - 2) + '+')

    return '\n'.join(output_lines)


def generate_minefield(height=5, width=5, mine_probability=0.2):

    # Generates the random minefield matrix
    matrix = [['*' if random.random() < mine_probability else ' ' for _ in range(width)]
              for _ in range(height)]

    # Converts the matrix to string format with borders
    output_lines = ['+' + '-' * width + '+']
    for row in matrix:
        output_lines.append('|' + ''.join(row) + '|')
    output_lines.append('+' + '-' * width + '+')

    return '\n'.join(output_lines)

# Test input
# input_str = "+-------+\n| *   * |\n| *  *  |\n|  * *  |\n|* * * *|\n| *   * |\n| *  *  |\n|  * *  |\n|* * * *|\n| *   * |\n| *  *  |\n|  * *  |\n|* * * *|\n| *   * |\n| *  *  |\n|  * *  |\n|* * * *|\n| *   * |\n| *  *  |\n|  * *  |\n|* * * *|\n+-------+"


print(minesweeper_map(generate_minefield()))
