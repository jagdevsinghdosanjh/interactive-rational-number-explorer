import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define some famous irrational numbers
irrationals = {
    "√2": np.sqrt(2),
    "π": np.pi,
    "e": np.e,
    "φ (Golden Ratio)": (1 + np.sqrt(5)) / 2
}

def plot_irrationals(irrationals, a, b):
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.hlines(1, a, b, colors='lightgrey')

    for label, value in irrationals.items():
        if a < value < b:
            ax.plot(value, 1, 'o', color='red')
            ax.text(value, 1.02, f"{label}\n≈ {value:.5f}", ha='center', fontsize=9)

    ax.set_title(f"Irrational Numbers between {a} and {b}")
    ax.set_yticks([])
    ax.set_xlim(a - 0.1, b + 0.1)
    ax.grid(True, axis='x', linestyle='--', linewidth=0.5)
    st.pyplot(fig)

def main():
    st.title("🔍 Irrational Number Explorer - https://www.dosanjhpubsasr.org")

    a = st.number_input("Start of Interval", value=1.0)
    b = st.number_input("End of Interval", value=4.0)
    st.write(f"Visualizing irrational numbers between `{a}` and `{b}` - By Jagdev Singh Dosanjh")

    plot_irrationals(irrationals, a, b)
    st.write(irrationals)

if __name__ == "__main__":
    main()
