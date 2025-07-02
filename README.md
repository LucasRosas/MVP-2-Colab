# 🍄 Posso comer este cogumelo?

> MVP desenvolvido para a disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes** da Pós-Graduação em Engenharia de Software – **PUC-Rio**

## 📌 Proposta

Este projeto é uma solução de **Machine Learning** para um problema clássico de **classificação**:

> **Dadas algumas características físicas de um cogumelo, podemos prever se ele é comestível ou venenoso?**

A aplicação possui uma interface simples para testar diferentes combinações de atributos e avaliar a classificação do modelo treinado.

---

## 🗂 Estrutura do Projeto

```

MVP-2-Colab/
├── backend/           # API Python com Flask para classificação dos cogumelos
├── frontend/          # Interface desenvolvida em Vue.js
├── mushroom/          # Dados originais utilizados no treinamento
├── mushroom.ipynb     # Notebook com o pipeline de treino e exportação do modelo
└── README.md          # Este arquivo

```

---

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/LucasRosas/MVP-2-Colab.git
cd MVP-2-Colab
```

### 🧠 Backend (Flask)

```bash
cd backend
```

Crie e ative um ambiente virtual (recomendado):

```bash
# Instale o virtualenv se necessário
pip install virtualenv

# Crie o ambiente
python -m venv .venv

# Ative o ambiente
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
flask run --host 0.0.0.0 --port 5000
```

A documentação interativa estará disponível em:
📎 [http://localhost:5000/openapi/swagger](http://localhost:5000/openapi/swagger)

#### 🧪 Rota disponível

```
GET /classifier
```

**Query Parameters:**

| Parâmetro  | Tipo | Descrição             | Exemplo |
| ---------- | ---- | --------------------- | ------- |
| capShape   | str  | Formato do chapéu     | x       |
| capSurface | str  | Textura da superfície | y       |
| capColor   | str  | Cor do chapéu         | w       |
| bruises    | str  | Presença de manchas   | t       |
| odor       | str  | Odor característico   | n       |

---

#### Rodar teste do modelo

Para rodar o teste do modelo basta executar

```bash
 pytest
```

### 🌿 Frontend (Vue.js)

Em outro terminal, a partir da raiz do projeto:

```bash
cd frontend
```

Instale as dependências:

```bash
npm install
```

Execute a aplicação:

```bash
npm run dev
```

Acesse a interface web em:
🌐 [http://localhost:5173](http://localhost:5173)

---

## 🔤 Classificações possíveis

| Atributo        | Código | Descrição              |
| --------------- | ------ | ---------------------- |
| **cap-shape**   | b      | bell (sino)            |
|                 | c      | conical (cônico)       |
|                 | x      | convex (convexo)       |
|                 | f      | flat (plano)           |
|                 | k      | knobbed (protuberante) |
|                 | s      | sunken (afundado)      |
| **cap-surface** | f      | fibrous (fibrosa)      |
|                 | g      | grooves (sulcada)      |
|                 | y      | scaly (escamosa)       |
|                 | s      | smooth (lisa)          |
| **cap-color**   | n      | brown (marrom)         |
|                 | b      | buff (amarelado claro) |
|                 | c      | cinnamon (canela)      |
|                 | g      | gray (cinza)           |
|                 | r      | green (verde)          |
|                 | p      | pink (rosa)            |
|                 | u      | purple (roxo)          |
|                 | e      | red (vermelho)         |
|                 | w      | white (branco)         |
|                 | y      | yellow (amarelo)       |
| **bruises**     | t      | sim                    |
|                 | f      | não                    |
| **odor**        | a      | almond (amêndoa)       |
|                 | l      | anise (anis)           |
|                 | c      | creosote (alcatrão)    |
|                 | y      | fishy (peixe)          |
|                 | f      | foul (fétido)          |
|                 | m      | musty (mofo)           |
|                 | n      | none (nenhum)          |
|                 | p      | pungent (picante)      |
|                 | s      | spicy (especiado)      |

---

## 🧠 Sobre o modelo

O modelo foi treinado com dados reais contendo características físicas e sensoriais de cogumelos, com a classificação final (`e` para comestível, `p` para venenoso). Foi utilizada uma abordagem de pré-processamento com `OneHotEncoder` e experimentação com diferentes algoritmos: `KNN`, `DecisionTree`, `NaiveBayes` e `SVM`.
