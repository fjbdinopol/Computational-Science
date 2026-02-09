import math
import matplotlib.pyplot as plt

# --- 1. SETUP ---
# Rocket Cone Dimensions
r = 50   # Radius of the cone base
h = 100  # Height of the cone

# The Iteration Steps (Terms in the series)
terms_list = [20, 40, 60, 100]

# Storage for the graph
gaps = []
areas_trunc = []
areas_round = []

print(f"{'TERMS':<5} | {'PARTIAL PI (Leibniz)':<20} | {'TRUNC (4 dec)':<15} | {'ROUND (4 dec)':<15} | {'GAP (Difference)'}")
print("-" * 90)

# --- 2. LOGIC LOOP ---
for n in terms_list:
    # A. Calculate Pi using Leibniz Series
    # Formula: 4 * (1 - 1/3 + 1/5 - 1/7 ...)
    leibniz_val = 0
    for i in range(n):
        term = (-1)**i / (2*i + 1)
        leibniz_val += term
    
    calc_pi = leibniz_val * 4
    
    # B. Apply Truncation and Rounding Logic (to 4 decimal places)
    # Truncate: Convert to string, slice, convert back
    # Note: We use string formatting because pure math truncation with floats is messy
    str_val = f"{calc_pi:.10f}" # Get enough decimals
    trunc_str = str_val[:6]     # Keep "3.1415" (6 chars)
    pi_trunc = float(trunc_str)
    
    # Round: Standard Python round()
    pi_round = round(calc_pi, 4)
    
    # C. Calculate the GAP
    gap = abs(pi_trunc - pi_round)
    
    # D. Apply to the CONE (Lateral Surface Area)
    # Formula: A = pi * r * sqrt(r^2 + h^2)
    slant_height = math.sqrt(r**2 + h**2)
    area_trunc = pi_trunc * r * slant_height
    area_round = pi_round * r * slant_height
    
    # Store data for plotting
    gaps.append(gap)
    areas_trunc.append(area_trunc)
    areas_round.append(area_round)
    
    # Print exactly like the screenshot
    print(f"{n:<5} | {calc_pi:<20.10f} | {pi_trunc:<15.4f} | {pi_round:<15.4f} | {gap:.4f}")

print("-" * 90)

# --- 3. VISUALIZATION (THE GRAPH) ---
plt.figure(figsize=(10, 6))

# We plot the CONE AREA computed with both methods
plt.plot(terms_list, areas_trunc, marker='x', linestyle='--', color='red', label='Cone Area (Truncated Pi)', markersize=10)
plt.plot(terms_list, areas_round, marker='o', linestyle='-', color='green', label='Cone Area (Rounded Pi)', markersize=8)

plt.title('Impact of Leibniz Series Accuracy on Cone Area', fontsize=14)
plt.xlabel('Number of Terms (Leibniz Iterations)', fontsize=12)
plt.ylabel('Calculated Area of Cone', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()