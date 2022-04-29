import csv
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from tokenize import Token
from typing import List, Type
from enum import Enum
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
import sys
from os import startfile
import webbrowser

datas = []
tokens = []
errors = []
tokens_list = []
errors_list = []
syntaxE_list = []
error_general = []
syntaxErrs = []
error = []
journeyses = []
tableses = []
seasonses = []
seasonses2 = []
partidoses = []
puntos = []
puntos2 = []

class journeys():
    def __init__(self, journey,team1,gol1,team2,gol2) -> None:
        self.journey = journey
        self.team1 = team1
        self.team2 = team2
        self.gol1 = gol1
        self.gol2 = gol2

class partidos():
    def __init__(self, journey,team1,gol1,team2,gol2) -> None:
        self.journey = journey
        self.team1 = team1
        self.team2 = team2
        self.gol1 = gol1
        self.gol2 = gol2

class punto():
    def __init__(self,team,points) -> None:
        self.name = team
        self.points = points

class punto2():
    def __init__(self,team,points) -> None:
        self.name = team
        self.points = points

class tables2():
    global puntos2 
    def __init__(self, journey,team1,gol1,team2,gol2,ids) -> None:
        self.journey = journey
        self.team1: str = str(team1)
        self.team2: str = str(team2)
        self.gol1: int = int(gol1)
        self.gol2: int = int(gol2)
        self.id: str = ids

        self.points1: int = 0
        self.points2: int = 0

        if gol1 > gol2:
            self.points1 += 3
        if gol1 < gol2:
            self.points2 += 3
        if gol1 == gol2:
            self.points1 += 1
            self.points2 += 1

            aux1 = ''
            aux2 = ''
        
        try:
            if len(puntos2) == 0:
                puntos2.append(punto2(self.team1,self.points1))
                puntos2.append(punto2(self.team2,self.points2))

            else:
                
                if ids == 'topSuperior':
                    aux1:punto2 = buscar2(self.team1)
                    aux2:punto2 = buscar2(self.team2)
                elif ids == 'topInferior':
                    aux1:punto2 = buscar3(self.team1)
                    aux2:punto2 = buscar3(self.team2)

                if aux1 != None or aux2 != None:
                    if aux1.name == self.team1 or aux2.name == self.team1:
                        aux1.points += self.points1
                    elif aux2.name == self.team2 or aux1.name == self.team2:
                        aux2.points += self.points2
                else:
                    puntos2.append(punto2(self.team1,self.points1))
                    puntos2.append(punto2(self.team2,self.points2))
        except:
            print('error')

class tables():
    global puntos 
    def __init__(self, journey,team1,gol1,team2,gol2) -> None:
        self.journey = journey
        self.team1: str = str(team1)
        self.team2: str = str(team2)
        self.gol1: int = int(gol1)
        self.gol2: int = int(gol2)

        self.points1: int = 0
        self.points2: int = 0

        if gol1 > gol2:
            self.points1 += 3
        if gol1 < gol2:
            self.points2 += 3
        if gol1 == gol2:
            self.points1 += 1
            self.points2 += 1

            aux1 = ''
            aux2 = ''
        
        try:
            if len(puntos) == 0:
                puntos.append(punto(self.team1,self.points1))
                puntos.append(punto(self.team2,self.points2))
            else:
                aux1:punto = buscar(self.team1)
                aux2:punto = buscar(self.team2)

                if aux1 != None or aux2 != None:
                    if aux1.name == self.team1 or aux2.name == self.team1:
                        aux1.points += self.points1
                    elif aux2.name == self.team2 or aux1.name == self.team2:
                        aux2.points += self.points2
                else:
                    puntos.append(punto(self.team1,self.points1))
                    puntos.append(punto(self.team2,self.points2))
        except:
            print('error')

def buscar(nombre):
    
    punto_ord = clasifications()
    
    for i in range(len(punto_ord)):
        if punto_ord[i].name == nombre:
            return punto_ord[i]
        else:
            pass

def buscar2(nombre):

    punto_ord = clasifications2()
    
    for i in range(len(punto_ord)):
        if punto_ord[i].name == nombre:
            return punto_ord[i]
        else:
            pass

def buscar3(nombre):

    punto_ord = clasifications3()
    
    for i in range(len(punto_ord)):
        if punto_ord[i].name == nombre:
            return punto_ord[i]
        else:
            pass

def bubble_sort_UP(data):
    for i in range(len(data) - 1):
        for j in range(0, len(data) - i - 1):
            if data[j].points < data[j + 1].points:
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data

def bubble_sort_DOWN(data: List[punto]):
    for i in range(len(data) - 1):
        for j in range(0, len(data) - i - 1):
            if data[j].points > data[j + 1].points:
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data

def clasifications():
    global puntos
    puntos_ord = bubble_sort_UP(puntos)
    return puntos_ord

def clasifications2():
    global puntos2
    puntos_ord = bubble_sort_UP(puntos2)
    return puntos_ord

def clasifications3():
    global puntos2
    puntos_ord = bubble_sort_DOWN(puntos2)
    return puntos_ord       

class Comand():
    def __init__(self) -> None:
        self.id = ''
        self.num1 = 0
        self.num2 = 0
        self.season = ''
        self.team1 = ''
        self.team2 = ''
    
    def show_cmds(self):
        print('ID:{}, N:{} N:{} team1:{} team2:{} YYYY:{}'.format(self.id,self.num1,self.num2,self.team1,self.team2,self.season))

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

class Types(Enum):
    no_one = 0
    res_result = 1
    res_vs =2
    res_temp = 3
    res_jorn = 4
    res_goles = 5
    res_local = 6
    res_visitante = 7
    res_total = 8
    res_tabla = 9
    res_partidos = 10
    res_top = 11
    res_sup = 12
    res_inf = 13
    res_adios = 14
    tk_flag_F = 15
    tk_flag_JI = 16
    tk_flag_JF =17
    tk_flag_N = 18
    tk_ID = 19
    tk_num = 20
    tk_year = 21
    string = 22
    empty = 23

class Token:
    def __init__(self, token: Types, lexeme: str, row: int, col: int) -> None:
        self.token: Types = token
        self.lexeme: str = lexeme
        self.row: int = row
        self.col: int = col

    def show_token(self):
        print('Se ha encontrado el token {} que contiene el lexeme {} en la fila {} y columna {}'.format(self.token,self.lexeme,self.row, self.col))

class LexicError:
    def __init__(self, line: int, col: int, char: str) -> None:
        self.line: int = line
        self.col: int = col
        self.char: str = char

    def show_LexicErrors(self):
        print('Se ha encontrado el error {} en la fila {} y columna {} '.format(self.char, self.line, self.col))

class SintaxError:
    def __init__(self, line: int, col: int, last_token: Types, expected_tokens: List[Types]) -> None:
        self.line: int = line
        self.col: int = col
        self.last_token: Types = last_token
        self.expected_tokens: List[Types] = expected_tokens
    
    def show_sitaxErrors(self):
        print('Error sintactico en la fila {} y columna {} , token {} , token esperado {} '.format(self.line, self.col, self.last_token, self.expected_tokens))

class Syntax:
    def __init__(self, tokens: List[Token]):
        self.preanalisis: Types = Types.no_one
        self.index: int = 0
        self.lista: List[Token] = tokens
        self.lista.append(Token(Types.empty, None, None, None))
        self.preanalisis: Types = self.lista[self.index].token
        self.errors: List[SintaxError] = []

    def startup(self):
        self.start()
        return self.errors

    def review(self, tipos_validos: List[Types]):
        if self.preanalisis not in tipos_validos:
            Token = self.lista[self.index]
            self.errors.append(
                SintaxError(Token.row, Token.col, Token.token, tipos_validos))
            self.retake()

        if self.preanalisis != Types.empty:
            self.index += 1
            self.preanalisis = self.lista[self.index].token

    def start(self):
        if self.preanalisis == Types.res_result:
            self.resultado()
            self.retake()
        elif self.preanalisis == Types.res_jorn:
            self.jornada()
            self.retake()
        elif self.preanalisis == Types.res_goles:
            self.goles()
            self.retake()
        elif self.preanalisis == Types.res_tabla:
            self.tabla()
            self.retake()
        elif self.preanalisis == Types.res_partidos:
            self.partidos()
            self.retake()
        elif self.preanalisis == Types.res_top:
            self.top()
            self.retake()
        elif self.preanalisis == Types.res_adios:
            self.adios()
            self.retake()

    def retake(self):
        if self.preanalisis == Types.res_result:
            self.resultado()
            self.retake()
        elif self.preanalisis == Types.res_jorn:
            self.jornada()
            self.retake()
        elif self.preanalisis == Types.res_goles:
            self.goles()
            self.retake()
        elif self.preanalisis == Types.res_tabla:
            self.tabla()
            self.retake()
        elif self.preanalisis == Types.res_partidos:
            self.partidos()
            self.retake()
        elif self.preanalisis == Types.res_top:
            self.top()
            self.retake()
        elif self.preanalisis == Types.res_adios:
            self.adios()
            self.retake()

    def resultado(self):
        self.review([Types.res_result])
        self.review([Types.string])
        self.review([Types.res_vs])
        self.review([Types.string])
        self.review([Types.res_temp])
        self.review([Types.tk_year])
    
    def jornada(self):
        self.review([Types.res_jorn])
        self.review([Types.tk_num])
        self.review([Types.res_temp])
        self.review([Types.tk_year])
        self.jornada2()

    def jornada2(self):
        if self.preanalisis == Types.tk_flag_F:
            self.review([Types.tk_flag_F])
            self.review([Types.tk_ID])          
        else:
            pass    

    def goles(self):
        self.review([Types.res_goles])
        self.cond()    

    def cond(self):
        if self.preanalisis == Types.res_local:
            self.review([Types.res_local])
            self.review([Types.string])
            self.review([Types.res_temp])
            self.review([Types.tk_year])
        elif self.preanalisis == Types.res_visitante:
            self.review([Types.res_visitante])
            self.review([Types.string])
            self.review([Types.res_temp])
            self.review([Types.tk_year])
        elif self.preanalisis == Types.res_total:
            self.review([Types.res_total])
            self.review([Types.string])
            self.review([Types.res_temp])
            self.review([Types.tk_year])

    def tabla(self):
        self.review([Types.res_tabla])
        self.review([Types.res_temp])
        self.review([Types.tk_year])
        self.tabla2()
    
    def tabla2(self):
        if self.preanalisis == Types.tk_flag_F:
            self.review([Types.tk_flag_F])
            self.review([Types.tk_ID]) 
        else:
            pass
    
    def partidos(self):
        self.review([Types.res_partidos])
        self.review([Types.string])
        self.review([Types.res_temp])
        self.review([Types.tk_year])
        self.partidos2()

    def partidos2(self):
        if self.preanalisis == Types.tk_flag_F:
            self.review([Types.tk_flag_F])
            self.review([Types.tk_ID])
        elif self.preanalisis == Types.tk_flag_JI:
            self.review([Types.tk_flag_JI])
            self.review([Types.tk_num])
        elif self.preanalisis == Types.tk_flag_JF:
            self.review([Types.tk_flag_JF])
            self.review([Types.tk_num]) 
        else:
            pass

    def top(self):
        self.review([Types.res_top])
        self.cond2()

    def cond2(self):
        if self.preanalisis == Types.res_sup:
            self.review([Types.res_sup])
            self.review([Types.res_temp])
            self.review([Types.tk_year])
            self.top2()

        elif self.preanalisis == Types.res_inf:
            self.review([Types.res_inf])  
            self.review([Types.res_temp])
            self.review([Types.tk_year])
            self.top2()

    def top2(self):
        if self.preanalisis == Types.tk_flag_N:
            self.review([Types.tk_flag_N])
            self.review([Types.tk_num])
        else:
            pass
    
    def adios(self):
        self.review([Types.res_adios])
        
def AFD(starter: str):
    #agregando al final
    starter += '\n'
    #lista de tokens
    tokens: List[Token] = []
    #lista de errores
    errores: List[LexicError] = []
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
            
            #Si el caracter es una comilla doble [ " ]    
            elif (ord(char) == 34):
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
                col += 1
                pointer += 1

            else:
                errores.append(LexicError(row, col, char))
                pointer += 1
                col += 1

        #estado 1 -> banderas
        elif state == 1:
            if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 164 or ord(char) == 165):
                state = 6
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(LexicError(row, col, char))
                pointer += 1
                col += 1

        elif state == 6:
            if((ord(char) >= 97 and ord(char) <= 122) or ord(char) == 164):
                pointer += 1
                col += 1
                lexeme += char
            else:
                if lexeme in ['-f', '-ji', '-jf', '-n']:
                    switcher = {
                        '-f': Types.tk_flag_F, 
                        '-ji': Types.tk_flag_JI, 
                        '-jf': Types.tk_flag_JF, 
                        '-n': Types.tk_flag_N
                    }
                    types: Types = switcher.get(lexeme.lower())
                    tokens.append(Token(types, lexeme, row, col))
                else:
                    errores.append(LexicError(row, col, lexeme))
                    pointer += 1
                    col += 1
                state = 0
                lexeme = ''
        
        #estado 2 -> archivos
        #reporte
        elif state == 2:
            if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 164 or ord(char) == 165):
                pointer += 1
                col += 1
                lexeme += char

                if lexeme in ['RESULTADO','VS','TEMPORADA','JORNADA','GOLES', 'LOCAL', 'VISITANTE', 'TOTAL', 'TABLA', 'PARTIDOS', 'TOP', 'SUPERIOR', 'INFERIOR','ADIOS']:
                    
                    switcher = {
                        'RESULTADO': Types.res_result,
                        'VS': Types.res_vs,
                        'TEMPORADA': Types.res_temp,
                        'JORNADA': Types.res_jorn,
                        'GOLES': Types.res_goles,
                        'LOCAL': Types.res_local, 
                        'VISITANTE': Types.res_visitante, 
                        'TOTAL': Types.res_total, 
                        'TABLA': Types.res_tabla, 
                        'PARTIDOS': Types.res_partidos, 
                        'TOP': Types.res_top, 
                        'SUPERIOR': Types.res_sup, 
                        'INFERIOR': Types.res_inf,
                        'ADIOS': Types.res_adios
                    }
                    
                    types: Types = switcher.get(lexeme)
                    tokens.append(Token(types, lexeme, row, col))
                    state = 0
                    lexeme = ''
            else:
                if((ord(char) >= 48 and ord(char) <= 57) or ord(char) == 95 or ord(char) == 46):
                    state = 7
                    pointer += 1
                    col += 1
                    lexeme += char 
                else:
                    state = 0
                    tokens.append(Token(Types.tk_ID, lexeme, row, col))
                    lexeme = ''
            
        elif state == 7:
            if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 164 or ord(char) == 165 or (ord(char) >= 48 and ord(char) <= 57) or ord(char) == 95 or ord(char) == 46):
                pointer += 1
                col += 1
                lexeme += char
            else:
                state = 0
                tokens.append(Token(Types.tk_ID, lexeme, row, col))
                lexeme = ''     

        #numeros
        elif state == 4:
            if(ord(char) >= 48 and ord(char) <= 57):
                state = 9
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(LexicError(row, col, char))
                pointer += 1
                col += 1
        
        elif state == 9:
            if(ord(char) >= 48 and ord(char) <= 57):
                pointer += 1
                col += 1
                lexeme += char
            else:
                if(ord(char) == 45):
                    state = 10
                    pointer += 1
                    col += 1
                    lexeme += char
                else:
                    errores.append(LexicError(row, col, char))
                    pointer += 1
                    col += 1
        
        elif state == 10:
            if(ord(char) >= 48 and ord(char) <= 57):
                state = 11
                pointer += 1
                col += 1
                lexeme += char
            else:
                errores.append(LexicError(row, col, char))
                pointer += 1
                col += 1
        
        elif state == 11:
            if(ord(char) >= 48 and ord(char) <= 57):
                pointer += 1
                col += 1
                lexeme += char
            else:
                if(ord(char) == 62):
                    state = 8
                    tmp_state = 11
                    pointer += 1
                    col += 1
                    lexeme += char
                else:
                    errores.append(LexicError(row, col, char))
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
                state = 0
                tokens.append(Token(Types.tk_num, lexeme, row, col))
                lexeme = ''

        #nombre de equipos
        elif state == 5:
            if(ord(char) >= 0 and ord(char) <= 255 and ord(char) != 34):
                pointer += 1
                col += 1
                lexeme += char
            else:
                if (ord(char) == 34):
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
                tokens.append(Token(Types.tk_year, lexeme, row, col))
                lexeme = ''
            elif tmp_state == 3:
                state = 0
                tmp_state = 0
                tokens.append(Token(Types.tk_num, lexeme, row, col))
                lexeme = ''
            elif tmp_state == 5:
                state = 0
                tmp_state = 0
                tokens.append(Token(Types.string, lexeme, row, col))
                lexeme = ''

    return tokens,errores

def scanner(tokens: List[Token]):
    list_parameters: List[Comand] = []
    tmp_comands: list = []
    comands: list = []
    tmp_comands.append(comands)
    tmp = ''
    for i in range(len(tokens)):
        if tokens[i].token == Types.no_one:
            new_cmds: list = []
            tmp_comands.append(new_cmds)
            continue
        tmp_comands[-1].append(tokens[i])
    try:
        for comands in tmp_comands:
            cmd = Comand()
            for i in range(len(tokens)):
                #comando Resultado
                if tokens[i].token == Types.res_result and tokens[i].lexeme == 'RESULTADO' and tokens[i+1].token == Types.string and tokens[i+2].token == Types.res_vs and tokens[i+2].lexeme == 'VS' and tokens[i+3].token == Types.string and tokens[i+4].token == Types.res_temp and tokens[i+4].lexeme == 'TEMPORADA' and tokens[i+5].token == Types.tk_year:
                    tmp = 'resultado'
                    cmd.team1 = tokens[i+1].lexeme.replace('"','')
                    cmd.team2 = tokens[i+3].lexeme.replace('"','')
                    cmd.season = tokens[i+5].lexeme.replace('<','').replace('>','')
                    break

                #comando Jornada
                elif tokens[i].token == Types.res_jorn and tokens[i].lexeme == 'JORNADA' and tokens[i+1].token == Types.tk_num and tokens[i+2].token == Types.res_temp and tokens[i+2].lexeme == 'TEMPORADA' and tokens[i+3].token == Types.tk_year:
                    tmp = 'jornada'
                    cmd.num1 = tokens[i+1].lexeme
                    cmd.season = tokens[i+3].lexeme.replace('<','').replace('>','')
                    
                    if tokens[i+4].token == Types.tk_flag_F and tokens[i+4].lexeme == '-f' and tokens[i+5].token == Types.tk_ID:
                        cmd.id = tokens[i+5].lexeme
                    else:
                        pass
                    break

                #comando Goles local
                elif tokens[i].token == Types.res_goles and tokens[i].lexeme == 'GOLES' and tokens[i+1].token == Types.res_local and tokens[i+1].lexeme == 'LOCAL' and tokens[i+2].token == Types.string and tokens[i+3].token == Types.res_temp and tokens[i+4].token == Types.tk_year:
                    tmp = 'golesL'
                    cmd.team1 = tokens[i+2].lexeme.replace('"','')
                    cmd.season = tokens[i+4].lexeme.replace('<','').replace('>','')
                    break
                
                 #comando Goles
                elif tokens[i].token == Types.res_goles and tokens[i].lexeme == 'GOLES' and tokens[i+1].token == Types.res_visitante and tokens[i+1].lexeme == 'VISITANTE' and tokens[i+2].token == Types.string and tokens[i+3].token == Types.res_temp and tokens[i+4].token == Types.tk_year:
                    tmp = 'golesV'
                    cmd.team1 = tokens[i+2].lexeme.replace('"','')
                    cmd.season = tokens[i+4].lexeme.replace('<','').replace('>','')
                    
                    break

                 #comando Goles
                elif tokens[i].token == Types.res_goles and tokens[i].lexeme == 'GOLES' and tokens[i+1].token == Types.res_total and tokens[i+1].lexeme == 'TOTAL' and tokens[i+2].token == Types.string and tokens[i+3].token == Types.res_temp and tokens[i+4].token == Types.tk_year:
                    tmp = 'golesT'
                    cmd.team1 = tokens[i+2].lexeme.replace('"','')
                    cmd.season = tokens[i+4].lexeme.replace('<','').replace('>','')
                    
                    break

                #comando Tabla
                elif tokens[i].token == Types.res_tabla and tokens[i].lexeme == 'TABLA' and tokens[i+1].token == Types.res_temp and tokens[i+1].lexeme == 'TEMPORADA' and tokens[i+2].token == Types.tk_year:
                    tmp = 'tabla'
                    cmd.season = tokens[i+2].lexeme.replace('<','').replace('>','')
                    
                    if tokens[i+3].token == Types.tk_flag_F and tokens[i+3].lexeme == '-f' and tokens[i+4].token == Types.tk_ID:
                        cmd.id = tokens[i+4].lexeme
                    else:
                        pass
                    break
            
                #comando Partidos
                elif tokens[i].token == Types.res_partidos and tokens[i].lexeme == 'PARTIDOS' and tokens[i+1].token == Types.string and tokens[i+2].token == Types.res_temp and tokens[i+2].lexeme == 'TEMPORADA' and tokens[i+3].token == Types.tk_year:
                    tmp = 'partidos'
                    cmd.team1 = tokens[i+1].lexeme.replace('"','')
                    cmd.season = tokens[i+3].lexeme.replace('<','').replace('>','')

                    if tokens[i+4].token == Types.tk_flag_F and tokens[i+4].lexeme == '-f'and tokens[i+5].token == Types.tk_ID: 
                        cmd.id = tokens[i+5].lexeme
                        if tokens[i+6].token == Types.tk_flag_JI and tokens[i+6].lexeme == '-ji' and tokens[i+7].token == Types.tk_num: 
                            cmd.num1 = tokens[i+7].lexeme
                            if tokens[i+8].token == Types.tk_flag_JF and tokens[i+8].lexeme == '-jf' and tokens[i+9].token == Types.tk_num:
                                cmd.num2 = tokens[i+9].lexeme
                            else:
                                pass
                        elif tokens[i+6].token == Types.tk_flag_JF and tokens[i+6].lexeme == '-jf' and tokens[i+7].token == Types.tk_num: 
                            cmd.num1 = tokens[i+7].lexeme
                            if tokens[i+8].token == Types.tk_flag_JI and tokens[i+8].lexeme == '-ji' and tokens[i+9].token == Types.tk_num:
                                cmd.num2 = tokens[i+9].lexeme
                            else:
                                pass               
                        else: 
                            pass  
       
                    elif tokens[i+4].token == Types.tk_flag_JI and tokens[i+4].lexeme == '-ji' and tokens[i+5].token == Types.tk_num:
                        cmd.num1 = tokens[i+5].lexeme
                        
                        if tokens[i+6].token == Types.tk_flag_F and tokens[i+6].lexeme == '-f' and tokens[i+7].token == Types.tk_ID:
                            cmd.id = tokens[i+7].lexeme
                            
                            if tokens[i+8].token == Types.tk_flag_JF and tokens[i+8].lexeme == '-jf' and tokens[i+9].token == Types.tk_num:
                                cmd.num2 = tokens[i+9].lexem
                            else:
                                pass    
                        elif tokens[i+6].token == Types.tk_flag_JF and tokens[i+6].lexeme == '-jf' and tokens[i+7].token == Types.tk_num:
                            cmd.num2 = tokens[i+7].lexeme
                            if tokens[i+8].token == Types.tk_flag_F and tokens[i+8].lexeme == '-f' and tokens[i+9].token == Types.tk_ID:
                                cmd.id = tokens[i+9].lexeme
                            else:
                                pass
                        else:
                            pass
                                        
                    elif tokens[i+4].token == Types.tk_flag_JF and tokens[i+4].lexeme == '-jf' and tokens[i+5].token == Types.tk_num:
                        cmd.num1 = tokens[i+5].lexeme
                        
                        if tokens[i+6].token == Types.tk_flag_F and tokens[i+6].lexeme == '-f' and tokens[i+7].token == Types.tk_ID:
                            cmd.id = tokens[i+7].lexeme
                                
                            if tokens[i+8].token == Types.tk_flag_JI and tokens[i+8].lexeme == '-ji' and tokens[i+9].token == Types.tk_num:
                                cmd.num2 = tokens[i+9].lexeme
                            else:
                                pass    
                        elif tokens[i+6].token == Types.tk_flag_JI and tokens[i+6].lexeme == '-ji' and tokens[i+7].token == Types.tk_num:
                            cmd.num2 = tokens[i+7].lexeme
                            
                            if tokens[i+8].token == Types.tk_flag_F and tokens[i+8].lexeme == '-f' and tokens[i+9].token == Types.tk_ID:
                                cmd.id = tokens[i+9].lexeme
                            else:
                                pass
                    else: 
                        pass

                    break

                #comando Top superior
                elif tokens[i].token == Types.res_top and tokens[i].lexeme == 'TOP' and (tokens[i+1].token == Types.res_sup and tokens[i+1].lexeme == 'SUPERIOR') and tokens[i+2].token == Types.res_temp and tokens[i+2].lexeme == 'TEMPORADA' and tokens[i+3].token == Types.tk_year:
                    tmp = 'topS'
                    cmd.season = tokens[i+3].lexeme.replace('<','').replace('>','')
                    if tokens[i+4].token == Types.tk_flag_N and tokens[i+4].lexeme == '-n' and tokens[i+5].token == Types.tk_num:
                        cmd.num1 = tokens[i+5].lexeme
                    else:
                        pass
                    break

                #comando Top inferior
                elif tokens[i].token == Types.res_top and tokens[i].lexeme == 'TOP' and (tokens[i+1].token == Types.res_inf and tokens[i+1].lexeme == 'INFERIOR') and tokens[i+2].token == Types.res_temp and tokens[i+2].lexeme == 'TEMPORADA' and tokens[i+3].token == Types.tk_year:
                    tmp = 'topI'
                    cmd.season = tokens[i+3].lexeme.replace('<','').replace('>','')
                    if tokens[i+4].token == Types.tk_flag_N and tokens[i+4].lexeme == '-n' and tokens[i+5].token == Types.tk_num:
                        cmd.num1 = tokens[i+5].lexeme
                    else:
                        pass
                    break
                

                #comando Adios
                elif tokens[i].token == Types.res_adios and tokens[i].lexeme == 'ADIOS':
                    tmp = 'adios'
                    break
                    
                else:
                    pass

            list_parameters.append(cmd)
        return list_parameters, str(tmp)
    except:
        comands = 'null'

def process_tokens(tokens):

    def extract_names(tokens: List[Types]):
        return list(map(lambda t: t.name, tokens))  

    env = Environment(loader=FileSystemLoader('Templates/'),
                    autoescape=select_autoescape(['html']))
    template = env.get_template('report_tokens.html')

    html_file = open('oficial_report_tokens.html', 'w+', encoding='utf-8')
    html_file.write(template.render(tokens=tokens, extract_names = extract_names))
    html_file.close()
    startfile('oficial_report_tokens.html')

def process_errors(errs,syntaxs):
    def extract_names(tokens: List[Types]):
        return list(map(lambda t: t.name, tokens))

    env = Environment(loader=FileSystemLoader('Templates/'),
                    autoescape=select_autoescape(['html']))
    template = env.get_template('report_errors.html')

    html_file = open('oficial_report_errors.html', 'w+', encoding='utf-8')
    html_file.write(template.render(errs=errs, syntaxs = syntaxs, extract_names = extract_names))
    html_file.close()
    startfile('oficial_report_errors.html')

def process_journeys(journeys,nombre):
    
    env = Environment(loader=FileSystemLoader('Templates/'),
                    autoescape=select_autoescape(['html']))
    template = env.get_template('report_journeys.html')

    html_file = open('{}.html'.format(nombre), 'w+', encoding='utf-8')
    html_file.write(template.render(journeys=journeys))
    html_file.close()
    startfile('{}.html'.format(nombre))

def process_tables(tables,nombre):

    env = Environment(loader=FileSystemLoader('Templates/'),
                    autoescape=select_autoescape(['html']))
    template = env.get_template('report_tables.html')

    html_file = open('{}.html'.format(nombre), 'w+', encoding='utf-8')
    html_file.write(template.render(tables=tables))
    html_file.close()
    startfile('{}.html'.format(nombre))

def process_tops(tops,nombre):

    env = Environment(loader=FileSystemLoader('Templates/'),
                    autoescape=select_autoescape(['html']))
    template = env.get_template('report_tops.html')

    html_file = open('{}.html'.format(nombre), 'w+', encoding='utf-8')
    html_file.write(template.render(tops=tops))
    html_file.close()
    startfile('{}.html'.format(nombre))

def process_partidos(partidos,nombre):

    env = Environment(loader=FileSystemLoader('Templates/'),
                    autoescape=select_autoescape(['html']))
    template = env.get_template('report_partidos.html')

    html_file = open('{}.html'.format(nombre), 'w+', encoding='utf-8')
    html_file.write(template.render(partidos=partidos))
    html_file.close()
    startfile('{}.html'.format(nombre))

class display_gui():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.frame = Frame()

        self.lexeme = ''
        self.lexeme2 = ''
        self.lexeme3 = ''

        self.root.title('La Liga Bot')
        self.root.geometry('850x400')

        self.frame.config(width=850, height=400)
        self.frame.place(x=0, y=0)

        self.btn_RE = Button(self.frame, width = 17, text="Reporte de Errores", command = self.errors)
        self.btn_RE.place(x=713, y=30)

        self.btn_LLE = Button(self.frame, width = 17, text="Limpiar log de Errores", command=self.LOE_clear)
        self.btn_LLE.place(x=713, y=60)

        self.btn_RT = Button(self.frame, width = 17, text="Reporte de Tokens", command = self.tokens)
        self.btn_RT.place(x=713, y=90)

        self.btn_LLT = Button(self.frame, width = 17, text="Limpiar log de Tokens", command= self.LOT_clear)
        self.btn_LLT.place(x=713, y=120)

        self.btn_MU = Button(self.frame, width = 17, text="Manual de Usuario", command=self.manual_usuario)
        self.btn_MU.place(x=713, y=150)

        self.btn_MT = Button(self.frame, width = 17, text="Manual Tecnico", command=self.manual_tecnico)
        self.btn_MT.place(x=713, y=180)

        self.btn_Send = Button(self.frame, width = 17, text="Enviar", command = lambda: self.analizer(self.text_area.get()))
        self.btn_Send.place(x=713, y=348)

        self.chat_area = Text(self.frame,  height = 19, width = 84)
        self.chat_area.place(x=30, y=30)

        Bot = '{} \n'.format('Bienvenido a la Liga Bot, Ingrese un Comando')
        self.chat_area.insert(END,Bot,("BOT",))
        self.chat_area.tag_configure("BOT",justify="left")
        self.chat_area.configure(state="disable")

        self.text_area = Entry(self.frame)
        self.text_area.place(x=30, y=350, width=675 , height=25)

        self.root.resizable(0,0)
        self.root.mainloop()

    def analizer(self,text):
        global tokens
        global errors
        global syntaxErrs
        global error

        self.chat_area.configure(state="normal")
        user = '{} \n'.format(text)
        self.chat_area.insert(END,user,("USER",))
        self.chat_area.tag_configure("USER",justify="right")
        self.chat_area.configure(state="disable")

        self.lexeme += '{}'.format(text)
        self.lexeme2 += '{}'.format(self.lexeme)
        self.lexeme3 += '{}'.format(self.lexeme)

        tokens, errors = AFD(self.lexeme)

        syntaxErrs = Syntax(tokens)
        error = syntaxErrs.startup()

        self.lexeme = ''

        if len(tokens) != 0:
            for i in tokens:
                i.show_token()
        else:
            print(' > No hay tokens')

        if len(errors) != 0 or len(error) != 0:
            showerror('Error',
                     'Se han encontrado Errores')
            print('<>=<>=<>=<>=<>=<>=<>=<> ERRORES LEXICOS <>=<>=<>=<>=<>=<>=<>=<>=<>=<>')
            for j in errors:
                j.show_LexicErrors()
            print('<>=<>=<>=<>=<>=<>=<>=<> ERRORES SINTACTICOS <>=<>=<>=<>=<>=<>=<>=<>=<>')
            for K in error:
                K.show_sitaxErrors()
        else:
            print(' > No hay errores')
            
        if len(error) == 0:
            showinfo('OK',
                     'Comando Aceptado')

            answer = ''
            answer = AI_BOT()
            Bot = '{} \n'.format(answer)
            self.chat_area.configure(state="normal")
            self.chat_area.insert(END,answer,("BOT",))
            self.chat_area.tag_configure("BOT",justify="left")
            self.chat_area.configure(state="disable")

            if answer == 'ADIOS':
                showinfo('Exit',
                     'Saliendo de la aplicaicon')
                sys.exit()

    def tokens(self):
        global tokens_list

        tokens_list, errors_list = AFD(self.lexeme2)

        if len(tokens_list) != 0:
            showinfo('Info',
                     'Reporte de Tokens')
            process_tokens(tokens_list) 
        else:
            showinfo('Info',
                     'Nada que reportar')
    
    def LOT_clear(self):
        global tokens_list
        tokens_list = ()
        self.lexeme2 = ''
        showinfo('Info',
                     'Log de Tokens Limpio')
    
    def errors(self):
        global tokens_list
        global errors_list
        global syntaxE_list
        global error_general

        tokens_list, errors_list = AFD(self.lexeme3)
        syntaxE_list = Syntax(tokens_list)
        error_general = syntaxE_list.startup()

        if len(errors_list) != 0 or len(error_general) != 0:
            showinfo('Info',
                     'Reporte de Errores')
            process_errors(errors_list,error_general)
        else:
            showinfo('Info',
                     'Nada que reportar')

    def LOE_clear(self):
        global errors_list
        global syntaxE_list
        errors_list = ()
        syntaxE_list = ()
        self.lexeme3 = ''
        showinfo('Info',
                     'Log de Errores Limpio')

    def manual_usuario(self):
        showinfo('Info',
                     'Manual de Usuario')
        webbrowser.open_new('Docs\\Usuario.pdf')
    
    def manual_tecnico(self):
        showinfo('Info',
                     'Manual Tecnico')
        webbrowser.open_new('Docs\\Tecnico.pdf')

def Load_CSV(ruta):
    with open(ruta,"r",encoding='utf-8') as File:
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

def AI_BOT():
    global datas
    global tokens
    global tableses
    global journeyses
    global seasonses
    global seasonses2
    global partidoses

    answer = ''
    aux_n = 5

    local = []

    cmds, type = scanner(tokens)

    if cmds != None:
        if type == 'resultado':
            for i in cmds:
                for j in datas:
                    if i.team1 == j.team1 and i.team2 == j.team2 and i.season == j.season:
                        answer = 'El resultado de este partido fue: {}: {} - {}: {} \n'.format(j.team1,j.gol1,j.team2,j.gol2)

        elif type == 'jornada':
            for i in cmds:
                for j in datas:
                    if i.num1 == j.journey and i.season == j.season:
                        journeyses.append(journeys(j.journey,j.team1,j.gol1,j.team2,j.gol2))
                        answer = 'Generando archivo de reaultados jornada: {} temporada {} \n'.format(i.num1,i.season)
                        if i.id == '':
                            i.id ='jornada'
            process_journeys(journeyses,i.id)

        elif type == 'golesL':
            aux1 = 0
            for i in cmds:
                for j in datas:
                    if i.team1 == j.team1 and i.season == j.season:
                        aux1 += int(j.gol1)
                        answer = 'Los goles anotados por: {}, como LOCAL en la temporada {} fueron {} \n'.format(j.team1,j.season,aux1)

        elif type == 'golesV':
            aux1 = 0
            for i in cmds:
                for j in datas:
                    if i.team1 == j.team2 and i.season == j.season:
                        aux1 += int(j.gol2)
                        answer = 'Los goles anotados por: {}, como VISITANTE en la temporada {} fueron {} \n'.format(j.team1,j.season,aux1)

        elif type == 'golesT':
            aux1 = 0
            aux2 = 0
            total = 0
            for i in cmds:
                for j in datas:
                    if i.team1 == j.team1 and i.season == j.season:
                        aux1 += int(j.gol1)
                    if i.team1 == j.team2 and i.season == j.season:
                        aux2 += int(j.gol2)
                    total = aux1+aux2
                    answer = 'Los goles anotados por: {}, en TOTAL en la temporada {} fueron {} \n'.format(j.team1,j.season,total)

        elif type == 'tabla':
            for i in cmds:
                for j in datas:
                    if i.season == j.season:
                        tableses.append(tables(j.journey,j.team1,j.gol1,j.team2,j.gol2))
                        lista = clasifications()
                        answer = 'Generando Archivo de clasificacion de temporada {} \n'.format(j.season)
                        if i.id == '':
                            i.id ='temporada'
            process_tables(lista,i.id)

        elif type == 'partidos':
            local = []
            aux1 = 0
            aux2 = 0

            for i in cmds:
                for j in datas:
                    if i.team1 == j.team1 or i.team1 == j.team2 and i.season == j.season:
                        if i.num1 == 0:
                            pass
                        else:
                            aux1 = int(i.num1)
                        
                        if i.num2 == 0:
                            pass
                        else:
                            aux2 = int(i.num2)

                        if i.id == '':
                            i.id ='partidos'    

                        partidoses.append(partidos(j.journey,j.team1,j.gol1,j.team2,j.gol2))
                        answer = 'Generando archivo de resultados de temporada: {} del {} \n'.format(j.season,j.team1)                        

            try:
                if aux1 != 0 and aux2 != 0:
                    for k in range(aux1,aux2):
                        local.append(partidoses[k])

                elif aux1 == 0 and aux2 != 0:
                    for l in range(0,aux2):
                        local.append(partidoses[l])

                elif aux1 != 0 and aux2 == 0:
                    for m in range(aux1,len(partidoses)):
                        local.append(partidoses[m])
                
                else:
                    for n in range(len(partidoses)):
                        local.append(partidoses[n])

            except:
                print()
             
            process_partidos(local,i.id)


        elif type == 'topS':
            for i in cmds:
                for j in datas:
                    if i.season == j.season:
                        if i.num1 == 0:
                            aux_n = 5
                        else:
                            aux_n = int(i.num1)

                        i.id ='topSuperior'
    
                        answer = 'El top superior de la temporada {} \n'.format(j.season)
                        
                        seasonses.append(tables2(j.journey,j.team1,j.gol1,j.team2,j.gol2,i.id))
                        lista = clasifications2() 

            try:
                for k in range(0,aux_n):
                    local.append(lista[k])
            except:
                print()
                            
            process_tops(local,i.id)
                                 
                        
        elif type == 'topI':
            for i in cmds:
                for j in datas:
                    if i.season == j.season:
                        if i.num1 == 0:
                            aux_n = 5
                        else:
                            aux_n = int(i.num1)

                        i.id ='topInferior'
    
                        answer = 'El top Inferior de la temporada {} \n'.format(j.season)
                        
                        seasonses2.append(tables2(j.journey,j.team1,j.gol1,j.team2,j.gol2,i.id))
                        lista = clasifications3() 

            try:
                for k in range(0,aux_n):
                    local.append(lista[k])
            except:
                print()
                            
            process_tops(local,i.id)

        elif type == 'adios':
            goodbye = 'ADIOS'
            answer = '{}'.format(goodbye)


        return answer

    else:
        print(' > No hay parametros para comandos')

if __name__ == '__main__':
    Load_CSV('Files\LaLigaBot-LFP.csv')
    display_gui()
