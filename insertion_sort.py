# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:49:45 2023

@author: bicom
"""
lista = [10,7,3,4]

def insertion_sort(lista):
    n = len(lista)
    i = 0
    lista = [10,7,3,4]
    
    print(len(lista))
    print(lista)
    
    for i in range(1, n):
        chave = lista[i]
        j = i -1
        while lista[j] > chave and j >= 0:
                lista[j+1] = lista[j]
                j = j - 1
        lista[j+1] = chave
        
    print(lista)
    



insertion_sort(lista)
