import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Utility Functions ---
def is_perfect_cube(n):
    root = round(n ** (1/3))
    return root ** 3 == n

def generate_cube_roots(start, end, include_rational=False):
    numbers = np.arange(start, end + 1)
    irrational_roots = [n ** (1/3) for n in numbers if not is_perfect_cube(n)]
    rational_roots = [n ** (1/3) for n in numbers if is_perfect_cube(n)] if include_rational else []
    return irrational_roots, rational_roots

# --- Streamlit App ---
st.set_page_config(page_title="Irrational Cube Root Explorer", layout="wide")
st.title("🧮 Irrational Cube Root Explorer")
st.markdown("Explore how irrational cube roots of rational numbers cluster along the number line.")

# --- Sidebar Controls ---
st.sidebar.header("🔧 Controls")
start = st.sidebar.number_input("Start of Range", min_value=1, value=1)
end = st.sidebar.number_input("End of Range", min_value=start + 1, value=1000)
bins = st.sidebar.slider("Number of Histogram Bins", min_value=10, max_value=200, value=100)
show_rational = st.sidebar.checkbox("Overlay Rational Cube Roots", value=False)

# --- Data Generation ---
irrational_roots, rational_roots = generate_cube_roots(start, end, include_rational=show_rational)

# --- Plotting ---
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(14, 6))
sns.histplot(irrational_roots, bins=bins, kde=True, color="purple", ax=ax, label="Irrational Cube Roots")

if show_rational and rational_roots:
    sns.histplot(rational_roots, bins=bins, kde=False, color="green", ax=ax, label="Rational Cube Roots")

ax.set_xlabel("Cube Root Value", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)
ax.set_title(f"Clustering of Cube Roots from {start} to {end}", fontsize=16, pad=20)
ax.legend()
fig.tight_layout()

st.pyplot(fig)
