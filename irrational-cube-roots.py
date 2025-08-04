import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

# --- Utility Function ---
def is_perfect_cube(n):
    root = round(n ** (1/3))
    return root ** 3 == n

# --- Generate Irrational Cube Roots ---
rational_numbers = np.arange(1, 1001)
irrational_roots = [n ** (1/3) for n in rational_numbers if not is_perfect_cube(n)]

# --- Streamlit App ---
st.set_page_config(page_title="Irrational Cube Roots", layout="wide")
st.title("Clustering of Irrational Cube Roots of Rational Numbers")
st.markdown("This histogram shows how irrational cube roots of rational numbers (1–1000) cluster along the number line.")

# --- Plotting ---
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(14, 6))
sns.histplot(irrational_roots, bins=100, kde=True, color="purple", ax=ax)

ax.set_xlabel("Cube Root Value", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)
ax.set_title("Clustering of Irrational Cube Roots", fontsize=16, pad=20)
fig.tight_layout()

st.pyplot(fig)

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import math

# # --- Utility Function ---
# def is_perfect_cube(n):
#     root = round(n ** (1/3))
#     return root ** 3 == n

# # --- Generate Irrational Cube Roots ---
# rational_numbers = np.arange(1, 1001)
# irrational_roots = [n ** (1/3) for n in rational_numbers if not is_perfect_cube(n)]

# # --- Plotting ---
# sns.set(style="whitegrid")
# plt.figure(figsize=(14, 6))
# sns.histplot(irrational_roots, bins=100, kde=True, color="purple")

# plt.title("📊 Clustering of Irrational Cube Roots of Rational Numbers", fontsize=16, pad=20)
# plt.xlabel("Cube Root Value", fontsize=14)
# plt.ylabel("Frequency", fontsize=14)
# plt.tight_layout()
# plt.show()
