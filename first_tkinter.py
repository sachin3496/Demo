import tkinter as tk


root = tk.Tk()

label = tk.Label(text="Hello World", fg='white', bg='black', height=10, width=30,
        font=('Times', 40, 'bold'))

label.pack(fill=tk.BOTH, expand=tk.YES)


root.mainloop()
