import matplotlib.pyplot as plt
from itertools import zip_longest

class Polynomial:
    def __init__(self, *coefficients):
        """Input: coefficients are in the form a_n, ..., a_1, a_0"""
        self.coefficients = list(coefficients)  # tuple is turned into a list

    def __repr__(self):
        """Method to return the canonical string representation of a polynomial."""
        return "Polynomial" + str(self.coefficients)

    def __call__(self, x):
        """Make the polynomial instance callable."""
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res

    def degree(self):
        """Return the degree of the polynomial."""
        return len(self.coefficients) - 1

    def __add__(self, other):
        """Overload the + operator for polynomial addition."""
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])

    def __sub__(self, other):
        """Overload the - operator for polynomial subtraction."""
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [t1 - t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])

    def __mul__(self, other):
        """Overload the * operator for polynomial multiplication."""
        result_coeffs = [0] * (self.degree() + other.degree() + 1)
        for i, self_coeff in enumerate(self.coefficients):
            for j, other_coeff in enumerate(other.coefficients):
                result_coeffs[i + j] += self_coeff * other_coeff
        return Polynomial(*result_coeffs)

    def __str__(self):
        """Convert the polynomial to a human-readable string."""
        def x_expr(degree):
            if degree == 0:
                return ""
            elif degree == 1:
                return "x"
            else:
                return f"x^{degree}"

        degree = len(self.coefficients) - 1
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff == 0:
                continue
            term = ""
            if coeff < 0:
                term += "-"
            elif terms:
                term += "+"
            if abs(coeff) != 1 or i == degree:
                term += str(abs(coeff))
            term += x_expr(degree - i)
            terms.append(term)
        return "".join(terms) if terms else "0"

p1 = Polynomial(-3, 0, 0, 2, -7)
p2 = Polynomial(5, -8, 0,0, 10)

print(f"p1(x) = {p1}")
print(f"p2(x) = {p2}")

p_sum = p1 + p2
p_diff = p1 - p2
p_prod = p1 * p2

print(f"p1(x) + p2(x) = {p_sum}")
print(f"p1(x) - p2(x) = {p_diff}")
print(f"p1(x) * p2(x) = {p_prod}")

X = list(range(-20, 21))

F_p1 = [p1(x) for x in X]
F_p2 = [p2(x) for x in X]
F_p_sum = [p_sum(x) for x in X]
F_p_diff = [p_diff(x) for x in X]
F_p_prod = [p_prod(x) for x in X]

# Grafica 1
plt.figure(figsize=(10, 6))
plt.plot(X, F_p1, label="p1(x)")
plt.plot(X, F_p2, label="p2(x)")
plt.plot(X, F_p_sum, label="p1(x) + p2(x)")
plt.plot(X, F_p_diff, label="p1(x) - p2(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráficas de polinomios")
plt.legend()
plt.grid(True)
plt.show()

# Grafica 2
plt.figure(figsize=(10, 6))
plt.plot(X, F_p_prod, label="p1(x) * p2(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica de p1(x) * p2(x)")
plt.legend()
plt.grid(True)
plt.show()
