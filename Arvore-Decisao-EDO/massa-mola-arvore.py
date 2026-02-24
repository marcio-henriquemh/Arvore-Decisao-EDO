import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import odeint
from classe_modelagem_fisica import Modelo_Fisico
from analise_estabilidade import Estabilidade_sistema, ArvoreDecisaoFisica, gerar_dataset
from algoritmoarvoredecisao import *

def calcular_metricas(dataset, arvore_id3=None):
    """Calcula Acurácias e Ganhos de Informação."""
    ds_disc = discretizar_dataset(dataset)
    # Acurácia Física
    af = ArvoreDecisaoFisica()
    acc_f = sum(1 for d in dataset if af.prever(Modelo_Fisico(d[0], d[1], d[2])) == d[-1]) / len(dataset)
    
    # Acurácia ID3 e Ganhos
    acc_id3 = sum(1 for i, d in enumerate(dataset) if prever_id3(arvore_id3, ds_disc[i][:2]) == d[-1]) / len(dataset)
    gi = { "σ": ganho_informacao(ds_disc, 0), "ζ": ganho_informacao(ds_disc, 1), "H(S)": entropia(ds_disc) }
    
    return acc_f*100, acc_id3*100, gi


def comparar_previsoes(dataset, arvore_id3, qtd=10):
    """Gera uma tabela comparando as abordagens com os dados reais."""
    ds_disc = discretizar_dataset(dataset)
    af = ArvoreDecisaoFisica()
    
    comparativo = []
    for i in range(min(qtd, len(dataset))):
        m, b, k = dataset[i][0:3]
        real = dataset[i][-1]
        
        prev_fisica = af.prever(Modelo_Fisico(m, b, k))
        prev_id3 = prever_id3(arvore_id3, ds_disc[i][:2])
        
        comparativo.append([f"{m:.0f},{b:.0f},{k:.0f}", real, prev_fisica, prev_id3])
    
    df_comp = pd.DataFrame(comparativo, columns=["Sistema (m,b,k)", "Real", "Prev. Física", "Prev. ID3"])
    print("\n=== COMPARAÇÃO DE PREVISÕES (AMOSTRAS) ===")
    print(df_comp.to_string(index=False))

def exibir_metricas_completas(dataset, arvore_id3):
    """Exibe Entropia, Ganhos e Acurácias."""
    ds_disc = discretizar_dataset(dataset)
    h_total = entropia(ds_disc)
    gi = {"σ": ganho_informacao(ds_disc, 0), "ζ": ganho_informacao(ds_disc, 1)}
    
    af = ArvoreDecisaoFisica()
    acc_f = sum(1 for d in dataset if af.prever(Modelo_Fisico(d[0], d[1], d[2])) == d[-1]) / len(dataset)
    acc_id3 = sum(1 for i, d in enumerate(dataset) if prever_id3(arvore_id3, ds_disc[i][:2]) == d[-1]) / len(dataset)

    print(f"\n=== ANÁLISE DE INFORMAÇÃO ===")
    print(f"Entropia Total H(S): {h_total:.4f}")
    print(f"Ganho σ: {gi['σ']:.4f} (Incerteza Residual: {h_total - gi['σ']:.4f})")
    print(f"Ganho ζ: {gi['ζ']:.4f} (Incerteza Residual: {h_total - gi['ζ']:.4f})")
    print(f"\nACURÁCIA FINAL -> Física: {acc_f*100:.1f}% | ID3: {acc_id3*100:.1f}%")

if __name__ == "__main__":
    #  Preparação
    dataset = gerar_dataset(100)
    ds_disc = discretizar_dataset(dataset)
    arvore_id3 = learn_decision_tree(ds_disc, [0, 1])

    #  Saídas de Dados
    exibir_metricas_completas(dataset, arvore_id3)
    comparar_previsoes(dataset, arvore_id3)

    #  Visualização Gráfica
    df = pd.DataFrame(dataset, columns=["m","b","k","wn","zeta","sigma","classe"])
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    for c, cor in {"Sub":"blue", "Super":"green", "Critico":"red", "Instavel":"orange", "Nao amortecido":"purple"}.items():
        sub = df[df["classe"] == c]
        ax1.scatter(sub["zeta"], sub["sigma"], c=cor, label=c, edgecolors='k')
    ax1.set_title("Espaço ζ vs σ"); ax1.legend()

    t = np.linspace(0, 5, 500)
    for i in range(10):
        sis = Modelo_Fisico(dataset[i][0], dataset[i][1], dataset[i][2])
        ax2.plot(t, odeint(sis.edo, [0.1, 0], t)[:, 0], alpha=0.5)
    ax2.set_title("Respostas Temporais"); plt.show()


imprimir_arvore(arvore_id3)
