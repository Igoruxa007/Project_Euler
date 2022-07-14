def delete_empty_frame(cells: list):
    empty_cells = True
    while empty_cells:
        empty_cells = False

        if not sum(cells[0]):
            del cells[0]
            empty_cells = True

        if not sum(cells[-1]):
            del cells[-1]
            empty_cells = True

        if not sum([i[0] for i in cells]):
            for row in cells:
                del row[0]
                empty_cells = True

        if not sum([i[-1] for i in cells]):
            for row in cells:
                del row[-1]
                empty_cells = True

    if len(cells) > len(cells[0]):
        counter = len(cells) - len(cells[0])
        for _ in range(counter):
            for row in cells:
                row.append(0)

    if len(cells) < len(cells[0]):
        counter = len(cells[0]) - len(cells)
        for _ in range(counter):
            cells.append([0 for _ in range(len(cells) + 1)])


def adding_empty_frame(cells):
    for row in cells:
        row.append(0)
        row.insert(0, 0)
    cells.append([0 for _ in range(len(cells) + 2)])
    cells.insert(0, [0 for _ in range(len(cells) + 1)])


def life(cells: list) -> list:
    k, m = [-1, 0, 1], [-1, 0, 1]
    new_cells = []
    for _ in range(len(cells)):
        new_cells.append([0] * len(cells))
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            sum_of_nearby_elements = cells[i - 1][j - 1] + cells[i - 1][j] + cells[i - 1][(j + 1) % len(cells)] + \
                                     cells[i][j - 1] + cells[i][(j + 1) % len(cells)] + \
                                     cells[(i + 1) % len(cells)][j - 1] + cells[(i + 1) % len(cells)][j] + \
                                     cells[(i + 1) % len(cells)][(j + 1) % len(cells)]
            if not cells[i][j] and sum_of_nearby_elements == 3:
                new_cells[i][j] = 1
            if cells[i][j] and sum_of_nearby_elements < 2:
                new_cells[i][j] = 0
            if cells[i][j] and sum_of_nearby_elements > 3:
                new_cells[i][j] = 0
            if cells[i][j] and (sum_of_nearby_elements == 2 or sum_of_nearby_elements == 3):
                new_cells[i][j] = 1
    return new_cells


def get_generation(cells: list, generations: int):
    if not cells: return cells
    for _ in range(generations):
        delete_empty_frame(cells)
        adding_empty_frame(cells)
        cells = life(cells)
    delete_empty_frame(cells)
    return cells


start = [[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]

print(*start, sep='\n')
print(' ')
print(*get_generation(start, 1), sep='\n')
