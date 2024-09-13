import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PIL import Image, ImageTk
import tkinter as tk
import io
from sympy.parsing.sympy_parser import parse_expr

def correctExpression(expression):
    expression = expression.replace(' ', '')
    corrected = ''
    length = len(expression)

    for i in range(length):
        corrected += expression[i]
        if (i < length - 1) and (
                (expression[i].isnumeric() or expression[i] in ')') and
                (expression[i + 1].isalpha() or expression[i + 1] == '(')
        ):
            corrected += '*'

    corrected = corrected.replace('exp(', 'exp(')
    return corrected


def readLatex(latex_str):
    fig, ax = plt.subplots(figsize=(5, 2))
    ax.text(0.5, 0.5, f'${latex_str}$', fontsize=20, ha='center', va='center')
    ax.axis('off')

    canvas = FigureCanvas(fig)
    buf = io.BytesIO()
    canvas.print_png(buf)
    plt.close(fig)

    buf.seek(0)
    image = Image.open(buf)
    return ImageTk.PhotoImage(image)


def oblicz_pochodne(fun, var):
    try:
        fun = correctExpression(fun)
        x = sp.symbols(var)
        fun = parse_expr(fun, evaluate=False)
        derivative = sp.diff(fun, x)
        simplified_derivative = sp.simplify(derivative)
        return simplified_derivative
    except Exception as e:
        return f'Wystąpił błąd: {e}'