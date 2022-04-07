# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:03:27 2020

@author: Jakub Koral
"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import *
from tkinter import *

master = Tk() # stworzenie okienka
master.title("Rysownik funkcji™") # tytuł programu
var = IntVar() # stworzenie zmiennej do checkboxu

def Zamknij():
    """
    Funkcja Zamknij() dodaje funkcjonalność przyciskowi "Zamknij".
    Zamyka okienko aplikacja i wyświetla komunikat "Do zobaczenia".
    """
    master.destroy()
    print("Do zobaczenia!")

def Rysuj():
    """
    Funkcja Rysuj()dodaje funkcjonalność przyciskowi "Rysuj".
    Rysuje wykresy na płótnie w okienku.
    """
    try:
        figure.clear() # wyczyszczenie płótna
        ax = figure.add_subplot() # dodanie podwykresu
        ax.set_xlim([eval(xlim_entry.get().split(";")[0]), eval(xlim_entry.get().split(";")[1])]) # ustawienie zakresu x 
        ax.set_ylim([eval(ylim_entry.get().split(";")[0]), eval(ylim_entry.get().split(";")[1])]) # ustawienie zakresu y 
        ax.set_title(title_entry.get()) # ustawienie tytułu wykresu
        ax.set_xlabel(xaxis_entry.get()) # ustawienie etykiety OX
        ax.set_ylabel(yaxis_entry.get()) # ustawienie etykiety OY
        x = linspace(eval(xlim_entry.get().split(";")[0]), eval(xlim_entry.get().split(";")[1]),1000) # stworzenie tablicy x-ów
        
        for i in range(len(entry.get().split(";"))): # pętla przez wzory funkcji
            y = eval(entry.get().split(";")[i]) # obliczenie wartości funkcji, dzięki numpy
            ax.plot(x,y) # dodanie wykresu funkcji
            
        if var.get() == 1: # gdy checkbox zaznaczony
            ax.legend(entry.get().split(";")) # dodanie legendy z wzorami
            
        wykres.draw() # narysowanie wykresu w okienku
        
    except:
        
        if entry.get() == "": # komunikat, gdy nie podano wzoru funkcji
            entry.insert(0,"Wpisz wzór funkcji!")
        
        if xlim_entry.get() == "": # komunikat, gdy nie podano zakresu x
            xlim_entry.insert(0,"Podaj zakres OX!")

        elif ";" not in xlim_entry.get(): # komunikat, gdy nie użyto ";" jako separatora
            xlim_entry.delete(0,END)
            xlim_entry.insert(0,"Zły separator zakresu!")

        if ylim_entry.get() == "": # komunikat, gdy nie podano zakresu y 
            ylim_entry.insert(0,"Podaj zakres OY!")

        elif ";" not in ylim_entry.get(): # komunikat, gdy nie użyto ";" jako separatora
            ylim_entry.delete(0,END)
            ylim_entry.insert(0,"Zły separator zakresu!")

        if title_entry.get() == "": # komunikat, gdy nie podano tytułu wykresu
            title_entry.insert(0,"Wpisz tytuł wykresu!")

        if xaxis_entry.get() == "": # komunikat, gdy nie podano etykiety OX
            xaxis_entry.insert(0,"Dodaj etykietę osi OX!")

        if yaxis_entry.get() == "": # komunikat, gdy nie podano etykiety OY
            yaxis_entry.insert(0,"Dodaj etykietę osi OY!")

#funkcje przycisków do budowania wzoru funkcji

def plus():
    """
    Funkcja plus() dodaje funkcjonalność przyciskowi "+".
    Wpisuje symbol dodawania "+" w polu do wpisywania wzoru
    w okienku.
    """
    entry.insert(END,"+")

def minus():
    """
    Funkcja minus() dodaje funkcjonalność przyciskowi "-".
    Wpisuje symbol odejmowania "-" w polu do wpisywania wzoru
    w okienku.
    """
    entry.insert(END,"-")

def multiply():
    """
    Funkcja multiply() dodaje funkcjonalność przyciskowi "*".
    Wpisuje symbol mnożenia "*" w polu do wpisywania wzoru
    w okienku.
    """
    entry.insert(END,"*")

def divide():
    """
    Funkcja divide() dodaje funkcjonalność przyciskowi "/".
    Wpisuje symbol dzielenia "/" w polu do wpisywania wzoru
    w okienku.
    """
    entry.insert(END,"/")

def left_bracket():
    """
    Funkcja left_bracket() dodaje funkcjonalność przyciskowi "(".
    Wpisuje symbol lewego nawiasu "(" w polu do wpisywania wzoru
    w okienku.
    """
    entry.insert(END,"(")

def right_bracket():
    """
    Funkcja right_bracket() dodaje funkcjonalność przyciskowi "/".
    Wpisuje symbol prawego nawiasu "(" w polu do wpisywania wzoru
    w okienku.
    """
    entry.insert(END,")")

def square():
    """
    Funkcja square() dodaje funkcjonalność przyciskowi "x^2".
    Wpisuje symbol podnoszenia x do kwadratu "x**2" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"x**2")

def cube():
    """
    Funkcja cube() dodaje funkcjonalność przyciskowi "x^3".
    Wpisuje symbol podnoszenia x do sześcianu "x**3" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"x**3")

def power():
    """
    Funkcja power() dodaje funkcjonalność przyciskowi "x^y".
    Wpisuje symbol podnoszenia x do wybranej potęgi "x**" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"x**")

def square_root():
    """
    Funkcja square_root() dodaje funkcjonalność przyciskowi "x^(1/2)".
    Wpisuje symbol pierwiastka kwadratowego "x**(1/2)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"x**(1/2)")

def cube_root():
    """
    Funkcja cube_root() dodaje funkcjonalność przyciskowi "x^(1/2)".
    Wpisuje symbol pierwiastka sześciennego "x**(1/3)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"x**(1/3)")

def root():
    """
    Funkcja root() dodaje funkcjonalność przyciskowi "x^(1/y)".
    Wpisuje symbol pierwiastka wybranego stopnia "x**(1/)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"x**(1/)")

def two_to_x():
    """
    Funkcja two_to_x() dodaje funkcjonalność przyciskowi "2^x".
    Wpisuje symbol podnoszenia 2 do potęgi x "2**x" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"2**x")
    
def ten_to_x():
    """
    Funkcja ten_to_x() dodaje funkcjonalność przyciskowi "10^x".
    Wpisuje symbol podnoszenia 10 do potęgi x "10**x" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"10**x")

def exponential():
    """
    Funkcja exponential() dodaje funkcjonalność przyciskowi "e^x".
    Wpisuje symbol podnoszenia liczby e do potęgi x "exp(x)"
    w polu do wpisywania wzoru w okienku.
    """
    entry.insert(END,"exp(x)")

def natural_logarithm():
    """
    Funkcja natural_logarithm() dodaje funkcjonalność przyciskowi "ln(x)".
    Wpisuje symbol logarytmu naturalnego z x "log(x)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"log(x)")

def logarithm_10():
    """
    Funkcja logarithm_10() dodaje funkcjonalność przyciskowi "log_10(x)".
    Wpisuje symbol logarytmu o podstawie 10 z x "log10(x)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"log10(x)")

def sinus():
    """
    Funkcja sinus() dodaje funkcjonalność przyciskowi "sin(x)".
    Wpisuje symbol funkcji sinus z x "sin(x)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"sin(x)")

def cosinus():
    """
    Funkcja cosinus() dodaje funkcjonalność przyciskowi "cos(x)".
    Wpisuje symbol funkcji cosinus z x "cos(x)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"cos(x)")

def tangens():
    """
    Funkcja tangens() dodaje funkcjonalność przyciskowi "tg(x)".
    Wpisuje symbol funkcji tangensa z x "tan(x)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"tan(x)")

def cotangens():
    """
    Funkcja cotangens() dodaje funkcjonalność przyciskowi "ctg(x)".
    Wpisuje symbol funkcji cotangens z x "1/tan(x)" w polu
    do wpisywania wzoru w okienku. Z powodu braku tej funkcji
    w bibliotece numpy obliczana jest z tożsmaości trygonometrycznej.
    """
    entry.insert(END,"1/tan(x)")

def arcsinus():
    """
    Funkcja arcsinus() dodaje funkcjonalność przyciskowi "arcsin(x)".
    Wpisuje symbol funkcji arcus sinus z x "arcsin(x)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"arcsin(x)")

def arccosinus():
    """
    Funkcja arccosinus() dodaje funkcjonalność przyciskowi "arccos(x)".
    Wpisuje symbol funkcji arcus cosinus z x "arccosin(x)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"arccos(x)")

def arctangens():
    """
    Funkcja arctangens() dodaje funkcjonalność przyciskowi "arctg(x)".
    Wpisuje symbol funkcji arcus tangens z x "arctan(x)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"arctan(x)")
    
def arccotangens():
    """
    Funkcja arccotangens() dodaje funkcjonalność przyciskowi "arcctg(x)".
    Wpisuje symbol funkcji arcus cotangens z x pi/2-arctan(x)" w polu
    do wpisywania wzoru w okienku. Z powodu braku tej funkcji
    w bibliotece numpy obliczana jest z tożsmaości trygonometrycznej.
    """
    entry.insert(END,"pi/2-arctan(x)")

def absolute_value():
    """
    Funkcja absolute_value() dodaje funkcjonalność przyciskowi "|x|".
    Wpisuje symbol wartości bezwzględnej z x "abs(x)" w polu
    do wpisywania wzoru w okienku.
    """
    entry.insert(END,"abs(x)")

def number_pi():
    """
    Funkcja number_pi() dodaje funkcjonalność przyciskowi "pi".
    Wpisuje symbol liczby pi "pi" w polu do wpisywania wzoru w okienku.
    """
    entry.insert(END,"pi")

#wykres
figure = plt.Figure(figsize=(4,4)) # stworzenie płótna 4x4
wykres = FigureCanvasTkAgg(figure,master) # dodanie płótna do okienka
wykres.get_tk_widget().grid(row=0,column=0) # pozycjonowanie płótna w okienku

#parametry wykresu
entry_label = Label(master, text = "Wzór funkcji: ").grid(row=1,column=0)
entry = Entry(master)
entry.grid(row=2,column=0)
xlim_label = Label(master, text = "Zakres x: ").grid(row=3,column=0)
xlim_entry = Entry(master)
xlim_entry.grid(row=4,column=0)
ylim_label = Label(master, text = "Zakres y: ").grid(row=5,column=0)
ylim_entry = Entry(master)
ylim_entry.grid(row=6,column=0)
title_label = Label(master, text = "Tytuł: ").grid(row=7,column=0)
title_entry = Entry(master)
title_entry.grid(row=8,column=0)
xaxis_label = Label(master, text = "Etykieta osi x: ").grid(row=9,column=0)
xaxis_entry = Entry(master)
xaxis_entry.grid(row=10,column=0)
yaxis_label = Label(master, text = "Etykieta osi y: ").grid(row=11,column=0)
yaxis_entry = Entry(master)
yaxis_entry.grid(row=12,column=0)
legend = Checkbutton(master, text = "Legenda", variable = var,onvalue=1, offvalue=0).grid(row=13,column=0)

#przyciski rysuj i zamknij
draw_button = Button(master, text = "Rysuj", command = Rysuj).grid(row=14,column=0)
close_button = Button(master,text = "Zamknij", command = Zamknij).grid(row=11,column=3)

#operatory arytmetyczne
aritmetic_operators_label = Label(master, text="Operatory arytmetyczne").grid(row=1,column=1)
plus_button = Button(master, text="+", command = plus).grid(row=1,column=2, sticky=N+S+E+W)
minus_button = Button(master, text="-", command = minus).grid(row=1,column=3, sticky=N+S+E+W)
multiply_button = Button(master, text="*", command = multiply).grid(row=1,column=4, sticky=N+S+E+W)
divide_button = Button(master, text="/", command = divide).grid(row=1,column=5, sticky=N+S+E+W)

#nawiasy
bracket_label = Label(master, text="Nawiasy").grid(row=2,column=1)
left_bracket_button = Button(master, text="(", command = left_bracket).grid(row=2,column=2, sticky=N+S+E+W)
right_bracket_button = Button(master, text=")", command = right_bracket).grid(row=2,column=3, sticky=N+S+E+W)

#funkcje kwadrat, sześcian, potęgowanie
square_cube_power_label = Label(master, text="Kwadrat, sześcian i do potęgi").grid(row=3,column=1)
square_button = Button(master, text="x^2", command = square).grid(row=3,column=2, sticky=N+S+E+W)
cube_button = Button(master, text="x^3", command = cube).grid(row=3,column=3, sticky=N+S+E+W)
power_button = Button(master, text="x^y", command = power).grid(row=3,column=4, sticky=N+S+E+W)

#pierwiastki
roots_label = Label(master, text="Pierwiastki").grid(row=4,column=1)
square_root_button = Button(master, text="x^(1/2)", command = square_root).grid(row=4,column=2, sticky=N+S+E+W)
cube_root_button = Button(master, text="x^(1/3)", command = cube_root).grid(row=4,column=3, sticky=N+S+E+W)
root_button = Button(master, text="x^(1/y)", command = root).grid(row=4,column=4, sticky=N+S+E+W)

#funkcje potęgowe
to_power_label = Label(master, text="Funkcje potęgowe").grid(row=5,column=1)
two_to_power_button = Button(master, text="2**x", command = two_to_x).grid(row=5,column=2, sticky=N+S+E+W)
ten_to_power_button = Button(master, text="10**x", command = ten_to_x).grid(row=5,column=3, sticky=N+S+E+W)
exp_button = Button(master, text="e^x", command = exponential).grid(row=5,column=4, sticky=N+S+E+W)

#logarytmy
logarithms_label = Label(master, text="Funkcje logarytmiczne").grid(row=6,column=1)
ln_button = Button(master, text="ln(x)", command = natural_logarithm).grid(row=6,column=2, sticky=N+S+E+W)
log10_button = Button(master, text="log_10(x)", command = logarithm_10).grid(row=6,column=3, sticky=N+S+E+W)

#funkcje trygonometryczne
trigonometric_label = Label(master, text="Funkcje trygonometryczne").grid(row=7,column=1)
sin_button = Button(master, text="sin(x)", command = sinus).grid(row=7,column=2, sticky=N+S+E+W)
cos_button = Button(master, text="cos(x)", command = cosinus).grid(row=7,column=3, sticky=N+S+E+W)
tan_button = Button(master, text="tan(x)", command = tangens).grid(row=7,column=4, sticky=N+S+E+W)
cot_button = Button(master, text="cot(x)", command = cotangens).grid(row=7,column=5, sticky=N+S+E+W)

#funkcje cyklometryczne
arcus_label = Label(master, text="Funkcje cyklometryczne").grid(row=8,column=1)
arcsin_button = Button(master, text="arcsin(x)", command = arcsinus).grid(row=8,column=2, sticky=N+S+E+W)
arccos_button = Button(master, text="arccos(x)", command = arccosinus).grid(row=8,column=3, sticky=N+S+E+W)
arctan_button = Button(master, text="arctan(x)", command = arctangens).grid(row=8,column=4, sticky=N+S+E+W)
arccot_button = Button(master, text="arccot(x)", command = arccotangens).grid(row=8,column=5, sticky=N+S+E+W)

#inne
others_label = Label(master, text="Inne").grid(row=9,column=1)
abs_button = Button(master, text="|x|", command = absolute_value).grid(row=9,column=2, sticky=N+S+E+W)
pi_button = Button(master, text="pi", command = number_pi).grid(row=9,column=3, sticky=N+S+E+W)


