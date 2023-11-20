import tkinter as tk
from tkinter import ttk
from itertools import permutations, combinations


class CombinationsPermutationsApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de permutaciones y combinaciones")
        self.root.geometry("750x400")

        self.elements_label = ttk.Label(root, text="Elementos (Separados por coma ','):")
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
        self.r_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.r_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.combinatory_result_text = tk.Text(root, height=10, width=40, wrap=tk.WORD)
        self.permutation_result_text = tk.Text(root, height=10, width=40, wrap=tk.WORD)

        self.combinatory_result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.permutation_result_text.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        self.calculate_combinatory_button= ttk.Button(root, text="Calcular Combinación", command=self.calculate_combination)
        self.calculate_combinatory_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.calculate_permutatory_button = ttk.Button(root, text="Calcular Permutación", command=self.calculate_permutation)
        self.calculate_permutatory_button.grid(row=3, column=2, columnspan=2, pady=5)

    def change_state(self):
        print(self.checkbox_value.get())

    def calculate_combination(self):
        elements_str = self.elements_entry.get()
        r_str = self.r_entry.get()

        elements = list(map(str, elements_str.split(' ')))
        r = int(r_str)

        print(r, len(elements))
        if r >= len(elements_str):
            self.combinatory_result_text.delete(1.0, tk.END)
            self.combinatory_result_text.insert(tk.END,"Cadena invalida, r debe ser menor al N de elementos en la lista")
            return
        # Calculate permutations and combinations
        combs = list(combinations(elements, r))

        # Display results in the text widget
        self.combinatory_result_text.delete(1.0, tk.END)
        self.combinatory_result_text.insert(tk.END, f"Combinaciones: {combs}")

    def calculate_permutation(self):
        elements_str = self.elements_entry.get()
        r_str = self.r_entry.get()

        elements = list(map(str, elements_str.split(' ')))
        r = int(r_str)

        print(r, len(elements))
        if r >= len(elements_str):
            self.permutation_result_text.delete(1.0, tk.END)
            self.permutation_result_text.insert(tk.END,"Cadena invalida, r debe ser menor al N de elementos en la lista")
            return
        # Calculate permutations and combinations
        perms = list(permutations(elements, r))

        # Display results in the text widget
        self.permutation_result_text.delete(1.0, tk.END)
        self.permutation_result_text.insert(tk.END, f"Permutaciones: {perms}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CombinationsPermutationsApp(root)
    root.mainloop()
