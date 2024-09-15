from m_action import *
import tkinter as tk
from tkinter import ttk

def displayResult(result):
    result_label.config(text=f'Wynik: {result}')

def downloadDerivative():
    function = fun_entry_derivatives.get()
    try:
        result = calculableDerivatives(function)
        displayResult(result)
    except Exception as e:
        displayResult(f'Błąd: {e}')

def downloadIndefiniteIntegral():
    function = fun_entry_integrals.get()
    try:
        result = calculatingTheIndefiniteIntegral(function)
        displayResult(result)
    except Exception as e:
        displayResult(f'Błąd: {e}')

def downloadDefiniteIntegral():
    function = fun_entry_definite_integrals.get()
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        result = definiteIntegralCalculator(function, a, b)
        displayResult(result)
    except ValueError:
        displayResult('Błąd: Proszę wprowadzić poprawne liczby dla a i b.')
    except Exception as e:
        displayResult(f'Błąd: {e}')

root = tk.Tk()
root.title('Kalkulator')
root.geometry('600x600')

notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill='both')

# Frames for each tab
derivative_frame = ttk.Frame(notebook)
integral_frame = ttk.Frame(notebook)
definite_integral_frame = ttk.Frame(notebook)

# Add frames to notebook
notebook.add(derivative_frame, text='Pochodne')
notebook.add(integral_frame, text='Całki Nieoznaczone')
notebook.add(definite_integral_frame, text='Całki Oznaczone')

# Pochodne
tk.Label(derivative_frame, text='Podaj funkcje:').pack()
fun_entry_derivatives = tk.Entry(derivative_frame)
fun_entry_derivatives.pack()

derivatives_button = tk.Button(derivative_frame, text='Pochodna', command=downloadDerivative)
derivatives_button.pack()



# Całki nieoznaczone
tk.Label(integral_frame, text='Podaj funkcje:').pack()
fun_entry_integrals = tk.Entry(integral_frame)
fun_entry_integrals.pack()

indefinite_integral_button = tk.Button(integral_frame, text='Całka nieoznaczona', command=downloadIndefiniteIntegral)
indefinite_integral_button.pack()

tk.Label(definite_integral_frame, text='Podaj a:').pack()
a_entry = tk.Entry(definite_integral_frame)
a_entry.pack()

tk.Label(definite_integral_frame, text='Podaj b:').pack()
b_entry = tk.Entry(definite_integral_frame)
b_entry.pack()



# Całki oznaczone
tk.Label(definite_integral_frame, text='Podaj funkcje:').pack()
fun_entry_definite_integrals = tk.Entry(definite_integral_frame)
fun_entry_definite_integrals.pack()

definite_integral_button = tk.Button(definite_integral_frame, text='Całka oznaczona', command=downloadDefiniteIntegral)
definite_integral_button.pack()

result_label = tk.Label(root, text='Wynik:', font = ('Helvetica', 16), anchor = 'center')
result_label.pack(expand=True, fill='both')

root.mainloop()
