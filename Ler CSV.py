# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sTA1nvwm3oeG_w6dSHhP-4fYjBLSW1RT
"""
import csv

nova_lista = list()

with open('C:/ProjetosDio/Entrada1.csv', 'r') as entrada:
    ler = csv.reader(entrada)

    # Para pular o cabeçalho
    next(ler)

    for linha in ler:
        if linha not in nova_lista:
            nova_lista.append(linha)
    print(nova_lista)

