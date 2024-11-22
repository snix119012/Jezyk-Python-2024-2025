import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def rysuj_wielomian(wejscie):
    wielomian_str, przedzial_str = wejscie.split(',')
    x_min, x_max = map(float, przedzial_str.split())
    x_val = np.linspace(x_min, x_max, 200)
    y_val = [eval(wielomian_str, {"x": x, "np": np}) for x in x_val]
    plt.plot(x_val, y_val)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Wykres wielomianu')
    plt.legend()
    plt.grid(True)
    plt.show()
    return float(y_val[0]), float(y_val[-1])


def rysuj_wielomian_sympy(wejscie):
    wielomian_str, przedzial_str = wejscie.split(',')
    x_min, x_max = map(float, przedzial_str.split())
    wielomian_str = wielomian_str.replace("sp.", "")
    x = sp.symbols('x')
    wielomian_sym = sp.sympify(wielomian_str)
    wielomian_func = sp.lambdify(x, wielomian_sym, "numpy")
    x_val = np.linspace(x_min, x_max, 200)
    y_val = wielomian_func(x_val)
    plt.plot(x_val, y_val)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Wykres wielomianu')
    plt.legend()
    plt.grid(True)
    plt.show()
    return float(y_val[0]), float(y_val[-1])

if __name__ == "__main__":
    # Przykładowe wywołanie funkcji z eval
    wejscie1 = "x**3 - 3*x**2 + 3*x - 1, -2 2"
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)

    # Przykładowe wywołanie funkcji z SymPy
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)
