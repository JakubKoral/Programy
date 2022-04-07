from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from tkinter import *
import sys
import os

try: # próba pobrania z internetu
    
    url = urlopen('https://www.nbp.pl/kursy/KursyA.html')
    page = url.read()
    url.close()
    page_bs = bs(page, 'html.parser')
    data = page_bs.findAll("tr")[4:39] # pobranie wierszy tabeli z walutami
    names = ['złoty'] # nazwy walut, złoty dodany dodatkowo jako pierwszy
    codes = ['1 PLN'] # kod waluty, ważny, bo nie zawsze przelicznik 1:1
    currency_rates = [1.0] # kurs waluty

    for i in range(len(data)):
        names.append(data[i].text[1:-1].split("\n")[0])
        codes.append(data[i].text[1:-1].split("\n")[1])
        currency_rates.append(float(data[i].text[1:-1].split("\n")[2].replace(",",".")))
        # zmiana polskich przecinków na floatowe kropki

    with open("table.txt", "w") as t: # zapisanie danych do pliku
        for i in range(len(data)):
            t.write(data[i].text[1:-1].split("\n")[0])
            t.write("\n") # rozdzielanie danych nową linią
            t.write(data[i].text[1:-1].split("\n")[1])
            t.write("\n") # rozdzielanie danych nową linią
            t.write(data[i].text[1:-1].split("\n")[2].replace(",","."))
            t.write("\n===\n") # separator danych walut
        
except: # próba pobrania z pliku
    
    if os.path.exists("table.txt"): # warunek istnienia pliku
        names = ['złoty'] # nazwy walut, złoty dodany dodatkowo jako pierwszy
        codes = ['1 PLN'] # kod waluty, ważny, bo nie zawsze przelicznik 1:1
        currency_rates = [1.0] # kurs waluty
        
        with open("table.txt","r") as t:
            table = t.read() # przeczytanie tabeli z pliku

        for i in range(len(table.split("\n===\n"))-1): # rozdzielenie walut
            names.append(table.split("\n===\n")[i].split("\n")[0])
            codes.append(table.split("\n===\n")[i].split("\n")[1])
            currency_rates.append(float(table.split("\n===\n")[i].split("\n")[2]))

    else:
        print("ERROR: Brak połączenia z internetem i brak pliku!")
        sys.exit()

def Konwertuj():
    """
    Funkcja Konwertuj() dodaje funkcjonalność przyciskowi "Konwertuj".
    Przlicza wybraną kwotę waluty currency_1 na docelową walutę currency_2. 
    Jeżeli użytkownik nie poda żadnej kwoty lub to co poda nie będzie liczbą,
    zostanie wydrukowany komunikat "ERROR: Podaj liczbę!".
    """
    try:
        result.delete(0,END) # czyszczenie okienka z wynikiem
        amount = eval(entry.get()) # pobranie kwoty w walucie źródłowej
        currency_1 = variable.get() # pobranie waluty źródłowej
        currency_2 = variable2.get() # pobranie waluty docelowej
        currency_1_rate=currency_rates[names.index(currency_1)] # pobranie kursu waluty źródłowej
        currency_2_rate=currency_rates[names.index(currency_2)] # pobranie kursu waluty docelowej
        currency_multiplier_1 = eval(codes[names.index(currency_1)][:-4]) # pobranie przelicznika waluty źródłowej
        currency_multiplier_2 = eval(codes[names.index(currency_2)][:-4]) # pobranie przelicznika waluty docelowej
        result.insert(0,str(round(amount*((currency_1_rate*currency_multiplier_2)/(currency_2_rate*currency_multiplier_1)),4))) # wypisanie wyniku
    except:
        result.insert(0,"Podaj kwotę i walutę!")

def Zamknij():
    """
    Funkcja Zamknij() dodaje funkcjonalność przyciskowi "Zamknij".
    Zamyka okienko aplikacja i wyświetla komunikat "Do zobaczenia".
    """
    master.destroy()
    print("Do zobaczenia!")

master = Tk() # stworzenie okienka
master.title("Kursy walut™") # tytuł programu

variable = StringVar(master) # lista rozwiajana walut źródłowych
variable2 = StringVar(master) # lista rozwijana walut docelowych

#etykiety
head_label = Label(master, text="Konwertuj waluty: ").grid(row=0,column=2)
from_label = Label(master, text="Z: ").grid(row=1,column=1)
to_label = Label(master, text="Na: ").grid(row=1,column=3)
amount_label = Label(master, text="Ilość: ").grid(row=3,column=1)
result_label = Label(master, text="Wynik: ").grid(row=3,column=3)

#listy rozwijane walut
currency_list_1 = OptionMenu(master, variable, *names)
currency_list_1.grid(row=2,column=1) # ustawienie na siatce
currency_list_2 = OptionMenu(master, variable2, *names)
currency_list_2.grid(row=2,column=3) # ustawienie na siatce

#przyciski
calculate_button = Button(master,text ="Konwertuj", command = Konwertuj).grid(row=2,column=2)
close_button = Button(master,text ="Zamknij", command = Zamknij).grid(row=5,column=2)

#pole do wpisania kwoty w walucie źródłowej i pole do wyświetlenia wyniku
entry = Entry(master)
entry.grid(row=4,column=1) # ustawienie na siatce
result = Entry(master)
result.grid(row=4,column=3) # ustawienie na siatce

mainloop()
