# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:06:31 2023

@author: bicom
"""
import random

def list():
    aluno = [1,2,3,4,5,6]
    
    print(aluno)
    print(len(aluno))
    
    for alunos in range(1,10):
        aluno.append(int(random.randint(0,9)))
        
    print(aluno)    

def forloop():
    listao = ["pedro" , "lucia", "heliana" , "let's go"]
    
    
    for y in range(1,4):
        listao.append(int(random.randint(0,200)))

    for x in listao:
        print(x)
        
    print("fim!")
    print(listao)
          
forloop()
