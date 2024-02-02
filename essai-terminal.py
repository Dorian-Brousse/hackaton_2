import numpy as np
import random as rd
import pandas as pd
import sys
from argparse import ArgumentParser

#truc qui génère
def gener():
    L=[]
    while len(L)!=9:
        k=rd.randint(0,8)
        if k not in L:
            L.append(k)
    L1 = np.array(L).reshape(3,3)
    return L1

def bouger_puzzle(puzzle, dir):
    assert dir in ["h","b","g","d"]
    #on va faire qqchose pour trouver les coordonnées du zéro dans le puzzle
    i = np.where(puzzle == 0)
    if dir == "h":
        if i[0][0]!=0:
            k=puzzle[i[0][0]-1][i[1][0]]
            puzzle[i[0][0]-1][i[1][0]]=0
            puzzle[i[0][0]][i[1][0]]=k
        else:
            k=puzzle[2][i[1][0]]
            puzzle[2][i[1][0]]=0
            puzzle[i[0][0]][i[1][0]]=k 
    elif dir == "b":
        if i[0][0]!=2:
            k=puzzle[i[0][0]+1][i[1][0]]
            puzzle[i[0][0]+1][i[1][0]]=0
            puzzle[i[0][0]][i[1][0]]=k
        else:
            k=puzzle[0][i[1][0]]
            puzzle[0][i[1][0]]=0
            puzzle[i[0][0]][i[1][0]]=k 
    elif dir == "g":
        if i[1][0]!=0:
            k=puzzle[i[0][0]][i[1][0]-1]
            puzzle[i[0][0]][i[1][0]-1]=0
            puzzle[i[0][0]][i[1][0]]=k
        else:
            k=puzzle[i[0][0]][2]
            puzzle[i[0][0]][2]=0
            puzzle[i[0][0]][i[1][0]]=k 
    elif dir == "d":
        if i[1][0]!=2:
            k=puzzle[i[0][0]][i[1][0]+1]
            puzzle[i[0][0]][i[1][0]+1]=0
            puzzle[i[0][0]][i[1][0]]=k
        else:
            k=puzzle[i[0][0]][0]
            puzzle[i[0][0]][0]=0
            puzzle[i[0][0]][i[1][0]]=k 
    return puzzle 


l=gener()
res = [i for i in range(1,9)]
res.append(0)
while np.any(l != np.array(res).reshape(3,3)):
    print(l)
    dir = input("h, b, g, d")
    bouger_puzzle(l,dir)
print("bien joué l'artiste")

