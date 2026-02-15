from classe_modelagem_fisica import Modelo_Fisico
import numpy as np, random
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from analise_estabilidade import Estabilidade_sistema,ArvoreDecisaoFisica




if __name__ == "__main__":

    print("\nTESTANDO ARVORE DE DECISAO FISICA\n")

    arvore = ArvoreDecisaoFisica()

    def testar_sistema(m,b,k):
        sistema = Modelo_Fisico(m,b,k)
        analise = Estabilidade_sistema(m,b,k)

        classe_real = analise.classificar()
        classe_arvore = arvore.prever(sistema)

        print("-----------------------------------")
        print(f"m={m}  b={b}  k={k}")
        print("Classe fisica real:", classe_real)
        print("Classe pela arvore:", classe_arvore)

    # exemplos individuais
    testar_sistema(250, 600, 20000)        # nao amortecido
    testar_sistema(250, 1000, 20000)     # subamortecido
    testar_sistema(250, 344, 20000)     # critico aprox
    testar_sistema(250, 12000, 20000)    # super
    testar_sistema(250, -666, 20000)     # instavel

    # ======================================================
    # VALIDACAO COM 50 SISTEMAS ALEATORIOS
    # ======================================================

    print("\nGERANDO DATASET DE 50 SISTEMAS...\n")

    from analise_estabilidade import gerar_dataset  # importa o gerador

    dataset = gerar_dataset(50)

    def validar_arvore(dataset):
        arvore = ArvoreDecisaoFisica()
        acertos = 0
        
        for linha in dataset:
            m,b,k,_,_,_,classe_real = linha
            
            sistema = Modelo_Fisico(m,b,k)
            previsao = arvore.prever(sistema)
            
            if previsao == classe_real:
                acertos += 1
        
        acc = acertos/len(dataset)*100
        print(f"\nACURÁCIA DA ÁRVORE: {acc:.2f}%")

    validar_arvore(dataset)

    print("\nDistribuição das classes no dataset:")

    classes, contagem = np.unique(dataset[:,6], return_counts=True)
    for c,n in zip(classes,contagem):
        print(f"{c}: {n}")

    print("\n PROJETO COMPLETO E VALIDADO!")




# ======================================================
# PLOT DA ARVORE DE DECISAO FISICA
# ======================================================

def plotar_arvore():
    plt.figure(figsize=(10,7))
    plt.axis("off")

    def caixa(texto, x, y):
        plt.text(x, y, texto, ha='center', va='center',
                 bbox=dict(boxstyle="round,pad=0.4"))

    # nós
    caixa("σ ≥ 0 ?", 0.5, 0.9)

    caixa("Instável", 0.85, 0.7)

    caixa("ζ = 0 ?", 0.25, 0.7)
    caixa("Não amortecido", 0.05, 0.5)

    caixa("ζ < 1 ?", 0.35, 0.5)
    caixa("Subamortecido", 0.20, 0.3)

    caixa("|ζ-1|<0.05 ?", 0.55, 0.3)
    caixa("Crítico", 0.45, 0.1)
    caixa("Superamortecido", 0.75, 0.1)

    # conexões
    plt.plot([0.5,0.85],[0.87,0.73])
    plt.plot([0.5,0.25],[0.87,0.73])

    plt.plot([0.25,0.05],[0.67,0.53])
    plt.plot([0.25,0.35],[0.67,0.53])

    plt.plot([0.35,0.20],[0.47,0.33])
    plt.plot([0.35,0.55],[0.47,0.33])

    plt.plot([0.55,0.45],[0.27,0.13])
    plt.plot([0.55,0.75],[0.27,0.13])

    plt.title("Árvore de Decisão Baseada na Física")
    plt.show()

plotar_arvore()



# ======================================================
# SIMULAR ALGUNS SISTEMAS DO DATASET
# ======================================================

print("\nSIMULANDO ALGUNS SISTEMAS DO DATASET...")

t = np.linspace(0,5,800)
estado_inicial = [0.1,0]

plt.figure(figsize=(12,7))

cores = {
    "Sub":"blue",
    "Super":"green",
    "Critico":"red",
    "Instavel":"orange",
    "Nao amortecido":"purple"
}

for i in range(10):   # plotar 10 exemplos para não poluir
    m,b,k,_,_,_,classe = dataset[i]

    sistema = Modelo_Fisico(m,b,k)
    sol = odeint(sistema.edo, estado_inicial, t)

    plt.plot(t, sol[:,0], color=cores[classe], alpha=0.7)

plt.title("Resposta no Tempo de Sistemas Aleatórios")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.grid(True)

# legenda manual
for classe,cor in cores.items():
    plt.plot([],[], color=cor, label=classe)

plt.legend()
plt.show()


