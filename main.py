from m_action import *
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PIL import Image, ImageTk
import tkinter as tk
import io

def calculatorDerivative():
    function = function_entry.get()
    variable = 'x'

    function = correctExpression(function)
    result = oblicz_pochodne(function, variable)

    print("Derivative result:", result)

    latex_result = sp.latex(result)
    result_image = readLatex(latex_result)

    result_label.config(image=result_image)
    result_label.image = result_image


root = tk.Tk()
root.title("Kalkulator Pochodnych")

tk.Label(root, text="Podaj funkcję:").pack()
function_entry = tk.Entry(root)
function_entry.pack(fill=tk.X, padx=10)


calculate_button = tk.Button(root, text="Oblicz Pochodną", command=calculatorDerivative)
calculate_button.pack(pady=10)

# Etykieta do wyświetlania wyniku
result_label = tk.Label(root)
result_label.pack(pady=10)

root.mainloop()
