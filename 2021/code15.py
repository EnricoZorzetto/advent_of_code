import numpy as np
import matplotlib.pyplot as plt
from numba import njit


@njit
def compute_total_costs(nswe, cost, ny, nx):
    totalcost = 1E9 * np.ones(ny * nx)  # cost to get there, for each cell
    visited = [0] # starting point ID
    new_visited = [x for x in visited[1:]]
    old_visited = [x for x in visited[1:]]
    # old_visited = []
    # new_visited = []
    totalcost[0] = 0 # starting cost
    iter = 0; itermax = 20000
    are_equal = False
    while iter < itermax and not are_equal:
        # print('iter = {}'.format(iter))
        # print("visited = {}".format(visited))
        # print("iter = {}; len visited = {}".format(iter, len(visited)))
        # print("iter =", iter, "len visited = ", len(visited))
        for vis in visited:
            neigh0 = nswe[vis, :]
            neigh = neigh0[neigh0 > 0]
            for nei in neigh:
                newcost = totalcost[vis] + cost[nei]
                if newcost < totalcost[nei]: # if that was already cheaper, skip
                    totalcost[nei] = newcost
                    if nei not in new_visited:
                        new_visited.append(nei)
        # print('iter = {}; visited = {}'.format(iter, visited))
        # print('iter = {}; new_visited = {}'.format(iter, new_visited))
        are_equal = visited == old_visited
        # print('iter = {}; equal = {}'.format(iter, are_equal))
        # print('new_visited', new_visited)
        if iter % 2 == 0: # at some point the solution becomes periodic; stop there
            old_visited = visited.copy()
        visited = list(set(new_visited.copy()))
        # new_visited = []
        new_visited = [x for x in visited[len(visited):]]
        iter += 1
    return totalcost


@njit
def get_neigh(tiid_mat):
    ny, nx = tiid_mat.shape
    # nswe = np.zeros((ny*nx, 4)).astype(int)  # neighbour IDs (N, S, W, E)
    nswe = np.zeros((ny*nx, 4))  # neighbour IDs (N, S, W, E)
    for jx in range(nx):
        for iy in range(ny):
            cell_value = tiid_mat[iy, jx] # value correspond to index/value in tiid
            if iy > 0:
                nswe[cell_value, 0] = cell_value - nx  # NORTH
            else:
                nswe[cell_value, 0] = -1
            if iy < ny - 1:
                nswe[cell_value, 1] = cell_value + nx # SOUTH
            else:
                nswe[cell_value, 1] = -1
            if jx < nx - 1:
                nswe[cell_value, 2] = cell_value + 1 # WEST
            else:
                nswe[cell_value, 2] = - 1
            if jx > 0:
                nswe[cell_value, 3] = cell_value - 1 # EAST
            else:
                nswe[cell_value, 3] = -1
    return nswe


def read_data(inputfile):
    with open(inputfile) as file:
        map = np.array( [[char for char in line.rstrip('\n')]
                         for line in file.readlines()] ).astype(int)
    return map


def compound_mats(cost_mat0):
    ny0, nx0 = cost_mat0.shape
    ntiles = 5
    cost_mat = np.zeros((ny0*ntiles, nx0*ntiles)).astype(int)
    for i in range(ntiles):
        for j in range(ntiles):
            cost_mat_i = cost_mat0 + i + j
            for iy in range(ny0):
                for ix in range(nx0):
                    if cost_mat_i[iy, ix] > 9: cost_mat_i[iy, ix] -= 9
            cost_mat[i*ny0:(i+1)*ny0, j*nx0:(j+1)*nx0] = cost_mat_i
    return cost_mat


def compute_path(nswe, tiid_mat, cost_mat, totalcost, ny, nx):
    # now given the map of total cost:
    # start from the end, backtrack the less costly path
    # path = [(ny-1, nx-1)] # coordinate of arrival point
    path = [nx * ny - 1]  # ARRIVAL POINT
    iterc = 0; itercmax = 20000
    completed = False
    while not completed and iterc < itercmax:
        # print(iter, path)
        # get cheapest neigh
        neig0 = nswe[path[-1]]
        neig = neig0[neig0 > -1]
        neig_totalcost = np.array([totalcost[ne] for ne in neig]).astype(int)
        # print(path[-1], neig, neig_totalcost)
        cheapest_loc = neig[ np.argmin(neig_totalcost)]
        path.append( cheapest_loc )
        if 0 in path: completed = True
        if iterc >= itercmax:
            raise Exception('something is horribly wrong!')
        iterc += 1
    # skip the starting point
    path = path[:-1]
    total_risk = 0 # do not count
    path_map = np.zeros((ny,nx)).astype(bool)
    for iy in range(ny):
        for ix in range(nx):
            if tiid_mat[iy, ix] in path:
                path_map[iy, ix] = True
                total_risk += cost_mat[iy, ix]
    return path_map, total_risk



def main_compute_path(cost_mat):
    cost = np.ravel(cost_mat) # row-wise
    ny, nx = cost_mat.shape
    tiid = np.arange(ny*nx).astype(int) # grid cell IDs
    tiid_mat = tiid.reshape(ny,nx)
    nswe = get_neigh(tiid_mat).astype(int)
    totalcost = compute_total_costs(nswe, cost, ny, nx)
    totalcost_mat = totalcost.reshape(ny,nx).astype(float)
    totalcost_mat[totalcost_mat > 1E8] = np.nan # for plotting
    path_map, total_risk = compute_path(nswe, tiid_mat, cost_mat ,totalcost, ny, nx)
    # plt.figure()
    # plt.imshow(cost_mat)
    # plt.colorbar()
    # plt.show()
    # plt.figure()
    # plt.imshow(totalcost_mat)
    # plt.colorbar()
    # plt.show()
    plt.figure()
    plt.imshow(path_map)
    plt.show()
    return total_risk


if __name__ == '__main__':

    # inputfile = 'test_data15.txt'
    inputfile = 'data15.txt'
    cost_mat = read_data(inputfile)
    total_risk_1 = main_compute_path(cost_mat)
    print("part 1:: the total risk is {}".format(total_risk_1))
    cost_mat_2 = compound_mats(cost_mat)
    total_risk_2 = main_compute_path(cost_mat_2)
    print("part 2:: the total risk is {}".format(total_risk_2))
