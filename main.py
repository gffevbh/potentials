from transport_table_cell import TransportTableCell
from pair_indexes import Pair


def print_a(a):

    for i in range(len(a)):
        for j in range(len(a[0])):
            print(f"(x={a[i][j].x}, c={a[i][j].c})", end=' ')
        print()
    print('_________________________________')

def northwest_corner_method(transport_table, supply, demand):
    a = []
    for i in range(len(transport_table)):
        row = []
        for j in range(len(transport_table[0])):
            elem = TransportTableCell(transport_table[i][j], None)
            row.append(elem)
        a.append(row)

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j].x is None:
                a[i][j].x = min(supply[i], demand[j])
                supply[i] = supply[i] - a[i][j].x
                demand[j] = demand[j] - a[i][j].x

                if supply[i] == 0:
                    for k in range(i, len(a[0])):
                        if a[i][k].x is None:
                            a[i][k].x = '*'
                elif demand[j] == 0:
                    for k in range(j, len(a)):
                        if a[k][j].x is None:
                            a[k][j].x = '*'

    return a

def move_left(transport_table, beginning_row_index, beginning_col_index, final_row_index, final_col_index):
    if transport_table[final_row_index][final_col_index].x != '*' and beginning_row_index <= len(transport_table[0]) and beginning_col_index <= len(transport_table) and final_col_index <= len(transport_table) and beginning_row_index == final_row_index and beginning_col_index > final_col_index:
        return True
    else:
        return False

def move_right(transport_table, beginning_row_index, beginning_col_index, final_row_index, final_col_index):
    if transport_table[final_row_index][final_col_index].x != '*' and beginning_row_index <= len(transport_table[0]) and beginning_col_index <= len(transport_table) and final_col_index <= len(transport_table) and beginning_row_index == final_row_index and beginning_col_index < final_col_index:
        return True
    else:
        return False

def move_down(transport_table, beginning_row_index, beginning_col_index, final_row_index, final_col_index):
    if transport_table[final_row_index][final_col_index].x != '*' and beginning_row_index <= len(transport_table[0]) and final_row_index <= len(transport_table[0]) and beginning_col_index <= len(transport_table) and beginning_row_index < final_row_index and beginning_col_index == final_col_index:
        return True
    else:
        return False

def move_up(transport_table, beginning_row_index, beginning_col_index, final_row_index, final_col_index):
    if transport_table[final_row_index][final_col_index].x != '*' and beginning_row_index <= len(transport_table[0]) and final_row_index <= len(transport_table[0]) and beginning_col_index <= len(transport_table) and beginning_row_index > final_row_index and beginning_col_index == final_col_index:
        return True
    else:
        return False

def choose_direction(transport_table, beginning_row_index, beginning_col_index, final_row_index, final_col_index):
    directions = [False] * 4
    if move_left(transport_table, beginning_row_index, beginning_col_index, final_row_index, final_col_index):
        directions[0] = True
    if move_right(transport_table, beginning_row_index, beginning_col_index, final_row_index, final_col_index):
        directions[1] = True
    if move_down(transport_table, beginning_row_index, beginning_col_index, final_row_index, final_col_index):
        directions[2] = True
    if move_up(transport_table, beginning_row_index, beginning_col_index, final_row_index, final_col_index):
        directions[3] = True
    return directions



def search_directions(transport_table, polyline):
    possible_polylines = []
    for k in range(len(polyline)):
        if polyline[k][len(polyline[k])-1].first_elem == '*':
            return polyline
    print('--------------после 1 итерации------------')
    print_polyline(polyline)

    for k in range(len(polyline)):

        now_polyline = polyline[k]

        bri = now_polyline[len(now_polyline) - 1].second_elem.first_elem
        bci = now_polyline[len(now_polyline) - 1].second_elem.second_elem
        print(f"bri={bri}, bci={bci}, {now_polyline[len(now_polyline) - 1].first_elem}")
        left = now_polyline
        right = now_polyline
        down = now_polyline
        up = now_polyline
        print("now_polyline =", now_polyline, k)
        prev = None

        for i in range(len(transport_table)):
            for j in range(len(transport_table[i])):

                directions = choose_direction(transport_table, bri, bci, i, j)
                print(f"bri={bri}, bci={bci}, ({i, j}), {directions}")

                if prev != 0:
                    if directions[0]:
                        prev = 0
                        elem = Pair(transport_table[i][j].x, Pair(i, j))

                        if elem not in now_polyline:
                            left.append(Pair(transport_table[i][j].x, Pair(i, j)))
                            possible_polylines.append(left)

                            left = left[0:len(left)-1]
                            right = right[0:len(right) - 1]
                            down = down[0:len(down) - 1]
                            up = up[0:len(up) - 1]
                            print(left, right, down, up)

                            print("possible polylines, left")
                            print_polyline(possible_polylines)

                if prev != 1:
                    if directions[1]:
                        prev = 1
                        elem = Pair(transport_table[i][j].x, Pair(i, j))
                        if elem not in now_polyline:

                            right.append(Pair(transport_table[i][j].x, Pair(i, j)))
                            possible_polylines.append(right)

                            left = left[0:len(left) - 1]
                            right = right[0:len(right) - 1]
                            down = down[0:len(down) - 1]
                            up = up[0:len(up) - 1]
                            print(left, right, down, up)

                            print("possible polylines, right")
                            print_polyline(possible_polylines)

                if prev != 2:
                    if directions[2]:
                        prev = 2
                        elem = Pair(transport_table[i][j].x, Pair(i, j))
                        if elem not in now_polyline:

                            down.append(Pair(transport_table[i][j].x, Pair(i, j)))
                            possible_polylines.append(down)
                            print_polyline(polyline)

                            left = left[0:len(left) - 1]
                            right = right[0:len(right) - 1]
                            down = down[0:len(down)-1]
                            up = up[0:len(up) - 1]

                            print("possible polylines, down")
                            print_polyline(possible_polylines)


                if prev != 3:
                    if directions[3]:
                        prev = 3
                        elem = Pair(transport_table[i][j].x, Pair(i, j))
                        if elem not in now_polyline:

                            up.append(Pair(transport_table[i][j].x, Pair(i, j)))

                            possible_polylines.append(up)
                            left = left[0:len(left) - 1]
                            right = right[0:len(right) - 1]
                            down = down[0:len(down) - 1]
                            up = up[0:len(up) - 1]

                            print("possible polylines, up")
                            print_polyline(possible_polylines)

    print_polyline(possible_polylines)

    #ПРОВЕРКА НА ОДИНАКОВЫЕ ЛОМАНЫЕ
    p = []
    for k in range(len(possible_polylines)):
        count = 0
        for i in range(len(possible_polylines[k])):
            for j in range(i+1, len(possible_polylines[k])):
                if possible_polylines[k][i].first_elem == possible_polylines[k][j].first_elem and possible_polylines[k][i].second_elem.first_elem == possible_polylines[k][j].second_elem.first_elem and possible_polylines[k][i].second_elem.second_elem == possible_polylines[k][j].second_elem.second_elem:
                    count += 1
                    break
        if count == 0:
            p.append(possible_polylines[k])
    build_polyline_with_indexes(p)

    #ЕСЛИ МОЖНО ПОПАСТЬ В НАЧАЛЬНЫЙ ЭЛЕМЕНТ - ДОБАВЛЯЕМ ЕГО
    for k in range(len(p)):
        if p[k][len(p[k]) - 1].second_elem.first_elem == p[k][0].second_elem.first_elem or p[k][len(p[k]) - 1].second_elem.second_elem == p[k][0].second_elem.second_elem:
            p[k].append(p[k][0])
    build_polyline_with_indexes(p)

    # ЕСЛИ В ЛОМАНОЙ 3 АРГУМЕНТА СТОЯТ НА ОДНОЙ СТРОКЕ ИЛИ В ОДНОМ СТОЛБЦЕ - НЕ БЕРЕМ ЕЁ
    count = 0
    p1 = []
    for k in range(len(p)):
        if len(p[k]) >= 3:
            for m in range(len(p[k]) - 2):
                if p[k][m].second_elem.first_elem == p[k][m + 1].second_elem.first_elem == p[k][m + 2].second_elem.first_elem or p[k][m].second_elem.second_elem == p[k][m + 1].second_elem.second_elem == p[k][m + 2].second_elem.second_elem:
                    count += 1
        if count == 0:
            p1.append(p[k])
        count = 0

    build_polyline_with_indexes(p1)
    return p1


def build_polyline_with_indexes(p1):
    print('________Ломаные__________')

    for k in range(len(p1)):
        for m in range(len(p1[k])):
            if p1[k][m] == '*':
                print(p1[k][m], end=' ')
            else:
                print(
                    f"{p1[k][m].first_elem, p1[k][m].second_elem.first_elem, p1[k][m].second_elem.second_elem}",
                    end=' ')
        print()

def build_polyline(transport_table, beginning_row_index, beginning_col_index):
    polyline = []

    for i in range(len(transport_table)):
        for j in range(len(transport_table[i])):
            print(f"build_polyline: {beginning_row_index, beginning_col_index, i, j}")
            directions = choose_direction(transport_table, beginning_row_index, beginning_col_index, i, j)
            print(directions)
            possible_polyline_left = []
            possible_polyline_right = []
            possible_polyline_down = []
            possible_polyline_up = []

            if directions[0]:
                possible_polyline_left.append(Pair(transport_table[beginning_row_index][beginning_col_index].x, Pair(beginning_row_index, beginning_col_index)))
                possible_polyline_left.append(Pair(transport_table[i][j].x, Pair(i, j)))
                polyline.append(possible_polyline_left)
                print_polyline(polyline)

            if directions[1]:
                possible_polyline_right.append(Pair(transport_table[beginning_row_index][beginning_col_index].x, Pair(beginning_row_index, beginning_col_index)))
                possible_polyline_right.append(Pair(transport_table[i][j].x, Pair(i, j)))
                polyline.append(possible_polyline_right)
                print_polyline(polyline)

            if directions[2]:
                possible_polyline_down.append(Pair(transport_table[beginning_row_index][beginning_col_index].x, Pair(beginning_row_index, beginning_col_index)))
                possible_polyline_down.append(Pair(transport_table[i][j].x, Pair(i, j)))
                polyline.append(possible_polyline_down)
                print_polyline(polyline)

            if directions[3]:
                possible_polyline_up.append(Pair(transport_table[beginning_row_index][beginning_col_index].x, Pair(beginning_row_index, beginning_col_index)))
                possible_polyline_up.append(Pair(transport_table[i][j].x, Pair(i, j)))
                polyline.append(possible_polyline_up)
                print_polyline(polyline)

    print('_______1 итерация_________')
    print_polyline(polyline)
    print("polyline = ", polyline)

    while polyline[0][len(polyline[0])-1].first_elem != '*':
        polyline = search_directions(transport_table, polyline)
        print("polyline в цикле while = ")
        print_polyline(polyline)
        for i in range(len(polyline)):
            for j in range(len(polyline[i])):
                print(f"{polyline[i][0].first_elem, polyline[i][len(polyline[i])-1].first_elem, len(polyline[i])}")
                if polyline[i][0].first_elem == polyline[i][len(polyline[i])-1].first_elem and len(polyline[i]) >= 5:
                    return polyline[i]

    print("ОКОНЧАТЕЛЬНАЯ ЛОМАНАЯ")
    print_polyline(polyline)
    return polyline[0]




def print_polyline(polyline):
    print('________Ломаные__________')

    for i in range(len(polyline)):
        for j in range(len(polyline[i])):
            if polyline[i][j] == '*':
                print(polyline[i][j], end=' ')
            else:
                print(polyline[i][j].first_elem, end=' ')
        print()

def sum_transport_table(transport_table):
    summ = 0
    for i in range(len(transport_table)):
        for j in range(len(transport_table[0])):
            if transport_table[i][j].x != '*':
                summ += transport_table[i][j].x * transport_table[i][j].c
    return summ


def method_of_potentials(transport_table, supply, demand):

    a = northwest_corner_method(transport_table, supply, demand)
    print_a(a)

    #-----------------------------------------------------------------------------------------#

    deltas = [-1]


    while sum(1 for x in deltas if x >= 0) != len(deltas):

        alphas = ['*'] * len(a)
        alphas[0] = 0
        betas = ['*'] * len(a[0])

        while alphas.count('*') + betas.count('*') != 0:
            for i in range(len(a)):
                for j in range(len(a[0])):
                    if a[i][j].x != '*':
                        if alphas[i] != '*' and betas[j] == '*':
                            betas[j] = a[i][j].c - alphas[i]
                        elif alphas[i] == '*' and betas[j] != '*':
                            alphas[i] = a[i][j].c - betas[j]
                        elif (alphas[i] == '*' and betas[j] == '*') or (alphas[i] != '*' and betas[j] != '*'):
                            continue

        print("alphas = ", alphas)
        print("betas = ", betas)
        print('_______след. итерация________')
        print_a(a)

        deltas = []
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j].x == '*':
                    deltas.append(a[i][j].c - (alphas[i] + betas[j]))

        print("deltas =", deltas)
        if sum(1 for x in deltas if x >= 0) == len(deltas):
            return a

        bri = []
        bci = []
        beginning_of_polyline = min(deltas)
        print(beginning_of_polyline)
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j].x == '*' and a[i][j].c - (alphas[i] + betas[j]) == beginning_of_polyline:
                    bri.append(i)
                    bci.append(j)

        beginning_row_index = bri[0]
        beginning_col_index = bci[0]

        print(f"bri={beginning_row_index}, bci={beginning_col_index}")
        polyline = build_polyline(a, beginning_row_index, beginning_col_index)
        minus_values = []
        for k in range(len(polyline)):
            if k % 2 == 1:
                minus_values.append(polyline[k].first_elem)



        print("minus_values = ", minus_values)
        theta = min(minus_values)
        a[beginning_row_index][beginning_col_index].x = theta
        print(f"minus_values.count(theta) = {minus_values.count(theta)}")




        for k in range(1, len(polyline)-1):
            if k % 2 == 1:
                a[polyline[k].second_elem.first_elem][polyline[k].second_elem.second_elem].x -= theta
            else:
                a[polyline[k].second_elem.first_elem][polyline[k].second_elem.second_elem].x += theta
            if a[polyline[k].second_elem.first_elem][polyline[k].second_elem.second_elem].x == 0:
                a[polyline[k].second_elem.first_elem][polyline[k].second_elem.second_elem].x = '*'

        if minus_values.count(theta) > 1:
            c = 0
            for k in range(1, len(polyline) - 1):
                if k % 2 == 1 and a[polyline[k].second_elem.first_elem][polyline[k].second_elem.second_elem].x == '*' and c == 0:
                    a[polyline[k].second_elem.first_elem][polyline[k].second_elem.second_elem].x = 0
                    c = 1



        print_a(a)
        print("sum =", sum_transport_table(a))

    #--------------------------------------------------------------------------------------#



if __name__ == '__main__':
    transport_table = [[5, 2, 4, 1],
                       [7, 3, 7, 2],
                       [1, 4, 5, 2]]

    supply = [25, 16, 20] # предложение
    demand = [15, 25, 11, 10] # спрос


    tt2 = [[2, 7, 2],
           [4, 1, 6],
           [3, 5, 2]]
    s = [80, 42, 25]
    d = [61, 12, 74]

    tt3 = [[8, 6, 4],
           [5, 9, 4],
           [6, 5, 5],
           [3, 1, 5]]
    s3 = [18, 20, 27, 15]
    d3 = [20, 20, 40]
    a = method_of_potentials(tt3, s3, d3)
