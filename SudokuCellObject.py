import math


class Cell:
    def __init__(self, line, row, cube, value):
        self.line = line
        self.row = row
        self.cube = cube
        self.value = value
        if value == 0:
            self.possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.possibilities = []


# region in this region system changes cells value by controlling if it is the only possiblity
def create_sudoku_list(sudoku):
    celllist = []
    celllist.append(Cell(1, 1, 1, sudoku[0][0]))
    celllist.append(Cell(1, 2, 1, sudoku[0][1]))
    celllist.append(Cell(1, 3, 1, sudoku[0][2]))
    celllist.append(Cell(1, 4, 2, sudoku[0][3]))
    celllist.append(Cell(1, 5, 2, sudoku[0][4]))
    celllist.append(Cell(1, 6, 2, sudoku[0][5]))
    celllist.append(Cell(1, 7, 3, sudoku[0][6]))
    celllist.append(Cell(1, 8, 3, sudoku[0][7]))
    celllist.append(Cell(1, 9, 3, sudoku[0][8]))
    #####################################
    celllist.append(Cell(2, 1, 1, sudoku[1][0]))
    celllist.append(Cell(2, 2, 1, sudoku[1][1]))
    celllist.append(Cell(2, 3, 1, sudoku[1][2]))
    celllist.append(Cell(2, 4, 2, sudoku[1][3]))
    celllist.append(Cell(2, 5, 2, sudoku[1][4]))
    celllist.append(Cell(2, 6, 2, sudoku[1][5]))
    celllist.append(Cell(2, 7, 3, sudoku[1][6]))
    celllist.append(Cell(2, 8, 3, sudoku[1][7]))
    celllist.append(Cell(2, 9, 3, sudoku[1][8]))
    #####################################
    celllist.append(Cell(3, 1, 1, sudoku[2][0]))
    celllist.append(Cell(3, 2, 1, sudoku[2][1]))
    celllist.append(Cell(3, 3, 1, sudoku[2][2]))
    celllist.append(Cell(3, 4, 2, sudoku[2][3]))
    celllist.append(Cell(3, 5, 2, sudoku[2][4]))
    celllist.append(Cell(3, 6, 2, sudoku[2][5]))
    celllist.append(Cell(3, 7, 3, sudoku[2][6]))
    celllist.append(Cell(3, 8, 3, sudoku[2][7]))
    celllist.append(Cell(3, 9, 3, sudoku[2][8]))
    #####################################
    celllist.append(Cell(4, 1, 4, sudoku[3][0]))
    celllist.append(Cell(4, 2, 4, sudoku[3][1]))
    celllist.append(Cell(4, 3, 4, sudoku[3][2]))
    celllist.append(Cell(4, 4, 5, sudoku[3][3]))
    celllist.append(Cell(4, 5, 5, sudoku[3][4]))
    celllist.append(Cell(4, 6, 5, sudoku[3][5]))
    celllist.append(Cell(4, 7, 6, sudoku[3][6]))
    celllist.append(Cell(4, 8, 6, sudoku[3][7]))
    celllist.append(Cell(4, 9, 6, sudoku[3][8]))
    #####################################
    celllist.append(Cell(5, 1, 4, sudoku[4][0]))
    celllist.append(Cell(5, 2, 4, sudoku[4][1]))
    celllist.append(Cell(5, 3, 4, sudoku[4][2]))
    celllist.append(Cell(5, 4, 5, sudoku[4][3]))
    celllist.append(Cell(5, 5, 5, sudoku[4][4]))
    celllist.append(Cell(5, 6, 5, sudoku[4][5]))
    celllist.append(Cell(5, 7, 6, sudoku[4][6]))
    celllist.append(Cell(5, 8, 6, sudoku[4][7]))
    celllist.append(Cell(5, 9, 6, sudoku[4][8]))
    #####################################
    celllist.append(Cell(6, 1, 4, sudoku[5][0]))
    celllist.append(Cell(6, 2, 4, sudoku[5][1]))
    celllist.append(Cell(6, 3, 4, sudoku[5][2]))
    celllist.append(Cell(6, 4, 5, sudoku[5][3]))
    celllist.append(Cell(6, 5, 5, sudoku[5][4]))
    celllist.append(Cell(6, 6, 5, sudoku[5][5]))
    celllist.append(Cell(6, 7, 6, sudoku[5][6]))
    celllist.append(Cell(6, 8, 6, sudoku[5][7]))
    celllist.append(Cell(6, 9, 6, sudoku[5][8]))
    #####################################
    celllist.append(Cell(7, 1, 7, sudoku[6][0]))
    celllist.append(Cell(7, 2, 7, sudoku[6][1]))
    celllist.append(Cell(7, 3, 7, sudoku[6][2]))
    celllist.append(Cell(7, 4, 8, sudoku[6][3]))
    celllist.append(Cell(7, 5, 8, sudoku[6][4]))
    celllist.append(Cell(7, 6, 8, sudoku[6][5]))
    celllist.append(Cell(7, 7, 9, sudoku[6][6]))
    celllist.append(Cell(7, 8, 9, sudoku[6][7]))
    celllist.append(Cell(7, 9, 9, sudoku[6][8]))
    #####################################
    celllist.append(Cell(8, 1, 7, sudoku[7][0]))
    celllist.append(Cell(8, 2, 7, sudoku[7][1]))
    celllist.append(Cell(8, 3, 7, sudoku[7][2]))
    celllist.append(Cell(8, 4, 8, sudoku[7][3]))
    celllist.append(Cell(8, 5, 8, sudoku[7][4]))
    celllist.append(Cell(8, 6, 8, sudoku[7][5]))
    celllist.append(Cell(8, 7, 9, sudoku[7][6]))
    celllist.append(Cell(8, 8, 9, sudoku[7][7]))
    celllist.append(Cell(8, 9, 9, sudoku[7][8]))
    #####################################
    celllist.append(Cell(9, 1, 7, sudoku[8][0]))
    celllist.append(Cell(9, 2, 7, sudoku[8][1]))
    celllist.append(Cell(9, 3, 7, sudoku[8][2]))
    celllist.append(Cell(9, 4, 8, sudoku[8][3]))
    celllist.append(Cell(9, 5, 8, sudoku[8][4]))
    celllist.append(Cell(9, 6, 8, sudoku[8][5]))
    celllist.append(Cell(9, 7, 9, sudoku[8][6]))
    celllist.append(Cell(9, 8, 9, sudoku[8][7]))
    celllist.append(Cell(9, 9, 9, sudoku[8][8]))
    return celllist
# endregion create cells


# region clean first level of possibilities


def clean_cell_list_possibilities(cell_list):
    is_changed = False
    for cell in cell_list:
        if clean_single_cell_possibilities(cell, cell_list):
            if not is_changed:
                is_changed = True
    return is_changed


def clean_single_cell_possibilities(cell, cell_list):
    is_changed = False
    line_list = [x.value for x in cell_list if x.line == cell.line]
    row_list = [x.value for x in cell_list if x.row == cell.row]
    cube_list = [x.value for x in cell_list if x.cube == cell.cube]
    unpossible_values = line_list + row_list + cube_list
    unique_unpossible = list(set(unpossible_values))
    for value in unique_unpossible:
        if value in cell.possibilities:
            cell.possibilities.remove(value)
            is_changed = True
    return is_changed


# endregion


# region applies first level of possibilities
def clean_value_from_possibilities(cell, cell_list):
    same_area_cell_list = [x for x in cell_list if (x.value == 0) and (x.line == cell.line or
                                                                       x.row == cell.row or
                                                                       x.cube == cell.cube)]
    for area_cell in same_area_cell_list:
        if cell.value in area_cell.possibilities:
            area_cell.possibilities.remove(cell.value)


def apply_only_possibility_in_cell_list(cell_list):
    is_change = False
    for cell in cell_list:
        if len(cell.possibilities) == 1:
            is_change = True
            cell.value = cell.possibilities[0]
            cell.possibilities = []
            clean_value_from_possibilities(cell, cell_list)
            print(cell.line, cell.row, cell.value)
    return is_change
# endregion


# region applies second level of possibilities
def apply_only_possibility_in_area(cell_list):
    is_changed = False
    for cell in cell_list:
        for value in cell.possibilities:
            if len([x for x in cell_list if x.line == cell.line and value in x.possibilities]) == 1:
                is_changed = True
                cell.value = value
                clean_value_from_possibilities(cell, cell_list)
                cell.possibilities = []
                print(cell.line, cell.row)
                break
            if len([x for x in cell_list if x.row == cell.row and value in x.possibilities]) == 1:
                is_changed = True
                cell.value = value
                clean_value_from_possibilities(cell, cell_list)
                cell.possibilities = []
                print(cell.line, cell.row)
                break
            if len([x for x in cell_list if x.cube == cell.cube and value in x.possibilities]) == 1:
                is_changed = True
                cell.value = value
                clean_value_from_possibilities(cell, cell_list)
                cell.possibilities = []
                print(cell.line, cell.row)
                break
    return is_changed

# endregion


# region first high level solutions starts
def check_for_only_two_possibilities(cell_list):
    is_changed = False
    if not is_changed:
        is_changed = only_two_possibilities_for_lines(cell_list)
    if not is_changed:
        is_changed = only_two_possibilities_for_cubes(cell_list)
    if not is_changed:
        is_changed = only_two_possibilities_for_rows(cell_list)
    return is_changed


# region for lines


def only_two_possibilities_for_lines(cell_list):
    is_changed = False
    i = 1
    while i < 10:
        is_changed = check_for_only_one_line(cell_list, i)
        if is_changed:
            return is_changed
        i += 1
    return is_changed


def check_for_only_one_line(cell_list, i):
    is_changed = False
    only_two_same_values = [x for x in cell_list if len(x.possibilities) == 2 and x.line == i]
    if len(only_two_same_values) > 1:
        for cell in only_two_same_values:
            identical_possibilities = [x for x in only_two_same_values if x.possibilities == cell.possibilities]
            if len(identical_possibilities) > 1:
                is_changed = clean_from_line_possibility(cell_list, identical_possibilities)
                if is_changed:
                    return is_changed
    return is_changed


def clean_from_line_possibility(cell_list, identical_possibilities):
    is_changed = False
    line = identical_possibilities[0].line
    to_be_changed_list = [x for x in cell_list if x not in identical_possibilities and x.line == line and x.value == 0]
    for cell in to_be_changed_list:
        for value in identical_possibilities[0].possibilities:
            if value in cell.possibilities:
                cell.possibilities.remove(value)
                is_changed = True
    return is_changed
# endregion

# region for cubes


def only_two_possibilities_for_cubes(cell_list):
    is_changed = False
    i = 1
    while i < 10:
        is_changed = check_for_only_one_cube(cell_list, i)
        if is_changed:
            return is_changed
        i += 1
    return is_changed


def check_for_only_one_cube(cell_list, i):
    is_changed = False
    only_two_same_values = [x for x in cell_list if len(x.possibilities) == 2 and x.cube == i]
    if len(only_two_same_values) > 1:
        for cell in only_two_same_values:
            identical_possibilities = [x for x in only_two_same_values if x.possibilities == cell.possibilities]
            if len(identical_possibilities) > 1:
                is_changed = clean_from_cube_possibility(cell_list, identical_possibilities)
                if is_changed:
                    return is_changed
    return is_changed


def clean_from_cube_possibility(cell_list, identical_possibilities):
    is_changed = False
    cube = identical_possibilities[0].cube
    to_be_changed_list = [x for x in cell_list if x not in identical_possibilities and x.cube == cube and x.value == 0]
    for cell in to_be_changed_list:
        for value in identical_possibilities[0].possibilities:
            if value in cell.possibilities:
                cell.possibilities.remove(value)
                is_changed = True
    return is_changed
# endregion

# region for rows


def only_two_possibilities_for_rows(cell_list):
    is_changed = False
    i = 1
    while i < 10:
        is_changed = check_for_only_one_row(cell_list, i)
        if is_changed:
            return is_changed
        i += 1
    return is_changed


def check_for_only_one_row(cell_list, i):
    is_changed = False
    only_two_same_values = [x for x in cell_list if len(x.possibilities) == 2 and x.row == i]
    if len(only_two_same_values) > 1:
        for cell in only_two_same_values:
            identical_possibilities = [x for x in only_two_same_values if x.possibilities == cell.possibilities]
            if len(identical_possibilities) > 1:
                is_changed = clean_from_row_possibility(cell_list, identical_possibilities)
                if is_changed:
                    return is_changed
    return is_changed


def clean_from_row_possibility(cell_list, identical_possibilities):
    is_changed = False
    row = identical_possibilities[0].row
    to_be_changed_list = [x for x in cell_list if x not in identical_possibilities and x.row == row and x.value == 0]
    for cell in to_be_changed_list:
        for value in identical_possibilities[0].possibilities:
            if value in cell.possibilities:
                cell.possibilities.remove(value)
                is_changed = True
    return is_changed
# endregion

# endregion


# region second high level solution starts


def start_second_level(cell_list):
    is_changed = False
    is_changed = check_lines_for_only_one_cube(cell_list)
    if is_changed:
        return is_changed
    is_changed = check_rows_for_only_one_cube(cell_list)
    if is_changed:
        return is_changed
    return is_changed


# region second hig level line control


def check_lines_for_only_one_cube(cell_list):
    is_changed = False
    i = 1
    while i < 10:
        is_changed = check_one_line_for_only_one_cube(cell_list,i)
        if is_changed:
            return is_changed
        i += 1
    return is_changed


def check_one_line_for_only_one_cube(cell_list,i):
    is_changed = False
    numbers = [1,2,3,4,5,6,7,8,9]
    values = [x.value for x in cell_list if x.value != 0 and x.line == i]
    for number in numbers:
        if number not in values:
            cubes = [x for x in cell_list if number in x.possibilities and x.line == i]
            cube_nums = [x.cube for x in cubes]
            cube_nums = list(set(cube_nums))
            if len(cube_nums) == 1:
                is_changed = clean_the_cube_for_lines(cell_list, cubes, number)
            if is_changed:
                return is_changed
    return is_changed


def clean_the_cube_for_lines(cell_list, cubes, number):
    is_changed = False
    cube = cubes[0].cube
    cubes_to_be_cleaned = [x for x in cell_list if x.cube == cube and number in x.possibilities]
    for cell in cubes_to_be_cleaned:
        if cell not in cubes:
            is_changed = True
            cell.possibilities.remove(number)
    return is_changed


# endregion

# region second high level row control


def check_rows_for_only_one_cube(cell_list):
    is_changed = False
    i = 1
    while i < 10:
        is_changed = check_one_row_for_only_one_cube(cell_list,i)
        if is_changed:
            return is_changed
        i += 1
    return is_changed


def check_one_row_for_only_one_cube(cell_list,i):
    is_changed = False
    numbers = [1,2,3,4,5,6,7,8,9]
    values = [x.value for x in cell_list if x.value != 0 and x.row == i]
    for number in numbers:
        if number not in values:
            cubes = [x for x in cell_list if number in x.possibilities and x.row == i]
            cube_nums = [x.cube for x in cubes]
            cube_nums = list(set(cube_nums))
            if len(cube_nums) == 1:
                is_changed = clean_the_cube_for_rows(cell_list, cubes, number)
            if is_changed:
                return is_changed
    return is_changed


def clean_the_cube_for_rows(cell_list, cubes, number):
    is_changed = False
    cube = cubes[0].cube
    cubes_to_be_cleaned = [x for x in cell_list if x.cube == cube and number in x.possibilities]
    for cell in cubes_to_be_cleaned:
        if cell not in cubes:
            is_changed = True
            cell.possibilities.remove(number)
    return is_changed
# endregion

# endregion






def __main__():
    sudoku = [[0,0,0,0,1,0,0,0,0],
              [0,2,0,0,0,0,0,9,5],
              [0,7,0,0,5,0,0,0,3],
              [0,0,2,3,0,0,7,0,1],
              [0,0,0,7,0,0,4,0,0],
              [4,3,0,8,0,0,0,0,0],
              [6,5,0,4,0,0,0,0,0],
              [0,0,0,0,6,2,0,0,0],
              [0,9,0,0,0,0,0,7,0]]

    cell_list = create_sudoku_list(sudoku)
    check = True
    while check:
        check = clean_cell_list_possibilities(cell_list)
        if not check:
            check = apply_only_possibility_in_cell_list(cell_list)
        if not check:
            check = apply_only_possibility_in_area(cell_list)
        if not check:
            check = check_for_only_two_possibilities(cell_list)
        if not check:
            check = start_second_level(cell_list)
    i = 0
    while i < 10:
        print([x.value for x in cell_list if x.line == i])
        i += 1
    i = 0
    while i < 10:
        print([x.possibilities for x in cell_list if x.line == i])
        i += 1


if __name__ == "__main__":
    __main__()
