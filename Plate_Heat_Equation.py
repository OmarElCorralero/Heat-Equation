import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Parameters
Lx = Ly = 1.0           # Length of the square plate (1 meter x 1 meter)
T = 2.0                 # Total simulation time (seconds)
alpha = 0.01            # Thermal diffusivity (m^2/s)

nx = ny = 50            # Grid points in x and y
dx = Lx / (nx - 1)
dy = Ly / (ny - 1)
dt = 0.001              # Time step
nt = int(T / dt)

# Stability parameter
s = alpha * dt / dx**2
print(f"Stability factor (s): {s:.4f} (should be <= 0.25 for 2D explicit)")

# Spatial grid
x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)
X, Y = np.meshgrid(x, y)

# Initial temperature distribution
u = np.zeros((ny, nx))
u[ny//2, nx//2] = 1.0  # Initial heat pulse in the center

# Store solution snapshots for animation
u_all = [u.copy()]

# Time evolution
for n in range(1, nt):
    u_new = u.copy()
    u_new[1:-1, 1:-1] = (
        u[1:-1, 1:-1] +
        s * (u[2:, 1:-1] + u[:-2, 1:-1] +
             u[1:-1, 2:] + u[1:-1, :-2] - 4 * u[1:-1, 1:-1])
    )
    u = u_new
    if n % 20 == 0:
        u_all.append(u.copy())

# ---------- 3D Animation ----------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = [ax.plot_surface(X, Y, u_all[0], cmap='hot', edgecolor='none')]
ax.set_zlim(0, 1.2)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("Temperature (°C)")
ax.set_title("2D Heat Equation: Temperature Evolution")

def update(frame):
    ax.clear()
    ax.set_zlim(0, 1.2)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("Temperature (°C)")
    ax.set_title(f"Time: {frame * dt * 20:.2f} s")
    ax.plot_surface(X, Y, u_all[frame], cmap='hot', edgecolor='none')
    return []

ani = FuncAnimation(fig, update, frames=len(u_all), interval=50)
plt.show()