import sympy as sp

def simplifyFun(fun):
    try:
        simplified = sp.trigsimp(fun)
        simplified = sp.simplify(simplified)
        simplified = sp.expand(simplified)
        simplified = sp.factor(simplified)
        simplified = sp.collate(simplified, sp.symbols('x'))
        simplified = sp.logcombine(simplified, force=True)

        return simplified
    except Exception as e:
        print(f'Error: {e}')
        return fun


def calculableDerivatives(fun):
    var = sp.symbols('x')
    fun = sp.sympify(fun)
    derivatives = sp.diff(fun,var)
    simplified_derivatives = simplifyFun(derivatives)

    return sp.latex(simplified_derivatives)


def calculatingTheIndefiniteIntegral(fun):
    var = sp.symbols('x')
    fun = sp.sympify(fun)
    integral = sp.integrate(fun,var)
    simplified_integral = simplifyFun(integral)

    return sp.latex(simplified_integral) + ' + C'


def definiteIntegralCalculator(fun, a, b):
    var = sp.symbols('x')
    fun = sp.sympify(fun)
    integral = sp.integrate(fun, (var, a, b))
    simplified_integral = simplifyFun(integral)

    return sp.latex(simplified_integral) + ' + C'
