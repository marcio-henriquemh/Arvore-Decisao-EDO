import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

'''
MODELAGEM DA EDO

Objetivo: descrever matematicamente a suspensão.
'''


'''
Informações 

Forças é dada em F=ma, massa x Aceleração
derivadas
V(t)=y'
a(t)=y''

Forca B atrito

F_B=(X'- Y') o atrito ou amortecimento é ue muitas vezes é o que se quer dizer com "atrito viscoso" — é proporcional à diferença de velocidade,
 e não apenas à diferença de posição, entre dois ponto.

 F_k=(X,Y) A força elástica (
) não depende apenas da posição da massa, mas da deformação total da mola, 

que é dada pela diferença entre o deslocamento das suas duas extremidade

EDO

    m*y'' + b*(y' - x') + k*(y - x) = 0

'''





class Modelo_Fisico:
    def __init__(self, massa,b_constante_amortecimento,k_constante_mola):

        self.massa=massa
        self.b_constante_amortecimento=b_constante_amortecimento
        self.k_constante_mola=k_constante_mola
        pass
     
     
    def forca_mola(self,x):
        return -self.k_constante_mola*x
    def forca_amortecedor(self,x_linha):
        return -self.b_constante_amortecimento*x_linha
    def segunda_lei_newton(self,x,x_linha):
        soma_forca=self.forca_mola(x)+self.forca_amortecedor(x_linha)
        x_2_linha=soma_forca/self.massa

        return x_2_linha
    def edo(self, estado, t):
        # estado = [x(t), x'(t)]
        x = estado[0]
        x_linha = estado[1]
        
        # Retorna [x'(t), x''(t)]
        return [x_linha, self.segunda_lei_newton(x, x_linha)]
    

     
