import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Physical and numerical parameters
L = 1.0                 # Length of the rod (1 meter)
T = 2.0                 # Total simulation time (seconds)
alpha = 0.01            # Thermal diffusivity (m^2/s)

nx = 100                # Number of spatial points
dx = L / (nx - 1)       # Spatial step size
dt = 0.001              # Time step (seconds)
nt = int(T / dt)        # Total number of time steps

# Stability parameter: s <= 0.5 for stability in explicit scheme
s = alpha * dt / dx**2
print(f"Stability factor (s): {s:.4f} (should be <= 0.5 for stability)")

# Spatial grid
x = np.linspace(0, L, nx)

# Initial condition: peak temperature at the center
u = np.zeros(nx)
u[int(nx/2)] = 1.0  # Initial heat pulse

# Store the time evolution of the solution
u_all = [u.copy()]

# Boundary conditions: ends fixed at 0°C
for n in range(1, nt):
    u_new = u.copy()
    for i in range(1, nx - 1):
        u_new[i] = u[i] + s * (u[i+1] - 2*u[i] + u[i-1])
    u = u_new
    if n % 20 == 0:  # Save every 20 steps for animation
        u_all.append(u.copy())

# ---------- Animation ----------
fig, ax = plt.subplots()
line, = ax.plot(x, u_all[0])
ax.set_ylim(0, 1.2)
ax.set_title("Temperature Evolution in the Rod")
ax.set_xlabel("Position (m)")
ax.set_ylabel("Temperature (°C)")

def update(frame):
    line.set_ydata(u_all[frame])
    ax.set_title(f"Time: {frame*dt*20:.2f} s")
    return line,

ani = FuncAnimation(fig, update, frames=len(u_all), interval=50)
plt.show()