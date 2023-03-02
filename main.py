def diagonalDifference(arr):
    # input is always a square 2d array
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0

    for index, row in enumerate(arr):
        left_to_right_diagonal += row[index]
        right_to_left_diagonal += row[-index - 1]

    return abs(left_to_right_diagonal - right_to_left_diagonal)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')