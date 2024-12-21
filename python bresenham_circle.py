import matplotlib.pyplot as plt

def plot_circle_points(center_x, center_y, x, y):
    """Plot symmetric points in a circle"""
    points = [
        (x + center_x, y + center_y), (y + center_x, x + center_y),
        (y + center_x, -x + center_y), (x + center_x, -y + center_y),
        (-x + center_x, -y + center_y), (-y + center_x, -x + center_y),
        (-y + center_x, x + center_y), (-x + center_x, y + center_y)
    ]
    for px, py in points:
        plt.scatter(px, py, color='blue', s=10)
    return points

def bresenham_circle(center_x, center_y, radius):
    """Implement Bresenham's Circle Drawing Algorithm"""
    x, y = 0, radius
    d = 3 - 2 * radius
    points = []

    while x <= y:
        points.extend(plot_circle_points(center_x, center_y, x, y))
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

def main():
    # Input for center and radius
    center_x, center_y = 0, 0
    radius = int(input("Enter the radius of the circle: "))

    # Draw the circle
    points = bresenham_circle(center_x, center_y, radius)

    # Print the points in the 2nd octant
    second_octant_points = [p for p in points if p[0] >= 0 and p[1] >= 0 and p[0] <= p[1]]
    print("Points in the 2nd octant:", second_octant_points)

    # Show the plot
    plt.title("Bresenham's Circle Drawing Algorithm")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    main()
