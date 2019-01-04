import numpy as np
from scipy.spatial import distance

#part a
points = np.loadtxt('6.txt', delimiter = ', ')
xMin, yMin = points.min(axis=0) - 1
xMax, yMax = points.max(axis=0) + 2

xGrid, yGrid = np.meshgrid(np.arange(xMin, xMax), np.arange(xMin, xMax))
targets = np.dstack([xGrid, yGrid]).reshape(-1, 2)

distances = distance.cdist(points, targets, 'cityblock')
closest_origin = np.argmin(distances, axis=0)
min_distances = np.min(distances, axis=0)
competing_filter = (distances == min_distances).sum(axis=0) > 1

closest_origin[competing_filter] = len(points) + 1
closest_origin = closest_origin.reshape(xGrid.shape)
infinites = np.unique(np.vstack([closest_origin[0],
                                 closest_origin[-1],
                                 closest_origin[:, 0],
                                 closest_origin[:, -1]
                                ]))
closest_origin[np.isin(closest_origin, infinites)] = len(points) + 1

print(np.max(np.bincount(closest_origin.ravel())[:-1]))

#part b
origin_distances = distances.sum(axis=0)
region = np.where(origin_distances < 10000, 1, 0)
print(region.sum())
