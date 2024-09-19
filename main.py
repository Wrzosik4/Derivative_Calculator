from m_action import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def insert_into_entry(entry_widget, value):
    entry_widget.insert(tk.END, value)


def create_numeric_keyboard(parent_frame, entry_widget):
    keyboard_frame = ttk.Frame(parent_frame)
    keyboard_frame.pack(pady=10)

    buttons = [
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
        ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
        ('9', '9'), ('0', '0'), ('+', '+'), ('-', '-'),
        ('*', '*'), ('/', '/'), ('(', '('), (')', ')'),
    ]

    row = 0
    col = 0
    for (text, value) in buttons:
        button = ttk.Button(keyboard_frame, text=text, command=lambda v=value: insert_into_entry(entry_widget, v))
        button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        col += 1
        if col > 3:
            col = 0
            row += 1


def create_trig_keyboard(parent_frame, entry_widget):
    trig_frame = ttk.Frame(parent_frame)
    trig_frame.pack(pady=10)

    buttons = [
        ('sin(', 'sin('), ('cos(', 'cos('), ('tan(', 'tan('),
        ('asin(', 'asin('), ('acos(', 'acos('), ('atan(', 'atan('),
        ('e', 'e'), ('^', '**'),
    ]

    row = 0
    col = 0
    for (text, value) in buttons:
        button = ttk.Button(trig_frame, text=text, command=lambda v=value: insert_into_entry(entry_widget, v))
        button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        col += 1
        if col > 2:
            col = 0
            row += 1

def create_log_keyboard(parent_frame, entry_widget):
    trig_frame = ttk.Frame(parent_frame)
    trig_frame.pack(pady=10)

    buttons = [
        ('log(','log('), ('e^','exp('), ('sqrt(','sqrt('),
        ('ln(', 'ln('),
    ]

    row = 0
    col = 0
    for (text, value) in buttons:
        button = ttk.Button(trig_frame, text=text, command=lambda v=value: insert_into_entry(entry_widget, v))
        button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        col += 1
        if col > 2:
            col = 0
            row += 1

def displayLatexResult(result):
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, f"${result}$", fontsize=24, ha='center', va='center')
    ax.axis('off')

    for widget in result_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')

def downloadDerivative():
    function = fun_entry_derivatives.get()
    try:
        result = calculableDerivatives(function)
        displayLatexResult(result)
    except Exception as e:
        displayLatexResult(f'Błąd: {e}')

def downloadIndefiniteIntegral():
    function = fun_entry_integrals.get()
    try:
        result = calculatingTheIndefiniteIntegral(function)
        displayLatexResult(result)
    except Exception as e:
        displayLatexResult(f'Błąd: {e}')

def downloadDefiniteIntegral():
    function = fun_entry_definite_integrals.get()
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        result = definiteIntegralCalculator(function, a, b)
        displayLatexResult(result)
    except ValueError:
        displayLatexResult('Błąd: Proszę wprowadzić poprawne liczby dla a i b.')
    except Exception as e:
        displayLatexResult(f'Błąd: {e}')


root = tk.Tk()
root.title('Kalkulator Równań')
root.geometry('800x800')

# Stylizacja
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 10), padding=6)
style.configure('TNotebook', tabposition='n')
style.configure('TFrame', background='#f0f0f0')

# Zakładki kalkulatora
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill='both', padx=10, pady=10)

# Zakładki na różne typy równań
derivative_frame = ttk.Frame(notebook, padding=10)
integral_frame = ttk.Frame(notebook, padding=10)
definite_integral_frame = ttk.Frame(notebook, padding=10)

notebook.add(derivative_frame, text='Pochodne')
notebook.add(integral_frame, text='Całki Nieoznaczone')
notebook.add(definite_integral_frame, text='Całki Oznaczone')

# Dodanie etykiet i pól wejściowych
ttk.Label(derivative_frame, text='Podaj funkcję:').pack(pady=5)
fun_entry_derivatives = ttk.Entry(derivative_frame, font=('Helvetica', 12))
fun_entry_derivatives.pack(pady=5)

derivatives_button = ttk.Button(derivative_frame, text='Oblicz Pochodną', command=downloadDerivative)
derivatives_button.pack(pady=10)

ttk.Label(integral_frame, text='Podaj funkcję:').pack(pady=5)
fun_entry_integrals = ttk.Entry(integral_frame, font=('Helvetica', 12))
fun_entry_integrals.pack(pady=5)

indefinite_integral_button = ttk.Button(integral_frame, text='Oblicz Całkę Nieoznaczoną', command=downloadIndefiniteIntegral)
indefinite_integral_button.pack(pady=10)

ttk.Label(definite_integral_frame, text='Podaj funkcję:').pack(pady=5)
fun_entry_definite_integrals = ttk.Entry(definite_integral_frame, font=('Helvetica', 12))
fun_entry_definite_integrals.pack(pady=5)

ttk.Label(definite_integral_frame, text='Podaj a:').pack(pady=5)
a_entry = ttk.Entry(definite_integral_frame, font=('Helvetica', 12))
a_entry.pack(pady=5)

ttk.Label(definite_integral_frame, text='Podaj b:').pack(pady=5)
b_entry = ttk.Entry(definite_integral_frame, font=('Helvetica', 12))
b_entry.pack(pady=5)

definite_integral_button = ttk.Button(definite_integral_frame, text='Oblicz Całkę Oznaczoną', command=downloadDefiniteIntegral)
definite_integral_button.pack(pady=10)

def calculatorKeys(frame, entry_widget):
    calc_notebook = ttk.Notebook(frame)
    calc_notebook.pack(expand=1, fill='both')

    numeric_frame = ttk.Frame(calc_notebook, padding=10)
    calc_notebook.add(numeric_frame, text='Numeryczny')
    create_numeric_keyboard(numeric_frame, entry_widget)

    trig_frame = ttk.Frame(calc_notebook, padding=10)
    calc_notebook.add(trig_frame, text='Trygonometryczny')
    create_trig_keyboard(trig_frame, entry_widget)

    log_frame = ttk.Frame(calc_notebook, padding= 10)
    calc_notebook.add(log_frame, text='Logarytmiczne')
    create_log_keyboard(log_frame, entry_widget)


calculatorKeys(derivative_frame, fun_entry_derivatives)
calculatorKeys(integral_frame, fun_entry_integrals)
calculatorKeys(definite_integral_frame, fun_entry_definite_integrals)

# Ramka na wyświetlanie wyników
result_frame = ttk.Frame(root, padding=10)
result_frame.pack(expand=True, fill='both', padx=10, pady=10)

root.mainloop()
