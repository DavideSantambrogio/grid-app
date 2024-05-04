import tkinter as tk

class GridApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Grid App")

        self.color_frame = self.create_color_frame()
        self.grid_frame = None

    def create_color_frame(self):
        frame = tk.Frame(self.master)
        frame.pack()

        tk.Label(frame, text="Scegli il colore per le linee della griglia:").pack()

        selected_color = tk.StringVar(value="white")

        options = ["white", "black", "red", "yellow", "blue", "magenta"]
        for color in options:
            tk.Radiobutton(frame, text=color, variable=selected_color, value=color, anchor="w", padx=20).pack(fill="x")

        ok_button = tk.Button(frame, text="OK", command=lambda: self.on_color_selected(selected_color.get(), frame))
        ok_button.pack(pady=10)

        return frame

    def on_color_selected(self, color, frame):
        frame.pack_forget()  # Nasconde il frame della selezione del colore
        self.create_grid_frame(color)  # Mostra il frame della griglia con il colore selezionato

    def create_grid_frame(self, color):
        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        self.grid_spacing = 50  # Distanza tra le linee
        self.line_color = color
        self.canvas = tk.Canvas(self.grid_frame, bg="#123456")  # Imposta il colore di sfondo del canvas su magenta
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.draw_grid()

        self.master.attributes("-alpha", 0.5)  # Imposta la trasparenza della finestra
        self.master.attributes("-transparentcolor", "#123456")  # Rendi trasparenti i pixel di colore magenta
        self.master.attributes("-topmost", True)  # Imposta la finestra in primo piano

        self.master.bind("<Configure>", self.on_resize)

    def draw_grid(self):
        self.canvas.delete("grid")  # Cancella eventuali griglie precedenti

        # Calcola il numero di righe e colonne in base alle dimensioni della finestra
        rows = (self.canvas.winfo_height() // self.grid_spacing) + 1
        columns = (self.canvas.winfo_width() // self.grid_spacing) + 1

        # Calcola la coordinata x della linea verticale centrale
        center_x = self.canvas.winfo_width() // 2

        # Disegna le linee verticali
        for i in range(columns):
            x = center_x + (i - columns // 2) * self.grid_spacing
            self.canvas.create_line(x, 0, x, self.canvas.winfo_height(), fill=self.line_color, tags="grid")

        # Calcola la coordinata y della linea orizzontale centrale
        center_y = self.canvas.winfo_height() // 2

        # Disegna le linee orizzontali
        for i in range(rows):
            y = center_y + (i - rows // 2) * self.grid_spacing
            self.canvas.create_line(0, y, self.canvas.winfo_width(), y, fill=self.line_color, tags="grid")

    def on_resize(self, event):
        self.draw_grid()

def main():
    root = tk.Tk()
    app = GridApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
