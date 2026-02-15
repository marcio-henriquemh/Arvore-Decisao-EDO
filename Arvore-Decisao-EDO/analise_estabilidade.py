from classe_modelagem_fisica import Modelo_Fisico
import numpy as np

# ==========================================================
# ANALISE DE ESTABILIDADE DO SISTEMA MASSA–MOLA–AMORTECEDOR
# ==========================================================

class Estabilidade_sistema(Modelo_Fisico):

    # ---------------- POLOS DO SISTEMA ----------------
    def polos(self):
        discriminante = self.b_constante_amortecimento**2 - 4*self.massa*self.k_constante_mola
        
        if discriminante >= 0:
            s1 = (-self.b_constante_amortecimento + np.sqrt(discriminante)) / (2*self.massa)
            s2 = (-self.b_constante_amortecimento - np.sqrt(discriminante)) / (2*self.massa)
            return s1, s2
        else:
            real = -self.b_constante_amortecimento / (2*self.massa)
            imag = np.sqrt(-discriminante) / (2*self.massa)
            return complex(real, imag), complex(real, -imag)

    # ---------------- FREQUENCIA NATURAL ----------------
    def frequencia_natural(self):
        return np.sqrt(self.k_constante_mola / self.massa)

    # ---------------- RAZAO DE AMORTECIMENTO ----------------
    def razao_amortecimento(self):
        return self.b_constante_amortecimento / (2 * np.sqrt(self.massa * self.k_constante_mola))

    # ---------------- PARTE REAL DOMINANTE ----------------
    def parte_real_dominante(self):
        s1, s2 = self.polos()
        real_s1 = s1.real if isinstance(s1, complex) else s1
        real_s2 = s2.real if isinstance(s2, complex) else s2
        return max(real_s1, real_s2)

    # ---------------- CLASSIFICACAO FISICA REAL ----------------
    def classificar(self):
        sigma = self.parte_real_dominante()
        zeta = self.razao_amortecimento()

        if sigma > 0:
            return "Instavel"
        if abs(zeta - 1) < 0.05:
            return "Critico"
        if zeta > 1:
            return "Super"
        if zeta == 0:
            return "Nao amortecido"
        return "Sub"






# ==========================================================
# ARVORE DE DECISAO BASEADA NA FISICA (SEM MACHINE LEARNING)
# ==========================================================

class ArvoreDecisaoFisica:

    def prever(self, sistema):
        analise = Estabilidade_sistema(
            sistema.massa,
            sistema.b_constante_amortecimento,
            sistema.k_constante_mola
        )

        zeta = analise.razao_amortecimento()
        sigma = analise.parte_real_dominante()

        # NÓ 1 — instabilidade
        if sigma > 0:
            return "Instavel"

        # NÓ 2 — sem amortecimento
        if zeta == 0:
            return "Nao amortecido"

        # NÓ 3 — crítico (ANTES do ζ<1)
        if abs(zeta - 1) < 0.05:
            return "Critico"

        # NÓ 4 — super
        if zeta > 1:
            return "Super"

        # NÓ FINAL
        return "Sub"


# ==========================================================
# GERADOR DE DATASET FISICO (50 SISTEMAS ALEATORIOS)
# ==========================================================

def gerar_sistema_aleatorio():
    """
    Gera um sistema massa-mola-amortecedor fisicamente plausível.
    Intervalos escolhidos para produzir todos os tipos de resposta.
    """

    massa = np.random.uniform(100, 2000)      # kg
    k = np.random.uniform(5000, 40000)        # N/m
    
    # amortecimento pode ser negativo -> permite instabilidade
    b = np.random.uniform(-2000, 20000)       # N·s/m

    return Modelo_Fisico(massa, b, k)


def gerar_dataset(qtd=50):
    """
    Gera dataset rotulado pela física:
    [m, b, k, wn, zeta, sigma, classe]
    """

    dataset = []

    for _ in range(qtd):
        sistema = gerar_sistema_aleatorio()
        analise = Estabilidade_sistema(
            sistema.massa,
            sistema.b_constante_amortecimento,
            sistema.k_constante_mola
        )

        wn = analise.frequencia_natural()
        zeta = analise.razao_amortecimento()
        sigma = analise.parte_real_dominante()
        classe = analise.classificar()

        dataset.append([
            sistema.massa,
            sistema.b_constante_amortecimento,
            sistema.k_constante_mola,
            wn,
            zeta,
            sigma,
            classe
        ])

    return np.array(dataset, dtype=object)




