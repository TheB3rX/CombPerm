import tkinter as tk
from tkinter import ttk, messagebox
from itertools import permutations, combinations


class CombinationsPermutationsApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de permutaciones y combinaciones")
        self.root.geometry("750x400")

        self.elements_label = ttk.Label(root, text="Elementos (Separados por espacio ' '):")
        self.elements_entry = ttk.Entry(root)
        self.checkbox_value = tk.BooleanVar()
        self.checkbox_value.set(False)
        self.type_checkbox = ttk.Checkbutton(root, text="Sin repeticiones?", onvalue=True, offvalue=False,
                                             variable=self.checkbox_value ,command=self.change_state)

        self.elements_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.S)
        self.elements_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self.type_checkbox.grid(row=0, column=2, padx=10, pady=5, sticky=tk.E)

        self.r_label = ttk.Label(root, text="r:")
        self.r_entry = ttk.Entry(root)

        self.comb_text = tk.StringVar()
        self.comb_text.set("Combinaciones")
        self.perm_text = tk.StringVar()
        self.perm_text.set("Permutaciones")

        self.comb_label = ttk.Label(root, text=self.comb_text.get())
        self.perm_label = ttk.Label(root, text=self.perm_text.get())

        self.r_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.r_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.comb_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.perm_label.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        self.combinatory_result_text = tk.Text(root, height=10, width=40, wrap=tk.WORD)
        self.permutation_result_text = tk.Text(root, height=10, width=40, wrap=tk.WORD)

        self.combinatory_result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.permutation_result_text.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

        self.calculate_combinatory_button= ttk.Button(root, text="Calcular Combinación", command=self.calculate_combination)
        self.calculate_combinatory_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.calculate_permutatory_button = ttk.Button(root, text="Calcular Permutación", command=self.calculate_permutation)
        self.calculate_permutatory_button.grid(row=4, column=2, columnspan=2, pady=5)

        self.target_phrase_label = ttk.Label(root, text="Frase Objetivo:")
        self.target_phrase_entry = ttk.Entry(root)
        self.target_phrase_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
        self.target_phrase_entry.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        self.validate_button = ttk.Button(root, text="Validar", command=self.validate_phrase)
        self.validate_button.grid(row=5, column=2, columnspan=2, pady=5)

    def change_state(self):
        print(self.checkbox_value.get())

    def calculate_combination(self):
        elements_str = self.elements_entry.get()
        r_str = self.r_entry.get()

        elements = list(map(str, elements_str.split(' ')))
        r = int(r_str)

        if r >= len(elements_str):
            self.combinatory_result_text.delete(1.0, tk.END)
            self.combinatory_result_text.insert(tk.END,"Cadena invalida, r debe ser menor al N de elementos en la lista")
            messagebox.showerror("Error", "r debe ser un entero y tiene que ser menor a la longitud de los elementos de la cadena")
            return

        self.comb_text.set("Combinaciones")
        self.perm_text.set("Permutaciones")

        # Calculate permutations and combinations
        if self.checkbox_value.get():
            combs = set(combinations(elements, r))
        else:
            combs = list(combinations(elements, r))

        messagebox.showinfo("Información", f"La cantidad de elementos en la lista es: {len(combs)}")
        # Display results in the text widget
        self.comb_text.set(f"Combinación: {len(combs)}")
        self.combinatory_result_text.delete(1.0, tk.END)
        for i in combs:
            self.combinatory_result_text.insert(tk.END, f"{i}\n")

    def calculate_permutation(self):
        elements_str = self.elements_entry.get()
        r_str = self.r_entry.get()

        elements = list(map(str, elements_str.split(' ')))
        r = int(r_str)

        if r >= len(elements):
            self.permutation_result_text.delete(1.0, tk.END)
            print(r)
            print(len(elements))
            self.permutation_result_text.insert(tk.END,"Cadena invalida, r debe ser menor al N de elementos en la lista")
            messagebox.showinfo("error", "r debe ser un entero y tiene que ser menor a la longitud de los elementos de la cadena")
            return

        self.comb_text.set("Combinaciones")
        self.perm_text.set("Permutaciones")

        # Calculate permutations and combinations
        if self.checkbox_value.get():
            perms = set(permutations(elements, r))
        else:
            perms = list(permutations(elements, r))
        # Display results in the text widget
        self.perm_text.set(f"Combinación: {len(perms)}")
        messagebox.showinfo("Información", f"La cantidad de elementos en la permutacion es: {len(perms)}")
        self.permutation_result_text.delete(1.0, tk.END)
        for i in perms:
            self.permutation_result_text.insert(tk.END, f"{i}\n")


    def validate_phrase(self):
        target_phrase = self.target_phrase_entry.get().strip().replace(" ", "")

        if not target_phrase:
            messagebox.showinfo("Error", "Ingrese una frase objetivo.")
            return

        elements_str = self.elements_entry.get()
        r_str = self.r_entry.get()

        elements = list(map(str, elements_str.split(' ')))
        r = int(r_str)

        if r >= len(elements):
            messagebox.showinfo("Error", "Cadena inválida. r debe ser menor al número de elementos en la lista.")
            return

        if self.checkbox_value.get():
            perms = set(permutations(elements, r))
        else:
            perms = list(permutations(elements, r))

        found = False
        for perm in perms:
            if ''.join(perm) == target_phrase:
                found = True
                break

        if found:
            messagebox.showinfo("¡Correcto!", "¡Esa es la frase correcta!")
        else:
            messagebox.showinfo("Incorrecto", "Esa no es la frase correcta.")
if __name__ == "__main__":
    root = tk.Tk()
    app = CombinationsPermutationsApp(root)
    root.mainloop()
