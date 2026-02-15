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

ACURÁCIA DA ÁRVORE: 98.00%

Distribuição das classes:
Critico: 3  
Instavel: 3  
Sub: 26  
Super: 18  

Isso prova que a árvore representa corretamente a teoria física.

---

# 📈 Visualizações geradas

O projeto também gera:

🌳 Imagem da árvore de decisão  
Gerada automaticamente via Graphviz.

Arquivo produzido:
arvore_fisica_suspensao.png

---

# 📂 Estrutura do projeto

projeto/
 ├── classe_modelagem_fisica.py  
 ├── analise_estabilidade.py  
 ├── gerar_imagem_arvore.py  
 ├── main.py  
 └── README.md  

---

# ▶️ Como executar

## 1️⃣ Instalar dependências

pip install numpy matplotlib scipy scikit-learn graphviz

Linux:

sudo pacman -S graphviz   # Arch  
sudo apt install graphviz # Ubuntu  

---

## 2️⃣ Rodar o projeto

python main.py

Gerar imagem da árvore:

python gerar_imagem_arvore.py

---

# 💡 Conceitos envolvidos

Este projeto integra:

- Sistemas Dinâmicos  
- Equações Diferenciais  
- Análise de Estabilidade  
- Teoria de Controle  
- Árvores de Decisão  
- Explicabilidade em IA (XAI)

---

# 🚀 Ideia principal

Mostrar que **Machine Learning pode ser interpretável**  
quando combinamos modelos de decisão com leis físicas.

Exemplo de:
Physics-Informed Decision Trees

---

# 👨‍💻 Autor

Projeto desenvolvido como estudo interdisciplinar entre:

- Sistemas Dinâmicos  
- Inteligência Artificial  
- Modelagem Física  
