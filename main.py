

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

        polyline = [Pair('*', Pair(beginning_row_index, beginning_col_index))]
        drct = directions(a, beginning_row_index, beginning_col_index)
        polyline = search_polyline(a, polyline, drct)
        #polyline = build_polyline(a, beginning_row_index, beginning_col_index)
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

def directions(tt, ri, ci):
    direct = []
    for i in range(len(tt)):
        for j in range(len(tt[i])):
            d = choose_direction(tt, ri, ci, i, j)
            if d.count(True) > 0:
                direct.append(Pair(tt[i][j].x, Pair(i, j)))
    return direct

def checking_for_elem_in_one_row_or_col(polyline, elem):
    for k in range(len(polyline)-1):
        if polyline[k].second_elem.first_elem == polyline[k+1].second_elem.first_elem == elem.second_elem.first_elem or polyline[k].second_elem.second_elem == polyline[k + 1].second_elem.second_elem == elem.second_elem.second_elem:
            return False
    return True
def checking_for_same_elem(polyline, elem):
    for k in range(len(polyline)):
        if polyline[k].first_elem == elem.first_elem and polyline[k].second_elem.first_elem == elem.second_elem.first_elem and polyline[k].second_elem.second_elem == elem.second_elem.second_elem:
            return False
    return True


def search_polyline(tt, polyline, drct):
    print("polyline: ")
    print_p(polyline)
    print(len(polyline))
    print("directions:")
    print_p(drct)
    if len(polyline) >= 4:
        if polyline[len(polyline)-1].second_elem.first_elem == polyline[0].second_elem.first_elem or polyline[len(polyline)-1].second_elem.second_elem == polyline[0].second_elem.second_elem:
            polyline.append(Pair(polyline[0].first_elem, Pair(polyline[0].second_elem.first_elem, polyline[0].second_elem.second_elem)))
            print("когда добавили *")
            print_p(polyline)

    if len(polyline) >= 4 and polyline[0].first_elem == polyline[len(polyline)-1].first_elem:
        print(polyline[0].first_elem, polyline[len(polyline)-1].first_elem)
        print("answer:")
        print_p(polyline)
        return polyline

    if len(drct) > 0:
        if checking_for_elem_in_one_row_or_col(polyline, drct[0]) and checking_for_same_elem(polyline, drct[0]):
            polyline.append(drct[0])
            drct = directions(tt, drct[0].second_elem.first_elem, drct[0].second_elem.second_elem)
            return search_polyline(tt, polyline, drct)
        else:
            del drct[0]
            return search_polyline(tt, polyline, drct)
    else:
        del polyline[len(polyline)-1]
        drct = directions(tt, polyline[len(polyline)-1].second_elem.first_elem, polyline[len(polyline)-1].second_elem.second_elem)
        del drct[0]
        return search_polyline(tt, polyline, drct)





def print_p(polyline):
    if len(polyline) == 0:
        print("[]")
    else:
        for k in range(len(polyline)):
            print(f"{polyline[k].first_elem, polyline[k].second_elem.first_elem, polyline[k].second_elem.second_elem}", end=' ')
    print('\n_____________________________')


if __name__ == '__main__':
    tt1 = [[5, 2, 4, 1],
           [7, 3, 7, 2],
           [1, 4, 5, 2]]

    s1 = [25, 16, 20] # предложение
    d1 = [15, 25, 11, 10] # спрос


    tt2 = [[2, 7, 2],
           [4, 1, 6],
           [3, 5, 2]]
    s2 = [80, 42, 25]
    d2 = [61, 12, 74]

    tt3 = [[8, 6, 4],
           [5, 9, 4],
           [6, 5, 5],
           [3, 1, 5]]
    s3 = [18, 20, 27, 15]
    d3 = [20, 20, 40]
    a = method_of_potentials(tt3, s3, d3)
    #a = northwest_corner_method(tt2, s2, d2)



