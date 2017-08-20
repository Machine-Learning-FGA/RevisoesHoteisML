# -*- coding: utf-8 -*-
from Tkinter import *
import ttk

app = Tk()
app.title("Wall-e Society - Revisões de Hotéis")
app.geometry("500x500")

# etiqueta
city_label = Label(app, text='Revisões de Hotéis')
city_label.place(x=200,y=50)

# cidade
city_label = Label(app, text='Cidade')
city_label.place(x=50,y=100)

# combobox
combo_city = ttk.Combobox(app)
combo_city.place(x=160,y=100)
combo_city['values'] = ('Gama','Santa Maria','Ocidental', 'Valparadise', '...')
combo_city.current(0)

# seleção de cidade
# def getCity():
#     combo_city.get()
#     test.set("Cidade: "+combo_city.get())

# botão de confirmar seleção (Mudar método para todos os parâmetros)
# confirm_button = Button(app,command=getCity,text='Confirmar')
confirm_button = Button(app,text='Confirmar')
confirm_button.place(x=50,y=400)

# testar seleção do combobox
# test = StringVar()
# test.set("Cidade: ")
# test_label = Label(app, textvariable=test)
# test_label.place(x=80,y=170)

# ------

# revisões
revision_label = Label(app,text='Total de revisões:')
revision_label.place(x=50,y=130)

revision = IntVar()
revision.set(50)

revision_entry = Entry(app, textvariable=revision)
revision_entry.place(x=160,y=130)

hotel_revision_label = Label(app,text='Revisões de Hotel:')
hotel_revision_label.place(x=50,y=160)

hotel_revision = IntVar()
hotel_revision.set(50)

hotel_revision_entry = Entry(app, textvariable=hotel_revision)
hotel_revision_entry.place(x=160,y=160)

# ------

# votos hoteis
hotel_votes_label = Label(app,text='Votos de Hotel:')
hotel_votes_label.place(x=50,y=190)

hotel_votes = IntVar()
hotel_votes.set(50)

hotel_votes_entry = Entry(app, textvariable=hotel_votes)
hotel_votes_entry.place(x=160,y=190)

# ------

# periodo
period_label = Label(app,text='Período:')
period_label.place(x=50,y=220)

combo_period = ttk.Combobox(app)
combo_period.place(x=160,y=220)
combo_period['values'] = ('Dez-Fev','Mar-Mai','Jun-Ago', 'Set-Nov', 'Dez-Fev')
combo_period.current(0)

app.mainloop()