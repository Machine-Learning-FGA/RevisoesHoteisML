#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import random

# obter resultado real
def get_evaluation():
	return random.randint(1, 5)


x_label = 100
x_input = 220
x_label_side = 380
x_input_side = 510

labels = [
			'Cidade:', 'Total de Revisões', 'Revisões de Hotel:', 
			'Votos de Hotel:', 'Período:', 'Tipo:', 'Animadores:',
			'Academia:', 'Quadra de Tenis:', 'Spa:', 'Piscina:',
			'Wi-fi:', 'Estrelas:','Quartos:','Anos como Membro:',
			'Mês revisão','Dia da Revisão:'
		 ]
cities = ['Gama','Santa Maria','Ocidental', 'Valparadise', '...']

app = Tk()
app.title("Wall-e Society - Revisões de Hotéis")
app.geometry("770x500")

title_label = Label(app,text='--- Configuração do modelo ---')
title_label.place(x=300,y=50)

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
revision_label.place(x=x_label,y=100)

# entrada: total de revisões
revision = IntVar()
revision.set(50)

revision_entry = Entry(app, textvariable=revision)
revision_entry.place(x=x_input,y=100)

## ------

## label: revisões de hotel
hotel_revision_label = Label(app,text=labels[2])
hotel_revision_label.place(x=x_label,y=130)

# entrada: revisões de hotel
hotel_revision = IntVar()
hotel_revision.set(50)

hotel_revision_entry = Entry(app, textvariable=hotel_revision)
hotel_revision_entry.place(x=x_input,y=130)

## ------

## label: votos hotéis
hotel_votes_label = Label(app,text=labels[3])
hotel_votes_label.place(x=x_label,y=160)

# entrada: votos hotéis
hotel_votes = IntVar()
hotel_votes.set(50)

hotel_votes_entry = Entry(app, textvariable=hotel_votes)
hotel_votes_entry.place(x=x_input,y=160)

# ------

## label: periodo
period_label = Label(app,text=labels[4])
period_label.place(x=x_label,y=190)

# entrada: período
combo_period = ttk.Combobox(app)
combo_period.place(x=x_input,y=190)
combo_period['values'] = ('Dez-Fev','Mar-Mai','Jun-Ago', 'Set-Nov', 'Dez-Fev')
combo_period.current(0)

# -----

## label: Tipo
type_label = Label(app,text=labels[5])
type_label.place(x=x_label,y=220)

# entrada: Tipo
type = IntVar()
type.set(50)

type_entry = Entry(app, textvariable=type)
type_entry.place(x=x_input,y=220)

# -----

## label: Animadores
animators_label = Label(app,text=labels[6])
animators_label.place(x=x_label,y=250)

# entrada:Animadores
animators = IntVar()
animators.set(50)

animators_entry = Entry(app, textvariable=animators)
animators_entry.place(x=x_input,y=250)

# -----

## label: Academia
gym_label = Label(app,text=labels[7])
gym_label.place(x=x_label,y=280)

# entrada: Academia
gym = IntVar()
gym.set(50)

gym_entry = Entry(app, textvariable=gym)
gym_entry.place(x=x_input,y=280)

# -----

## label: Quadra de tenis
gym_label = Label(app,text=labels[8])
gym_label.place(x=x_label,y=310)

# entrada: Quadra de tenis
gym = IntVar()
gym.set(50)

gym_entry = Entry(app, textvariable=gym)
gym_entry.place(x=x_input,y=310)

# -----

## label: Spa
spa_label = Label(app,text=labels[9])
spa_label.place(x=x_label,y=340)

# entrada: Spa
spa = IntVar()
spa.set(50)

spa_entry = Entry(app, textvariable=spa)
spa_entry.place(x=x_input,y=340)

# -----

## label: Piscina
pool_label = Label(app,text=labels[10])
pool_label.place(x=x_label,y=370)

# entrada: Piscina
pool = IntVar()
pool.set(50)

pool_entry = Entry(app, textvariable=pool)
pool_entry.place(x=x_input,y=370)

# -----

# -----

## label: Wi-fi
internet_label = Label(app,text=labels[11])
internet_label.place(x=x_label_side,y=100)

# entrada: Wi-fi
internet = IntVar()
internet.set(50)

internet_entry = Entry(app, textvariable=internet)
internet_entry.place(x=x_input_side,y=100)

# -----

## label: Estrelas
stars_label = Label(app,text=labels[12])
stars_label.place(x=x_label_side,y=130)

# entrada: Estrelas
stars = IntVar()
stars.set(50)

stars_entry = Entry(app, textvariable=stars)
stars_entry.place(x=x_input_side,y=130)

# -----

## label: Quartos
rooms_label = Label(app,text=labels[13])
rooms_label.place(x=x_label_side,y=160)

# entrada: Quartos
rooms = IntVar()
rooms.set(50)

rooms_entry = Entry(app, textvariable=rooms)
rooms_entry.place(x=x_input_side,y=160)

# -----

## label: Anos como Membro
membership_years_label = Label(app,text=labels[14])
membership_years_label.place(x=x_label_side,y=190)

# entrada: Anos como Membro
membership_years = IntVar()
membership_years.set(50)

membership_years_entry = Entry(app, textvariable=membership_years)
membership_years_entry.place(x=x_input_side,y=190)

# -----

## label: Meses como Membro
membership_month_label = Label(app,text=labels[15])
membership_month_label.place(x=x_label_side,y=220)

# entrada: Meses como Membro
membership_month = IntVar()
membership_month.set(50)

membership_month_entry = Entry(app, textvariable=membership_month)
membership_month_entry.place(x=x_input_side,y=220)

# -----

## label: Dia da Revisão
revision_day_label = Label(app,text=labels[16])
revision_day_label.place(x=x_label_side,y=250)

# entrada: Dia da Revisão
revision_day = IntVar()
revision_day.set(50)

revision_day_entry = Entry(app, textvariable=revision_day)
revision_day_entry.place(x=x_input_side,y=250)

# -----

# botão de confirmar seleção (Mudar método para todos os parâmetros)
# confirm_button = Button(app,command=getCity,text='Confirmar')
confirm_button = Button(app,text='Calcular Nota')
confirm_button.place(x=x_label_side+30,y=325)

# ## label: resultado
result_predict_label = Label(app,text='Nota Provável:')
result_predict_label.place(x=x_input_side+30,y=310)

# # campo: resultado
result_predict = Label(app, text=get_evaluation())
result_predict.config(font=("Courier", 30))
result_predict.place(x=x_input_side+50,y=340)

app.mainloop()