#!/usr/bin/env python
# -*- coding: utf-8 -*-
def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")

def mostra_registro(registro):
    for campo in registro:
        print(campo)

def mostra_campos(lista_campos):
    for campo in lista_campos:
        print(campo)

def mostra_tabela(lista_registros):
    for registro in lista_registros:
        for campo in registro:
            print(campo)

with open('AM_RevisoesHoteisCaldas.csv', 'r') as f:
    reader = f.readline()
    campos_tabela = reader.split(';')
    reader = f.readline()
    lista_registros = []
    colunas = len(campos_tabela)
    for reader in f:
        registro = reader.split(';')
        if(len(registro) == colunas):
            lista_registros.append(registro)
################ Ative os 4 se quiser ver um registro só #################
#i = input("Digite o numero do registro: ")
#assert(i >= 0 and "O numero tem que ser maior que 0")
#mostra_registro(lista_registros[i])
#pause()
mostra_tabela(lista_registros)
