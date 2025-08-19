# Heat Equation Simulations

This repository contains **numerical simulations of the heat (diffusion) equation** in Python, using an **explicit finite-difference scheme**.  

Two scripts are included:

1. **1D Heat Conduction in a Rod** (`heat_1d_rod.py`)  
2. **2D Heat Conduction in a Square Plate** (`heat_2d_plate.py`)  

Both simulations visualize the **time evolution of temperature** using `matplotlib` animations.

---

## 📖 The Heat Equation

The heat equation models the diffusion of temperature in a medium:

**1D Rod:**
\[
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
\]

**2D Plate:**
\[
\frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)
\]

Where:
- \(u(x,t)\) or \(u(x,y,t)\) is the temperature distribution,
- \(\alpha\) is the thermal diffusivity.

The **explicit finite-difference scheme** is used for time integration, with stability parameters:

- **1D:** \( s = \alpha \frac{dt}{dx^2} \leq 0.5 \)  
- **2D:** \( s = \alpha \frac{dt}{dx^2} \leq 0.25 \)

---

## 🚀 Features

- ✅ Initial condition: **heat pulse** at the center  
- ✅ Explicit finite-difference scheme for numerical integration  
- ✅ Stability check printed before simulation  
- ✅ Animated time evolution using `matplotlib.animation.FuncAnimation`  
- ✅ 1D line plot (rod) and 3D surface plot (plate)  
- ✅ Adjustable parameters: grid size, time step, thermal diffusivity  

---

## 📂 Files

- `heat_1d_rod.py` → Simulates temperature evolution in a **1D rod** and animates it.  
- `heat_2d_plate.py` → Simulates temperature evolution in a **2D square plate** and animates it as a **3D surface plot**.  

---

## ⚙️ Requirements

Python 3.8+ with the following libraries:
- `numpy`
- `matplotlib`

Install dependencies via pip:

```bash
pip install numpy matplotlib
