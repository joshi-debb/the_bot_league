import csv
from tkinter import *
import tkinter as tk
from typing import List

from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader

from os import startfile
import webbrowser

datas = []

class Datas:
    def __init__(self,date,season,journey,team1,team2,gol1,gol2) -> None:
        self.date = date
        self.season = season
        self.journey = journey
        self.team1 = team1
        self.team2 = team2
        self.gol1 = gol1
        self.gol2 = gol2
    
    def show_datas(self):
        print('{} {} {} {} {} {} {}'.format(self.date,self.season,self.journey,self.team1,self.team2,self.gol1,self.gol2))

class Token:
    def __init__(self, token: str, lexeme: str, row: int, col: int) -> None:
        self.token: str = token
        self.lexeme: str = lexeme
        self.row: int = row
        self.col: int = col

    def show_token(self):
        print('Se ha encontrado el token {} que contiene el lexema {} en la fila {} y columna {}'.format(self.token,self.lexeme,self.row, self.col))

class Errors:
    def __init__(self, line: int, col: int, char: str) -> None:
        self.line: int = line
        self.col: int = col
        self.char: str = char
    
    def show_errors(self):
        print('Se ha encontrado el error {} en la fila {} y columna {} '.format(self.char, self.line, self.col))

def Load_CSV(ruta):

    with open(ruta) as File:
        line = csv.reader(File, delimiter = ",")
        next(line,None)
        for index in line:
            date = index[0]
            season = index[1]
            journey = index[2]
            team1 = index[3]
            team2 = index[4]
            gol1 = index[5]
            gol2 = index[6]

            datas.append(Datas(date,season,journey,team1,team2,gol1,gol2))

def AFD(starter: str):
    #agregando al final
    starter += '\n'
    #lista de tokens
    tokens: List[Token] = []
    #lista de errores
    errores: List[Errors] = []
    #estado inicial
    state: int = 0
    tmp_state: int = 0
    #estado actual
    lexeme: str = ''
    #apuntador
    pointer: int = 0
    #Contador de filas y columnas
    row: int = 1
    col: int = 0

    while pointer < len(starter):
        char = starter[pointer]
        # state inicial
        if state == 0:
            #Lista de transiciones
            #Si el caracter es un simbolo [ - ]
            if(ord(char) == 45):
                state = 1
                tmp_state = 1
                pointer += 1
                col += 1
                lexeme += char
            #Si el caracter es una letra, un digito o un simbolo [A-Z,Ñ , a-z,ñ]
            elif((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 164 or ord(char) == 165):
                state = 2
                pointer += 1
                col += 1
                lexeme += char

            #Si el caracter es un digito [ 0-9 ]
            elif (ord(char) >= 48 and ord(char) <= 57):
                state = 3
                pointer += 1
                col += 1
                lexeme += char

            #Si el caracter es un sigo de "menor que" [ < ]
            elif(ord(char) == 60):
                state = 4
                pointer += 1
                col += 1
                lexeme += char
            
            #Si el caracter es un digito [ " ]    
            elif char == '"':
                state = 5
                pointer += 1
                col += 1
                lexeme += char

            # caracteres ignorados
            #si es un salto de linea [\n]
            elif (ord(char) == 10):
                row += 1
                col = 0
                pointer += 1
            #si es un tabulador horizontal [\t]
            elif (ord(char) == 9):
                col += 1
                pointer += 1
            #si es un espacio en blanco ['']
            elif (ord(char) == 32):
                row += 1
                col = 0
                pointer += 1
            else:
                errores.append(Errors(row, col, char))
                pointer += 1
                col += 1

        #estado 1 -> reservadas
        elif state == 1:
            if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 164 or ord(char) == 165):
                state = 6
                pointer += 1
                col += 1
                lexeme += char
            elif(ord(char) == 45):
                state = 0
                tokens.append(Token('simbolo', lexeme, row, col))
                lexeme = ''
            else:
                errores.append(Errors(row, col, char))
                pointer += 1
                col += 1

        elif state == 6:
            if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 164 or ord(char) == 165):
                pointer += 1
                col += 1
                lexeme += char
            else:
                if lexeme in ['RESULTADO','VS','TEMPORADA','JORNADA','GOLES', 'LOCAL', 'VISITANTE', 'TOTAL', 'TABLA', 'PARTIDOS', 'TOP', 'SUPERIOR', 'INFERIOR','ADIOS','-f', '-ji', '-jf', '-n']:
                    tokens.append(Token('Reservada', lexeme, row, col))
                else:
                    errores.append(Errors(row, col, lexeme))
                    pointer += 1
                    col += 1
                state = 0
                lexeme = ''
        
        #estado 2 -> archivos
        elif state == 2:
            if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 164 or ord(char) == 165):
                pointer += 1
                col += 1
                lexeme += char
            elif((ord(char) >= 48 and ord(char) <= 57) or ord(char) == 95 or ord(char) == 46):
                state = 7
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(Errors(row, col, char))
                pointer += 1
                col += 1
            
            state = 0
            tokens.append(Token('Archivo', lexeme, row, col))
            lexeme = ''
        
        elif state == 7:
            if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 164 or ord(char) == 165 or (ord(char) >= 48 and ord(char) <= 57) or ord(char) == 95 or ord(char) == 46):
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(Errors(row, col, char))
                pointer += 1
                col += 1
            
            state = 0
            tokens.append(Token('Archivo', lexeme, row, col))
            lexeme = ''

        #numeros
        elif state == 4:
            if(ord(char) >= 48 and ord(char) <= 57):
                state = 9
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(Errors(row, col, char))
                pointer += 1
                col += 1
        
        elif state == 9:
            if(ord(char) >= 48 and ord(char) <= 57):
                pointer += 1
                col += 1
                lexeme += char
            elif(ord(char) == 45):
                state = 10
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(Errors(row, col, char))
                pointer += 1
                col += 1
        
        elif state == 10:
            if(ord(char) >= 48 and ord(char) <= 57):
                state = 11
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(Errors(row, col, char))
                pointer += 1
                col += 1
        
        elif state == 11:
            if(ord(char) >= 48 and ord(char) <= 57):
                pointer += 1
                col += 1
                lexeme += char
            elif(ord(char) == 60):
                state = 8
                tmp_state = 11
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(Errors(row, col, char))
                pointer += 1
                col += 1      

        elif state == 3:
            if(ord(char) >= 48 and ord(char) <= 57):
                state = 8
                tmp_state = 3
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(Errors(row, col, char))
                pointer += 1
                col += 1
            
            state = 0
            tokens.append(Token('numero', lexeme, row, col))
            lexeme = ''

        #nombre de equipos
        elif state == 5:
            state = 8
            tmp_state = 5
            pointer += 1
            col += 1
            lexeme += char
           
        #estado 8 -> Aceptacion General
        elif state == 8:
            if tmp_state == 11:
                state = 0
                tmp_state = 0
                tokens.append(Token('YYYY', lexeme, row, col))
                lexeme = ''
            elif tmp_state == 3:
                state = 0
                tmp_state = 0
                tokens.append(Token('numero', lexeme, row, col))
                lexeme = ''
            elif tmp_state == 5:
                state = 0
                tmp_state = 0
                tokens.append(Token('equipo', lexeme, row, col))
                lexeme = ''

    return tuple(tokens), tuple(errores)

def process_tokens(tokens):
    env = Environment(loader=FileSystemLoader('Templates/'),
                    autoescape=select_autoescape(['html']))
    template = env.get_template('report_tokens.html')

    html_file = open('oficial_report_tokens.html', 'w+', encoding='utf-8')
    html_file.write(template.render(tokens=tokens))
    html_file.close()
    startfile('oficial_report_tokens.html')

def process_errors(errs):
    env = Environment(loader=FileSystemLoader('Templates/'),
                    autoescape=select_autoescape(['html']))
    template = env.get_template('report_errors.html')

    html_file = open('oficial_report_errors.html', 'w+', encoding='utf-8')
    html_file.write(template.render(errs=errs))
    html_file.close()
    startfile('oficial_report_errors.html')

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

        self.btn_load_files = Button(self.frame, width = 17, text="Enviar", command = self.getText_entry)
        self.btn_load_files.place(x=563, y=348)

        self.chat_area = Text(self.frame,  height = 19, width = 65)
        self.chat_area.place(x=30, y=30)
        self.chat_area.configure(state="disable")

        self.text_area = Entry(self.frame,  height = 1, width = 65)
        self.text_area.place(x=30, y=350)

        self.root.resizable(0,0)
        self.root.mainloop()
    
    def getText_entry(self):
        self.text = (self.text_area.get(1.0, tk.END+"-1c"))
    
    def clearText_area(self):
        self.chat_area.delete("1.0","end")

    def analizer(self):
        self.getText_entry()
        tokens, errors = AFD(self.text)

        if len(tokens) != 0:
            for i in tokens:
                i.show_token()
        else:
            print(' > No hay tokens')
        if len(errors) != 0:
            print('<>=<>=<>=<>=<>=<>=<>=<>=<>=<> ERRORES <>=<>=<>=<>=<>=<>=<>=<>=<>=<>')
            for j in errors:
                j.show_errors()
        else:
            print(' > No hay errores')

        if len(self.text) != 0:
            print(' > Reporte de Tokens')
            process_tokens(tokens)
        
            print(' > Reporte de Errores')
            process_errors(errors)
        else:
            print(' > No hay nada que reportar')
    
        
if __name__ == '__main__':
    Load_CSV('Files\LaLigaBot-LFP.csv')
    display_gui()
    