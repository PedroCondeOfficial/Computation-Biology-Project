import numpy as np

particle1 = [110.4, 118.8, 120.76]
particle2 = [39.6, 24.63, 29.24 ]
corner1 = [150,150,150]
corner2 = [0,0,0]
dist = np.linalg.norm(np.array(particle1)-np.array(corner1))
dist2 = np.linalg.norm(np.array(particle2)-np.array(corner2))
print(dist)
print(dist2)
print(147-58-50)