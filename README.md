# Projeto Disciplina de Fundamentos de Inteligência Artificial
Aqui está a equipe principal:

**Equipe de Desenvolvimento**
- Marcos Vinicius
- Marcio Henrique Matos De Freitas

# 🌳 Árvore de Decisão Física para Análise de Estabilidade  
### Sistema Massa–Mola–Amortecedor

Este projeto demonstra como aplicar o conceito de **Árvore de Decisão** sem Machine Learning para classificar automaticamente o comportamento de sistemas dinâmicos de segunda ordem usando **apenas leis da física**.


A ideia central é:  
👉 Fazer a árvore de decisão “aprender a física”.

---

# 🎯 Objetivo do Projeto

Modelar e classificar a resposta de sistemas massa–mola–amortecedor em:

- Instável  
- Não amortecido  
- Subamortecido  
- Criticamente amortecido  
- Superamortecido  

E validar a árvore comparando sua previsão com o resultado obtido diretamente da modelagem matemática do sistema.

---

# ⚙️ Modelo físico utilizado

Sistema clássico:

m x¨ + b x˙ + kx = 0

Onde:

| Parâmetro | Significado |
|---|---|
| m | Massa (kg) |
| b | Coeficiente de amortecimento (N·s/m) |
| k | Constante da mola (N/m) |

---

## 📌 Parâmetros físicos calculados

O projeto calcula automaticamente:

### Frequência natural
ωn = sqrt(k/m)

### Razão de amortecimento
ζ = b / (2√(mk))

### Polos do sistema
s = (-b ± √(b² − 4mk)) / (2m)

A parte real dominante dos polos define a **estabilidade** do sistema.

---

# 🌳 Árvore de decisão baseada na física

A árvore criada manualmente segue exatamente a teoria de sistemas dinâmicos:

σ > 0 ? → Instável

senão:

ζ = 0 ? → Não amortecido

senão:

|ζ − 1| < 0.05 ? → Crítico

senão:

ζ > 1 ? → Superamortecido

senão → Subamortecido

Essa árvore é **determinística, interpretável e explicável**.

---

# 🧪 Dataset físico automático

* classe real no dataset não é atribuída manualmente nem aprendida pelo algoritmo de machine learning. Ela é gerada de forma determinística a partir do modelo físico do sistema massa–mola–amortecedor. Inicialmente, são sorteados valores para os parâmetros físicos 
m
m (massa), 
b
b (coeficiente de amortecimento) e 
k
k (constante elástica). Esses valores apenas definem um sistema dinâmico possível dentro do espaço paramétrico admissível.

* A classificação do sistema decorre diretamente das propriedades matemáticas das raízes da equação característica associada à equação diferencial 
mx¨+bx˙+kx=0
m
x
¨
+b
x
˙
+kx=0. Dependendo do valor de 
ζ
ζ e do sinal de 
σ
σ, o sistema pode ser classificado como instável, subamortecido, superamortecido ou criticamente amortecido

O projeto gera automaticamente sistemas físicos aleatórios:

- 50 sistemas massa–mola–amortecedor
- Parâmetros fisicamente plausíveis
- Cada sistema é rotulado pela própria física

Formato do dataset:

[m, b, k, wn, zeta, sigma, classe]

---

# 🔍 Validação da árvore

O sistema compara:

- Classificação real (equações diferenciais)
- Classificação da árvore de decisão

Exemplo de saída:
### === ANÁLISE DE INFORMAÇÃO ===
*   **Entropia Total H(S):** 1.4789
*   **Ganho $\sigma$:** 0.4022 (Incerteza Residual: 1.0767)
*   **Ganho $\zeta$:** 1.1643 (Incerteza Residual: 0.3146)
*   **ACURÁCIA FINAL ->** Física: 100.0% | ID3: 100.0%

### === COMPARAÇÃO DE PREVISÕES (AMOSTRAS) ===


| Sistema (m,b,k) | Real | Prev. Física | Prev. ID3 |
| :--- | :--- | :--- | :--- |
| 1493, -176, 6118 | Instavel | Instavel | Instavel |
| 1454, 5727, 25505 | Sub | Sub | Sub |
| 1879, 16033, 13430 | Super | Super | Super |
| 706, 17974, 5561 | Super | Super | Super |
| 1341, -643, 30008 | Instavel | Instavel | Instavel |
| 1482, 4331, 20701 | Sub | Sub | Sub |
| 1145, 3202, 24768 | Sub | Sub | Sub |
| 746, 7823, 16400 | Super | Super | Super |
| 1896, 9583, 19864 | Sub | Sub | Sub |
| 1499, 16954, 22303 | Super | Super | Super |

**Conclusão:** Isso prova que a árvore representa corretamente a teoria física.


---


# 📂 Estrutura do projeto

projeto/
 ├── classe_modelagem_fisica.py  
 ├── analise_estabilidade.py  
 ├── massa-mola-arvore.py  
 ├── algoritmoarvoredecisao.py  
 └── README.md  

---

# ▶️ Como executar

## 1️⃣ Instalar dependências

pip install numpy matplotlib scipy
### Detalhes técnicos :
*   `numpy` (manipulação numérica)
*   `matplotlib.pyplot` (gráficos)
*   `scipy.integrate.odeint` (integração de equações diferenciais)
*   `math` (biblioteca padrão)
*   `collections.Counter` (biblioteca padrão)

O comando `pip install numpy matplotlib scipy` instala todas as bibliotecas de terceiros necessárias.


---

## 2️⃣ Rodar o projeto

python massa-mola-arvore.py


---

# 💡 Conceitos envolvidos

Este projeto integra:

- Sistemas Dinâmicos  
- Equações Diferenciais  
- Análise de Estabilidade  
- Teoria de Controle  
- Árvores de Decisão  

---

# 🚀 Ideia principal

Mostrar que **Machine Learning pode ser interpretável**  
quando combinamos modelos de decisão com leis físicas.
---

# 👨‍💻 Autor

Projeto desenvolvido como estudo interdisciplinar entre:

- Sistemas Dinâmicos  
- Inteligência Artificial  
- Modelagem Física  
