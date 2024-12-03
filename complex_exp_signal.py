import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the interval for x (arbitrary start and end)
t_start = -4 * np.pi
t_end = 6 * np.pi

# Generate x values within the specified interval
t = np.linspace(t_start, t_end, 1000)
Re = np.cos(t)  # Real Part
Im = np.sin(t)  # Imaginary Part

# Define the tick positions (multiples of π within the range)
tick_positions = np.arange(np.ceil(t_start / np.pi), np.floor(t_end / np.pi) + 1) * np.pi

# Define the tick labels
tick_labels = []
for i in range(int(np.ceil(t_start / np.pi)), int(np.floor(t_end / np.pi)) + 1):
    if i == 0:
        tick_labels.append(r"$0$")
    elif i == 1:
        tick_labels.append(r"$\pi$")
    elif i == -1:
        tick_labels.append(r"$-\pi$")
    else:
        tick_labels.append(r"$%d\pi$" % i)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D curve

ax.set_xlim(t_start, t_end)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

ax.plot(t, Re, Im, label=r"Signal of ${e^{jt}}$", color='b')

proj_plane = t * 0 + 1.04
ax.plot(t, Re, -proj_plane, color="grey")    # real projection
ax.plot(t, proj_plane, Im, color="grey")     # imaginary projection

# Set ticks and labels for the x-axis
ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels, rotation=45)
ax.set_xlabel("t")
ax.set_ylabel("Re")
ax.set_zlabel("Im")

# Add a title
func_name = r"The signal of $e^{jt}$"
interval = f" from {tick_labels[0]} to {tick_labels[-1]}"
title = func_name + interval
ax.set_title(title)

# Add a legend
ax.legend()

# Display the plot
plt.show()
