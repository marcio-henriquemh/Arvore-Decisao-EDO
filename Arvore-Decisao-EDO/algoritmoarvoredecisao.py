import math
from collections import Counter

class NoArvore:
    def __init__(self, atributo=None, classe=None):
        self.atributo, self.classe, self.filhos = atributo, classe, {}

def entropia(exemplos):
    contagem = Counter(e[-1] for e in exemplos)
    p = [c / len(exemplos) for c in contagem.values()]
    return -sum(pi * math.log2(pi) for pi in p)

def ganho_informacao(exemplos, idx):
    ent_total = entropia(exemplos)
    valores = set(e[idx] for e in exemplos)
    ent_cond = sum((len(s := [e for e in exemplos if e[idx] == v]) / len(exemplos)) * entropia(s) for v in valores)
    return ent_total - ent_cond

def learn_decision_tree(exemplos, atributos, parent_exemplos=[]):
    if not exemplos: return NoArvore(classe=Counter(e[-1] for e in parent_exemplos).most_common(1)[0][0])
    classes = [e[-1] for e in exemplos]
    if len(set(classes)) == 1 or not atributos: return NoArvore(classe=classes[0] if len(set(classes)) == 1 else Counter(classes).most_common(1)[0][0])

    melhor_at = max(atributos, key=lambda a: ganho_informacao(exemplos, a))
    raiz = NoArvore(atributo=melhor_at)
    
    for v in set(e[melhor_at] for e in exemplos):
        subset = [e for e in exemplos if e[melhor_at] == v]
        raiz.filhos[v] = learn_decision_tree(subset, [a for a in atributos if a != melhor_at], exemplos)
    return raiz

def prever_id3(arvore, exemplo):
    if arvore.classe is not None: return arvore.classe
    return prever_id3(arvore.filhos[val], exemplo) if (val := exemplo[arvore.atributo]) in arvore.filhos else None

def discretizar_dataset(dataset):
    def cat_zeta(z):
        if abs(z - 1) < 0.05: return "critico"
        return "zero" if z == 0 else ("maior_1" if z > 1 else "menor_1")
    
    return [["positivo" if d[5] > 0 else "negativo", cat_zeta(d[4]), d[6]] for d in dataset]













def imprimir_arvore(no, indent=""):
    if no.classe is not None:
        print(f"{indent}└── 🏁 CLASSE: {no.classe}")
        return
    
    attr_nome = "Sigma (σ)" if no.atributo == 0 else "Zeta (ζ)"
    print(f"{indent}❓ PERGUNTA: {attr_nome}")
    for valor, filho in no.filhos.items():
        print(f"{indent}  ├── Rota: {valor}")
        imprimir_arvore(filho, indent + "  │ ")

