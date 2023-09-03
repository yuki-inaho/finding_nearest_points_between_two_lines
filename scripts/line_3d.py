import numpy as np


class Line3D:
    def __init__(self, base_point: np.ndarray, direction: np.ndarray, length: float = 1.0):
        self._base_point = base_point
        self._direction = direction / np.linalg.norm(direction)  # Normalize direction
        self._length = length

    @property
    def base_point(self):
        return self._base_point

    @property
    def direction(self):
        return self._direction

    @property
    def length(self):
        return self._length

    @property
    def start_point(self):
        return self._base_point - (self._length / 2) * self._direction

    @property
    def end_point(self):
        return self._base_point + (self._length / 2) * self._direction


def random_rotation_matrix():
    # Generate the axis vector of rotation
    axis = np.random.randn(3)
    axis /= np.linalg.norm(axis)

    # Generate the angle of rotation
    theta = np.random.uniform(0, 2 * np.pi)

    # Calculate the rotation matrix with Rodrigues' rotation formula
    cross_product_matrix = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]])
    R = np.eye(3) + np.sin(theta) * cross_product_matrix + (1 - np.cos(theta)) * np.dot(cross_product_matrix, cross_product_matrix)
    return R


def generate_random_line(length=1.0, point_mean=[0, 0, 0], point_std=[0.1, 0.1, 0.1]):
    base_point = np.random.normal(point_mean, point_std)
    direction = np.array([0, 0, 1.0])
    direction_rotated = np.dot(random_rotation_matrix(), direction)
    return Line3D(base_point, direction_rotated, length)
