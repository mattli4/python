'''this function present a type of traverseing a matrix
    e.g
        input:[[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        output:[1, 2, 4, 7, 5, 3, 6, 8, 9]
'''
def zigzag(m, n):
    zigzag = []
    row = 0
    col = 0
    right, rightUp, down, leftDown = range(4)
    choice = right
    while row != n - 1 or col != n - 1:
        zigzag.append(m[row][col])
        if choice == right:
            col += 1
            if row == 0:
                choice = leftDown
            else:
                choice = rightUp
        elif choice == rightUp:
            row -= 1
            col += 1
            if row == 0 and col != n - 1:
                choice = right
            elif col == n - 1:
                choice = down
            else:
                choice = rightUp
        elif choice == down:
            row += 1
            if col == 0:
                choice = rightUp
            else:
                choice = leftDown
        elif choice == leftDown:
            row += 1
            col -= 1
            if col == 0 and row != n - 1:
                choice = down
            elif row == n - 1:
                choice = right
            else:
                choice = leftDown;
    zigzag.append(m[n-1][n-1])
    return zigzag