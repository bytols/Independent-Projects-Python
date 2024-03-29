# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 20:57:20 2023

@author: bicom
"""

def main():
    char1 = 'f'
    char2 = 'b'
    
    
    if char1 == "f" and char2 == "b":
        print("a vida é muito feliz")
    if char1 == "f":
        print("char 1 é igual a f")
    if char2 == "b":
        print("char 2  é igual a b")
    if char1 != "f" and char2 != "b":
        print("a vida é muito trsite")
        
    

def chutes():
    numero1 = 2
    numero2 = 6
    numero3 = 7
    
    
    if numero1 == 3 or numero2 == 3 or numero3 == 5:
        print("você acertou em pelo menos um dos chutes")
    else:
        print("você  errou todos os chutes")
        
chutes()