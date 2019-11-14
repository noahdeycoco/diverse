# /usr/bin/env python3
# coding: utf-8

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def workworkwork(picture):
    try:
        if isinstance(picture, list):
            graph_data = []
            for y in range(len(picture[0])):  # 0 to 5
                for i in range(len(picture)):  # 0 to 8
                    graph_data.append(picture[i][y])
                    # print(i,y) # to understand indexes

            graph = (''.join(graph_data))
            first_counter = 0
            second_counter = len(picture)
       
            for i in range(len(picture[0])):  # 6 times for 6 lines
                print(graph[int(0+first_counter):int(second_counter)])
                first_counter += len(picture)
                second_counter += len(picture)
        else:
            print('No list, no grid.')
    except Exception:
        print('An error occured.')


if __name__ == '__main__':
    workworkwork(grid)
