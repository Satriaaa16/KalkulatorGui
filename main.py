import tkinter as tk
from tkinter import messagebox
import math

# Fungsi untuk menambahkan angka/operator ke layar
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Fungsi untuk menghitung hasil
def btn_equal():
    try:
        global expression
        # Ubah simbol 'X' menjadi '*' dan ':' menjadi '/' untuk evaluasi
        eval_expression = expression.replace('X', '*').replace(':', '/')
        result = str(eval(eval_expression))
        input_text.set(result)
        add_to_history(f"{expression} = {result}")
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Input")
        input_text.set("")
        expression = ""

# Fungsi untuk membersihkan layar
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Fungsi untuk menghapus karakter terakhir
def btn_delete():
    global expression
    expression = expression[:-1]  # Hapus karakter terakhir
    input_text.set(expression)   # Perbarui layar

# Fungsi untuk operasi ilmiah
def scientific_function(func):
    try:
        global expression
        if not expression:  # Jika ekspresi kosong
            raise ValueError("No input")
        value = float(expression)
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            if value <= 0:
                raise ValueError("Math domain error")
            result = math.log10(value)
        elif func == "sqrt":
            if value < 0:
                raise ValueError("Math domain error")
            result = math.sqrt(value)
        input_text.set(str(result))
        add_to_history(f"{func}({expression}) = {result}")
        expression = str(result)
    except:
        messagebox.showerror("Error", "Invalid Input")
        input_text.set("")
        expression = ""

# Fungsi untuk menambahkan ke history logs
def add_to_history(log):
    history_list.insert(tk.END, log)  # Tambahkan log ke Listbox

# Fungsi untuk membersihkan history logs
def clear_history():
    history_list.delete(0, tk.END)  # Hapus semua item di Listbox

# Fungsi untuk membuka GUI baru dengan hanya menampilkan logs history
def open_history_window():
    history_window = tk.Toplevel(root)  # Jendela baru
    history_window.title("History Logs")
    history_window.geometry("400x400")
    
    tk.Label(history_window, text="History Logs", font=('arial', 15)).pack(pady=10)
    
    # Widget Listbox untuk menampilkan history
    logs_listbox = tk.Listbox(history_window, height=20, width=50, font=('arial', 12))
    logs_listbox.pack(pady=10)
    
    # Salin semua item dari history_list ke logs_listbox
    for item in history_list.get(0, tk.END):
        logs_listbox.insert(tk.END, item)
    
    # Tombol untuk menutup jendela
    close_btn = tk.Button(history_window, text="Close", font=('arial', 12), command=history_window.destroy)
    close_btn.pack(pady=10)

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Kalkulator Ilmiah dengan History Logs")
root.geometry("500x600")

# Variabel global untuk menyimpan ekspresi
expression = ""
input_text = tk.StringVar()

# Input layar
input_frame = tk.Frame(root, height=50, bd=5, relief=tk.RIDGE)
input_frame.pack(side=tk.TOP)
input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18), justify='right', bd=5)
input_field.pack(fill=tk.BOTH)

# Tombol-tombol kalkulator
btn_frame = tk.Frame(root)
btn_frame.pack()

# Tombol angka dan operator
buttons = [
    '7', '8', '9', ':', 
    '4', '5', '6', 'X', 
    '1', '2', '3', '-', 
    'C', 'DEL', '=', '+'
]

row = 0
col = 0
for button in buttons:
    if button == "C":
        btn = tk.Button(btn_frame, text=button, font=('arial', 15), height=2, width=6, command=btn_clear)
    elif button == "DEL":
        btn = tk.Button(btn_frame, text=button, font=('arial', 15), height=2, width=6, command=btn_delete)
    elif button == "=":
        btn = tk.Button(btn_frame, text=button, font=('arial', 15), height=2, width=6, command=btn_equal)
    else:
        btn = tk.Button(btn_frame, text=button, font=('arial', 15), height=2, width=6, command=lambda x=button: btn_click(x))
    
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Tombol operasi ilmiah
sci_frame = tk.Frame(root)
sci_frame.pack()

scientific_buttons = ['sin', 'cos', 'tan', 'log', 'sqrt']
for i, func in enumerate(scientific_buttons):
    btn = tk.Button(sci_frame, text=func, font=('arial', 15), height=2, width=8, 
                    command=lambda x=func: scientific_function(x))
    btn.grid(row=0, column=i, padx=5, pady=5)

# Frame untuk history logs
history_frame = tk.Frame(root)
history_frame.pack(pady=10)

# Tombol untuk membuka history logs di GUI baru
open_history_btn = tk.Button(history_frame, text="Open History Logs", font=('arial', 12), command=open_history_window)
open_history_btn.pack(pady=5)

# Widget Listbox untuk menampilkan history
history_list = tk.Listbox(history_frame, height=10, width=50, font=('arial', 12))
history_list.pack()

# Tombol untuk membersihkan history
clear_history_btn = tk.Button(history_frame, text="Clear History", font=('arial', 12), command=clear_history)
clear_history_btn.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()
