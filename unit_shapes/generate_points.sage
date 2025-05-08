# --- This code generates data that we use in the visualization example: d4_unit_shapes_visualization.py --- #
# --- Input: a list of approximately 4600 quartic number fields with Galois group D4 (and signature 2,1)
# --- Output: an array [[P, disc]] where P is the 'shape' of the unit lattice in the fundamental domain and disc is the absolute discriminant

# This uses `make_data()` which returns a list of dictionaries.
# Each dictionary has a 'field' key corresponding to a quartic D4 field with signature (2,1).
load('D4_fields_data_500000.sage')
data = make_data()

fields = [data[i]['field'] for i in range(len(data))]

grams_discs = [[unit_shape_pari(field), field.disc().abs()] for field in fields]

# Being lazy and adding this for precision errors, we print how many points we actually got and how many failed.
fail_count = 0
points_discs = []
for G, disc in grams_discs:
    try:
        points_discs.append([gram_to_point(G), disc])
    except:
        fail_count += 1
        
print(f"Processed {len(points_discs)} shapes. Skipped {fail_count} due to errors.")

save(points_discs,'points_discs')

