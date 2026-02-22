import numpy as np
from classe_modelagem_fisica import Modelo_Fisico

class Estabilidade_sistema(Modelo_Fisico):
    """Análise de estabilidade com cálculos otimizados."""

    def info_fisica(self):
        """Retorna (zeta, sigma) em uma única chamada para evitar cálculos repetidos."""
        m, b, k = self.massa, self.b_constante_amortecimento, self.k_constante_mola
        
        # Frequência natural e Razão de amortecimento (zeta)
        wn = np.sqrt(k / m)
        zeta = b / (2 * np.sqrt(m * k))
        
        # Parte real dominante (sigma)
        discriminante = b**2 - 4*m*k
        if discriminante >= 0:
            sigma = (-b + np.sqrt(discriminante)) / (2*m)
        else:
            sigma = -b / (2*m) # Parte real de polos complexos
            
        return wn, zeta, sigma

    def classificar(self):
        wn, zeta, sigma = self.info_fisica()
        
        if sigma > 0:           return "Instavel"
        if zeta == 0:          return "Nao amortecido"
        if abs(zeta - 1) < 0.05: return "Critico"
        return "Super" if zeta > 1 else "Sub"

class ArvoreDecisaoFisica:
    """Simula a árvore de decisão usando a lógica da classe física."""
    def prever(self, sistema):
        return Estabilidade_sistema(sistema.massa, sistema.b_constante_amortecimento, sistema.k_constante_mola).classificar()

def gerar_dataset(qtd=50):
    dataset = []
    for _ in range(qtd):
        # Geração aleatória de parâmetros
        m, k = np.random.uniform(100, 2000), np.random.uniform(5000, 40000)
        b = np.random.uniform(-2000, 20000)
        
        sistema = Estabilidade_sistema(m, b, k)
        wn, zeta, sigma = sistema.info_fisica()
        
        dataset.append([m, b, k, wn, zeta, sigma, sistema.classificar()])
        
    return np.array(dataset, dtype=object)