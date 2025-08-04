import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# --- Utility Functions ---
def is_perfect_cube(n):
    root = round(n ** (1/3))
    return root ** 3 == n

def generate_cube_roots(start, end, include_rational=False):
    numbers = np.arange(start, end + 1)
    irrational = [{"n": n, "cube_root": n ** (1/3)} for n in numbers if not is_perfect_cube(n)]
    rational = [{"n": n, "cube_root": n ** (1/3)} for n in numbers if is_perfect_cube(n)] if include_rational else []
    return irrational, rational

# --- Streamlit App ---
st.set_page_config(page_title="Interactive Cube Root Explorer", layout="wide")
st.title("🧮 Interactive Cube Root Explorer")
st.markdown("Hover over each bar to see the original number and its cube root.")

# --- Sidebar Controls ---
st.sidebar.header("🔧 Controls")
start = st.sidebar.number_input("Start of Range", min_value=1, value=1)
end = st.sidebar.number_input("End of Range", min_value=start + 1, value=1000)
show_rational = st.sidebar.checkbox("Overlay Rational Cube Roots", value=False)

# --- Data Preparation ---
irrational_data, rational_data = generate_cube_roots(start, end, include_rational=show_rational)
irr_df = pd.DataFrame(irrational_data)
irr_df["Type"] = "Irrational"

if show_rational:
    rat_df = pd.DataFrame(rational_data)
    rat_df["Type"] = "Rational"
    full_df = pd.concat([irr_df, rat_df], ignore_index=True)
else:
    full_df = irr_df

# --- Plotting ---
fig = px.histogram(
    full_df,
    x="cube_root",
    color="Type",
    nbins=100,
    hover_data=["n", "cube_root"],
    labels={"cube_root": "Cube Root Value", "n": "Original Number"},
    title=f"Clustering of Cube Roots from {start} to {end}"
)

fig.update_layout(bargap=0.1, title_font_size=18)
st.plotly_chart(fig, use_container_width=True)
