import streamlit as st
import matplotlib.pyplot as plt
from fractions import Fraction

def generate_rationals_between(a, b, max_denom):
    rationals = []
    for denom in range(1, max_denom + 1):
        for num in range(1, denom):
            frac = Fraction(num, denom)
            if a < frac < b:
                rationals.append(frac)
    # Remove duplicates and sort
    unique_rationals = sorted(set(rationals))
    return unique_rationals, len(unique_rationals)

# def generate_rationals_between(a, b, max_denominator=20):
#     if a > b:
#         a, b = b, a
#     result = set()
#     for denominator in range(1, max_denominator + 1):
#         for numerator in range(int(a * denominator) + 1, int(b * denominator)):
#             frac = Fraction(numerator, denominator)
#             if a < frac < b:
#                 result.add(frac)
#     return sorted(result)
a = Fraction(3, 10)
b = Fraction(3, 5)

rationals, count = generate_rationals_between(a, b, max_denom)
st.write(f"🧮 Number of rational numbers between {a} and {b} with denominator ≤ {max_denom}: **{count}**")

st.write("📍 Rational Numbers:")
st.write([str(r) for r in rationals])

def count_vs_denominator(a, b, max_limit):
    counts = []
    for d in range(1, max_limit + 1):
        _, c = generate_rationals_between(a, b, d)
        counts.append(c)
    return counts

if st.checkbox("📊 Show count vs. denominator chart"):
    max_limit = st.slider("Chart Max Denominator", 1, 100, 50)
    counts = count_vs_denominator(a, b, max_limit)
    fig, ax = plt.subplots()
    ax.plot(range(1, max_limit + 1), counts)
    ax.set_xlabel("Max Denominator")
    ax.set_ylabel("Count of Rational Numbers")
    ax.set_title("Density of Rational Numbers")
    st.pyplot(fig)

def plot_rationals(rationals, a, b):
    x_values = [float(r) for r in rationals]
    labels = [str(r) for r in rationals]

    fig, ax = plt.subplots(figsize=(10, 2))
    ax.hlines(1, float(a), float(b), colors='lightgray')
    for x, label in zip(x_values, labels):
        ax.plot(x, 1, 'o', color='blue')
        ax.text(x, 1.02, label, ha='center', fontsize=9)

    ax.set_title(f"Rational Numbers between {a} and {b}")
    ax.set_yticks([])
    ax.set_xticks(sorted(x_values))
    ax.set_xlim(float(a) - 0.1, float(b) + 0.1)
    ax.grid(True, axis='x', linestyle='--', linewidth=0.5)
    st.pyplot(fig)

def main():
    st.title("📊 Rational Number Explorer - https://www.dosanjhpubsasr.org")

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Numerator for A", value=1)
        den1 = st.number_input("Denominator for A", value=2, min_value=1)
    with col2:
        num2 = st.number_input("Numerator for B", value=2)
        den2 = st.number_input("Denominator for B", value=2, min_value=1)

    max_denom = st.slider("Max Denominator", min_value=2, max_value=50, value=10)

    a = Fraction(num1, den1)
    b = Fraction(num2, den2)
    st.write(f"Exploring rational numbers between `{a}` and `{b}` - By Jagdev Singh Dosanjh")

    rationals = generate_rationals_between(a, b, max_denom)
    plot_rationals(rationals, a, b)

if __name__ == "__main__":
    main()
