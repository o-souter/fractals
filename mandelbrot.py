import numpy as np
import matplotlib.pyplot as plt
import tqdm
def create_complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))

    return re[np.newaxis, :] + im[:, np.newaxis] * 1j
def z(n, c):
    if n ==0:
        return 0
    else:
        return z(n - 1, c) ** 2 + c

point_count = 1000

def sequence(c, z=0):
    while True:
        yield z
        z = z ** 2 + c

def mandelbrot(candidate):
    return sequence(z=0, c=candidate)

def julia(candidate, parameter):
    return sequence(z=candidate, c=parameter)

def is_stable(c, num_iter):
    z = 0
    for _ in range(num_iter):
        #z = z ** 96 + c
        z = np.sin(z) + c
    return abs(z) <= 2

def get_members(c, num_iter):
    mask = is_stable(c, num_iter)
    return c[mask]

c = create_complex_matrix(-5, 5, -5, 5, pixel_density=1024)
members = get_members(c, num_iter=20)
plt.imshow(is_stable(c, num_iter=20), cmap="binary")
#plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
# for n in range(10):
#     print(f"z({n}) = {z(n, c=1)}")