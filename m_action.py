import sympy as sp

def calculableDerivatives(fun):
    var = sp.symbols('x')
    fun = sp.sympify(fun)
    derivatives = sp.diff(fun,var)
    derivatives.simplify()

    return derivatives

def calculatingTheIndefiniteIntegral(fun):
    var = sp.symbols('x')
    fun = sp.sympify(fun)
    integral = sp.integrate(fun,var)
    integral.simplify()

    return integral

def definiteIntegralCalculator(fun, a, b):
    var = sp.symbols('x')
    fun = sp.sympify(fun)
    integral = sp.integrate(fun, (var, a, b))
    integral.simplify()

    return integral
