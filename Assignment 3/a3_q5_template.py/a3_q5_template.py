def index_sort(table_matrix):
    index_list = list(range(len(table_matrix)))

    for i in range(len(index_list) - 1):
        min_index = i
        for j in range(i + 1, len(index_list)):
            for col in range(len(table_matrix[0])):
                if table_matrix[index_list[j]][col] < table_matrix[index_list[min_index]][col]:
                    min_index = j
                elif table_matrix[index_list[j]][col] > table_matrix[index_list[min_index]][col]:
                    break

        index_list[i], index_list[min_index] = index_list[min_index], index_list[i]

    return index_list

table1 = [
    ['Miley Cyrus', 164, 106],
    ['Geri Halliwell', 157.5, 107],
    ['Madonna', 162.6, 107],
    ['Fergie/Stacy Ferguson', 158.8, 108],
    ['Victoria Beckham', 167.6, 108],
    ['Penelope Cruz', 172.7, 109],
    ['ELVIS PRESLEY', 182.2, 165],
    ['CHARLIE CHAPLIN', 162.6, 165],
    ['LARRY FINE', 163, 165],
    ['KIEFER SUTHERLAND', 174, 168],
    ['Raven Symone', 180.3, 170],
    ['KURT RUSSELL', 176, 170],
    ['John Wayne', 193, 170]
]

result1 = index_sort(table1)
print(result1)

table2 = [
    ['chevrolet', 'hatchback', 88.4, 141.1, 'l', 'three', 48, 47, 5151],
    ['mazda', 'hatchback', 93.1, 159.1, 'ohc', 'four', 68, 30, 5195],
    ['toyota', 'hatchback', 95.7, 158.7, 'ohc', 'four', 62, 35, 6348],
    ['mitsubishi', 'hatchback', 93.7, 157.3, 'ohc', 'four', 68, 37, 5389],
    ['mazda', 'hatchback', 93.1, 159.1, 'ohc', 'four', 68, 31, 6095],
    ['mitsubishi', 'hatchback', 93.7, 157.3, 'ohc', 'four', 68, 31, 5889],
    ['dodge', 'hatchback', 93.7, 157.3, 'ohc', 'four', 68, 31, 6229],
    ['chevrolet', 'hatchback', 94.5, 155.9, 'ohc', 'four', 70, 38, 6295],
    ['toyota', 'hatchback', 95.7, 158.7, 'ohc', 'four', 62, 31, 6338],
    ['dodge', 'hatchback', 93.7, 157.3, 'ohc', 'four', 68, 31, 7377],
    ['toyota', 'hatchback', 95.7, 158.7, 'ohc', 'four', 62, 31, 6488],
    ['chevrolet', 'sedan', 94.5, 158.8, 'ohc', 'four', 70, 38, 6575]
 ]

result2 = index_sort(table2)
print(result2)
