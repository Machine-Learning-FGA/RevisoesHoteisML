#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import random

# obter resultado real
def get_evaluation():
	return random.randint(1, 5)


x_label = 100
x_input = 220

labels = ['Cidade:', 'Total de Revisões', 'Revisões de Hotel:', 'Votos de Hotel:', 'Período:',]
cities = ['Gama','Santa Maria','Ocidental', 'Valparadise', '...']

app = Tk()
app.title("Wall-e Society - Revisões de Hotéis")
app.geometry("500x500")

# descrição app
city_label = Label(app, text='---- Revisões de Hotéis ----')
city_label.place(x=180,y=50)

## label: cidade
city_label = Label(app, text=labels[0])
city_label.place(x=x_label,y=100)

# entrada: cidade
combo_city = ttk.Combobox(app)
combo_city.place(x=x_input,y=100)
combo_city['values'] = cities
combo_city.current(0)

## ------

# seleção de cidade
# def getCity():
#     combo_city.get()
#     test.set("Cidade: "+combo_city.get())

# testar seleção do combobox
# test = StringVar()
# test.set("Cidade: ")
# test_label = Label(app, textvariable=test)
# test_label.place(x=80,y=170)

# ------

## label: total de revisões
revision_label = Label(app,text=labels[1])
revision_label.place(x=x_label,y=130)

# entrada: total de revisões
revision = IntVar()
revision.set(50)

revision_entry = Entry(app, textvariable=revision)
revision_entry.place(x=x_input,y=130)

## ------

## label: revisões de hotel
hotel_revision_label = Label(app,text=labels[2])
hotel_revision_label.place(x=x_label,y=160)

# entrada: revisões de hotel
hotel_revision = IntVar()
hotel_revision.set(50)

hotel_revision_entry = Entry(app, textvariable=hotel_revision)
hotel_revision_entry.place(x=x_input,y=160)

## ------

## label: votos hotéis
hotel_votes_label = Label(app,text=labels[3])
hotel_votes_label.place(x=x_label,y=190)

# entrada: votos hotéis
hotel_votes = IntVar()
hotel_votes.set(50)

hotel_votes_entry = Entry(app, textvariable=hotel_votes)
hotel_votes_entry.place(x=x_input,y=190)

# ------

## label: periodo
period_label = Label(app,text=labels[4])
period_label.place(x=x_label,y=220)

# entrada: período
combo_period = ttk.Combobox(app)
combo_period.place(x=x_input,y=220)
combo_period['values'] = ('Dez-Fev','Mar-Mai','Jun-Ago', 'Set-Nov', 'Dez-Fev')
combo_period.current(0)

## ------

# botão de confirmar seleção (Mudar método para todos os parâmetros)
# confirm_button = Button(app,command=getCity,text='Confirmar')
confirm_button = Button(app,text='Calcular Nota')
confirm_button.place(x=200,y=280)

## label: resultado
result_predict_label = Label(app,text='Nota Provável:')
result_predict_label.place(x=210,y=390)

# campo: resultado
result_predict = Label(app, text=get_evaluation())
result_predict.config(font=("Courier", 30))
result_predict.place(x=235,y=410)

# -----

app.mainloop()