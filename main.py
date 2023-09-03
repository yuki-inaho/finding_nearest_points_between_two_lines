import numpy as np
import matplotlib.pyplot as plt
from scripts.line_3d import Line3D, generate_random_line
from scripts.visualization import label2color

np.random.seed(123)


def main():
    length = 1.0
    n_lines = 5

    ax = plt.figure().add_subplot(projection="3d")
    for i in range(n_lines):
        if i == 0:
            line = Line3D(np.array([0, 0, 0]), np.array([0, 0, 1]), length)
            color = [1.0, 0, 0]
        else:
            line = generate_random_line(length)
            color = label2color(i)
        print(f"{i}-th Line color: {color} (R, G, B)")
        ax.plot(
            [line.start_point[0], line.end_point[0]],
            [line.start_point[1], line.end_point[1]],
            zs=[line.start_point[2], line.end_point[2]],
            color=color,
            label=f"Line {i}",
            linewidth=3.0,
        )
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
