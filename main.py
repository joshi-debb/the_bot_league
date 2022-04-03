
from tkinter import *
import tkinter as tk

class display_gui():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.frame = Frame()
        self.text = []

        self.root.title('La Liga Bot')
        self.root.geometry('700x400')

        self.frame.config(width=700, height=400)
        self.frame.place(x=0, y=0)

        self.btn_load_files = Button(self.frame, width = 17, text="Reporte de Errores")
        self.btn_load_files.place(x=563, y=30)

        self.btn_load_files = Button(self.frame, width = 17, text="Limpiar log de Errores")
        self.btn_load_files.place(x=563, y=60)

        self.btn_load_files = Button(self.frame, width = 17, text="Reporte de Tokens")
        self.btn_load_files.place(x=563, y=90)

        self.btn_load_files = Button(self.frame, width = 17, text="Limpiar log de Tokens")
        self.btn_load_files.place(x=563, y=120)

        self.btn_load_files = Button(self.frame, width = 17, text="Manual de Usuario")
        self.btn_load_files.place(x=563, y=150)

        self.btn_load_files = Button(self.frame, width = 17, text="Manual Tecnico")
        self.btn_load_files.place(x=563, y=180)

        self.btn_load_files = Button(self.frame, width = 17, text="Enviar")
        self.btn_load_files.place(x=563, y=348)

        self.text_area = Text(self.frame,  height = 19, width = 65)
        self.text_area.place(x=30, y=30)

        self.text_areas = Text(self.frame,  height = 1, width = 65)
        self.text_areas.place(x=30, y=350)


        self.root.resizable(0,0)
        self.root.mainloop()
    
        
if __name__ == '__main__':
    display_gui()