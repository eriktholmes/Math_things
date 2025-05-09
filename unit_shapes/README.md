# Unit Lattice Shapes of D₄ Fields

This folder contains code and data used to visualize the shapes of unit lattices for quartic number fields with Galois group $D_4$.

In our research, we compute the unit log lattice of each field, project it to the upper half-plane, and apply a reduction algorithm to place it in the standard fundamental domain for $\mathcal{F} = \mathrm{GL}_2(\mathbb{Z}) \backslash \mathbb{H}$. Each point is then colored by the absolute value of the field discriminant.

## Plot Preview
A rank 2 lattice has a shape lying in $\mathcal{F}$, which is given by the following plot (code for this to come!):
![Space of shapes of rank 2 unit lattices](https://github.com/user-attachments/assets/80b26cdf-290f-4894-8e4b-8b1f502aa06f)


The plot below shows unit lattice shapes of all $D_4$ fields with $|\mathrm{Disc}(K)| \leq 500,000$:

![D₄ unit lattice shapes](/unit_shapes/D4_abs_disc_500000.png)

- More to come!
---

## Contents

- `generate_points_discs.sage`: Generates `[point, discriminant]` pairs and saves them as `points_discs.sobj`. Requires:
  - `D4_fields_data_500000.sage` (provides a list of $D_4$ fields downloaded from the [LMFDB](https://www.lmfdb.org/)
- `points_discs.sobj`: Precomputed unit shape + discriminant data.
- `d4_unit_shapes_visualization.py`: Python script to generate the final plot using `matplotlib`.
- `D4_abs_disc_500000.png`: Output plot.

---

