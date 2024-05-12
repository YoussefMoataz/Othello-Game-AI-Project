GREEN = "green"
WHITE = "white"
BLACK = "black"
BORDER_WIDTH = 1

def get_index_2d(index):
    i = index // 8
    j = index % 8
    return i, j

def get_index_1d(i, j):
    return i * 8 + j
