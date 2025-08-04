import streamlit as st
import matplotlib.pyplot as plt
from fractions import Fraction
import math

# --- Utility Functions ---
def generate_rationals_between(a, b, max_denominator=20):
    if a > b:
        a, b = b, a
    result = set()
    for denominator in range(1, max_denominator + 1):
        for numerator in range(int(a * denominator) + 1, int(b * denominator)):
            frac = Fraction(numerator, denominator)
            if a < frac < b:
                result.add(frac)
    return sorted(result)

def is_perfect_square(n):
    root = math.isqrt(n)
    return root * root == n

def is_irrational_sqrt(frac: Fraction):
    return not (is_perfect_square(frac.numerator) and is_perfect_square(frac.denominator))

# --- Plotting Function ---
def plot_irrational_square_roots(rationals, a, b):
    irrationals = [(r, math.sqrt(float(r))) for r in rationals if is_irrational_sqrt(r)]
    x_values = [val for _, val in irrationals]
    labels = [f"√({str(r)})" for r, _ in irrationals]

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.hlines(1, float(a), float(b), colors='lightgrey')

    for x, label in zip(x_values, labels):
        ax.plot(x, 1, 'o', color='purple')
        ax.text(x, 1.08, label, ha='center', va='bottom', fontsize=9, rotation=90)

    ax.set_title(f"Irrational Square Roots of Rationals between {a} and {b}", fontsize=14, pad=20)
    ax.set_yticks([])
    ax.set_xlim(min(x_values) - 0.05, max(x_values) + 0.05)
    ax.set_ylim(0.95, 1.15)
    ax.grid(True, axis='x', linestyle='--', linewidth=0.5)
    fig.tight_layout()
    st.pyplot(fig)

# --- Streamlit App ---
def main():
    st.set_page_config(page_title="Irrational Square Roots", layout="wide")
    st.markdown("## 🧮 Irrational Square Roots of Rational Numbers")
    st.markdown("Explore irrational square roots of rational numbers between two fractions. Created by **Jagdev Singh Dosanjh** — [dosanjhpubsasr.org](https://www.dosanjhpubsasr.org)")

    with st.sidebar:
        st.markdown("### 🔢 Input Fractions")
        num1 = st.number_input("Numerator for A", value=1)
        den1 = st.number_input("Denominator for A", value=2, min_value=1)
        num2 = st.number_input("Numerator for B", value=3)
        den2 = st.number_input("Denominator for B", value=2, min_value=1)
        max_denom = st.slider("Max Denominator", min_value=2, max_value=50, value=10)

    a = Fraction(num1, den1)
    b = Fraction(num2, den2)

    st.markdown(f"### 🔍 Exploring irrational square roots between `{a}` and `{b}`")
    rationals = generate_rationals_between(a, b, max_denom)

    if not rationals:
        st.warning("No rational numbers found between the given range with the selected max denominator.")
    else:
        plot_irrational_square_roots(rationals, a, b)

if __name__ == "__main__":
    main()

# import streamlit as st
# import matplotlib.pyplot as plt
# from fractions import Fraction
# import math

# # --- Utility Functions ---
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

# def is_perfect_square(n):
#     root = math.isqrt(n)
#     return root * root == n

# def is_irrational_sqrt(frac: Fraction):
#     return not (is_perfect_square(frac.numerator) and is_perfect_square(frac.denominator))

# # --- Plotting Function ---
# def plot_irrational_square_roots(rationals, a, b):
#     irrationals = [(r, math.sqrt(float(r))) for r in rationals if is_irrational_sqrt(r)]
#     x_values = [val for _, val in irrationals]
#     labels = [f"√({str(r)})" for r, _ in irrationals]

#     fig, ax = plt.subplots(figsize=(12, 4))
#     ax.hlines(1, float(a), float(b), colors='lightgrey')

#     for x, label in zip(x_values, labels):
#         ax.plot(x, 1, 'o', color='purple')
#         ax.text(x, 1.05, label, ha='center', va='bottom', fontsize=9, rotation=90)

#     ax.set_title(f"Irrational Square Roots of Rationals between {a} and {b}", fontsize=14)
#     ax.set_yticks([])
#     ax.set_xlim(float(a)**0.5 - 0.1, float(b)**0.5 + 0.1)
#     ax.grid(True, axis='x', linestyle='--', linewidth=0.5)
#     st.pyplot(fig)

# # --- Streamlit App ---
# def main():
#     st.set_page_config(page_title="Irrational Square Roots", layout="wide")
#     st.markdown("## 🧮 Irrational Square Roots of Rational Numbers")
#     st.markdown("Explore irrational square roots of rational numbers between two fractions. Created by **Jagdev Singh Dosanjh** — [dosanjhpubsasr.org](https://www.dosanjhpubsasr.org)")

#     with st.sidebar:
#         st.markdown("### 🔢 Input Fractions")
#         num1 = st.number_input("Numerator for A", value=1)
#         den1 = st.number_input("Denominator for A", value=2, min_value=1)
#         num2 = st.number_input("Numerator for B", value=3)
#         den2 = st.number_input("Denominator for B", value=2, min_value=1)
#         max_denom = st.slider("Max Denominator", min_value=2, max_value=50, value=10)

#     a = Fraction(num1, den1)
#     b = Fraction(num2, den2)

#     st.markdown(f"### 🔍 Exploring irrational square roots between `{a}` and `{b}`")
#     rationals = generate_rationals_between(a, b, max_denom)

#     if not rationals:
#         st.warning("No rational numbers found between the given range with the selected max denominator.")
#     else:
#         plot_irrational_square_roots(rationals, a, b)

# if __name__ == "__main__":
#     main()

# # import streamlit as st
# # import matplotlib.pyplot as plt
# # from fractions import Fraction
# # import math

# # def generate_rationals_between(a, b, max_denominator=20):
# #     if a > b:
# #         a, b = b, a
# #     result = set()
# #     for denominator in range(1, max_denominator + 1):
# #         for numerator in range(int(a * denominator) + 1, int(b * denominator)):
# #             frac = Fraction(numerator, denominator)
# #             if a < frac < b:
# #                 result.add(frac)
# #     return sorted(result)

# # def is_perfect_square(n):
# #     root = math.isqrt(n)
# #     return root * root == n

# # def is_irrational_sqrt(frac: Fraction):
# #     # √(a/b) is irrational if a is not a perfect square or b is not a perfect square
# #     return not (is_perfect_square(frac.numerator) and is_perfect_square(frac.denominator))

# # def plot_irrational_square_roots(rationals, a, b):
# #     irrationals = [(r, math.sqrt(float(r))) for r in rationals if is_irrational_sqrt(r)]
# #     x_values = [val for _, val in irrationals]
# #     labels = [f"√({str(r)})" for r, _ in irrationals]

# #     fig, ax = plt.subplots(figsize=(10, 3))  # Slightly taller for vertical labels
# #     ax.hlines(1, float(a), float(b), colors='lightgrey')

# #     for x, label in zip(x_values, labels):
# #         ax.plot(x, 1, 'o', color='purple')
# #         ax.text(x, 1.05, label, ha='center', va='bottom', fontsize=9, rotation=90)

# #     ax.set_title(f"Irrational Square Roots of Rationals between {a} and {b}")
# #     ax.set_yticks([])
# #     ax.set_xlim(float(a)**0.5 - 0.1, float(b)**0.5 + 0.1)
# #     ax.grid(True, axis='x', linestyle='--', linewidth=0.5)
# #     st.pyplot(fig)

# # # def plot_irrational_square_roots(rationals, a, b):
# # #     irrationals = [(r, math.sqrt(float(r))) for r in rationals if is_irrational_sqrt(r)]
# # #     x_values = [val for _, val in irrationals]
# # #     labels = [f"√({str(r)})" for r, _ in irrationals]

# # #     fig, ax = plt.subplots(figsize=(20, 8))
# # #     ax.hlines(1, float(a), float(b), colors='lightgrey')
# # #     for x, label in zip(x_values, labels):
# # #         ax.plot(x, 1, 'o', color='purple')
# # #         ax.text(x, 1.02, label, ha='center', fontsize=20)

# # #     ax.set_title(f"Irrational Square Roots of Rationals between {a} and {b}")
# # #     ax.set_yticks([])
# # #     ax.set_xlim(float(a)**0.5 - 0.1, float(b)**0.5 + 0.1)
# # #     ax.grid(True, axis='x', linestyle='--', linewidth=0.5)
# # #     st.pyplot(fig)

# # def main():
# #     st.title("🧮 Irrational Square Roots of Rational Numbers - https://www.dosanjhpubsasr.org")

# #     col1, col2 = st.columns(2)
# #     with col1:
# #         num1 = st.number_input("Numerator for A", value=1)
# #         den1 = st.number_input("Denominator for A", value=2, min_value=1)
# #     with col2:
# #         num2 = st.number_input("Numerator for B", value=3)
# #         den2 = st.number_input("Denominator for B", value=2, min_value=1)

# #     max_denom = st.slider("Max Denominator", min_value=2, max_value=50, value=5)

# #     a = Fraction(num1, den1)
# #     b = Fraction(num2, den2)
# #     st.write(f"Exploring irrational square roots of rational numbers between `{a}` and `{b}` - By Jagdev Singh Dosanjh")

# #     rationals = generate_rationals_between(a, b, max_denom)
# #     plot_irrational_square_roots(rationals, a, b)

# # if __name__ == "__main__":
# #     main()
