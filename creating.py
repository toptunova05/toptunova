import numpy as np
def create(n, grid_size=50):
    grid = np.zeros((grid_size, grid_size))
    indices = np.random.choice(grid_size*grid_size, n, replace=False)
    np.put(grid, indices, 1)
    return grid


def save_m(m, filename):
    np.savetxt(filename, m, fmt='%d', delimiter=',')


def user_input():
    return int(input())

a = user_input()

m = create(a)

save_m(m, 'input.txt')