import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as ticker

# Load data: an array of points, (x,y), and the corresponding fields absolute discriminant, disc
points_discs = load('points_discs.sobj')
points = [point for point, disc in points_discs]
discs = [disc for points, disc in points_discs]


# Create numpy objects for the array of points and corresponding discriminants
points = np.array(points)  # assuming 'points' is a list of (x, y)
discriminants = np.array(discs)  # matching list of discriminants


# Create figure
fig, ax = plt.subplots(figsize=(6, 8), dpi=300)



# --- F = fundamental domain of the upper half plane modulo GL(2,Z) --- #

# Left boundary of F (square cusp to 'infinty'). i.e. the vertical line from (0, 1) upward
ax.plot([0.0, 0.0], [1.0, 50], color='red', linewidth=1.5, zorder=1)

# Right boundary of F (hexagonal cusp to 'infinty'). i.e. the vertical line from (1/2, sqrt(3)/2) upward
ax.plot([0.5, 0.5], [np.sqrt(3)/2, 50], color='red', linewidth=1.5, zorder=1)

# Bottom boundary of F (square cusp to hexagonal cusp), i.e. the arc of the circle from pi/3 to pi/2 with radius 1
theta = np.linspace(np.pi/3, np.pi/2, 100)
arc_x = np.cos(theta)
arc_y = np.sin(theta)
ax.plot(arc_x, arc_y, color='red', linewidth=1.5, zorder=1)

# --- Plot the points with label coming from the dicriminant ordering --- #
scatter = ax.scatter(
    points[:,0], points[:,1],
    c=discriminants,
    cmap='plasma',
    s=30,
    edgecolor='black',
    linewidths=0.5,
    alpha=1,
    zorder=2
)

# Colorbar for discriminants
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.1)
cbar = plt.colorbar(scatter, cax=cax)
cbar.set_label(r'$|\mathrm{Disc}(K)|$', fontsize=12)

# x-axis ticks
ax.set_xticks([0, 0.25, 0.5])
ax.set_xticklabels([r'$0$', r'$\tfrac{1}{4}$', r'$\tfrac{1}{2}$'])

# label axes
ax.set_xlabel(r'$\mathrm{Re}(z)$')
ax.set_ylabel(r'$\mathrm{Im}(z)$')

# Set axis limits (this fit the data and seemed a bit more aesthetically pleasing)
ax.set_xlim(-.035, .535)
ax.set_ylim(0, 3)

# Optional grid
ax.grid(True, linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig('D4_abs_discs_500000.png', bbox_inches='tight', dpi=300)
plt.show()
# --- the above code produces the image 'D4_abs_discs_500000.png' --- #
