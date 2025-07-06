# 🍄 Posso comer este cogumelo?

> MVP desenvolvido para a disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes** da Pós-Graduação em Engenharia de Software – **PUC-Rio**

## 📌 Proposta

Este projeto é uma solução de **Machine Learning** para um problema de **classificação**:

> **Dadas algumas características físicas de um cogumelo, podemos prever se ele é comestível ou venenoso?**

A aplicação possui uma interface simples para testar diferentes combinações de atributos e avaliar a classificação do modelo treinado.

Notebook no Google Colab: https://colab.research.google.com/github/LucasRosas/MVP-2-Colab/blob/main/mushroom.ipynb

Vídeo de apresentação no YouTube:

[![Apresentação de MVP - Posso comer esse cogumelo? | Lucas Araújo Rosas](https://img.youtube.com/vi/ZRZYooK0m2c/0.jpg)](https://www.youtube.com/watch?v=ZRZYooK0m2c)

---

## 🗂 Estrutura do Projeto

```

MVP-2-Colab/
├── backend/           # API Python com Flask para classificação dos cogumelos
|   └── test           # Dados para teste e o teste do modelo.
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

![image](https://raw.githubusercontent.com/LucasRosas/MVP-2-Colab/refs/heads/main/frontend/public/test.jpg)

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

## Conclusão

O presente trabalho teve como objetivo principal a construção de um modelo de machine learning para a resolução de um problema de classificação. Diferentemente do fluxo habitual, no qual primeiro se identifica um problema e depois se busca um conjunto de dados relevante, aqui o processo foi invertido: partiu-se da escolha de um dataset interessante e, a partir dele, foi elaborado o problema. A questão proposta ("Será que posso comer esse cogumelo?") extrapola o desafio técnico e levanta também questões éticas sobre o uso responsável da Inteligência Artificial, já que uma classificação incorreta pode causar desde uma leve intoxicação alimentar até danos graves e irreversíveis, incluindo a morte. Por esse motivo, foi adicionado à aplicação front-end um alerta explícito indicando que se trata de um exercício acadêmico, sem qualquer garantia quanto à segurança do consumo. De fato, este projeto configura-se como um exercício prático que permitiu explorar e compreender diversas etapas do fluxo de machine learning: seleção de dados, pré-processamento, modelagem, otimização e implementação.

Considerados os dilemas éticos, partimos para a construção do modelo. O dataset original, disponível em https://archive.ics.uci.edu/dataset/73/mushroom, contém 8.124 amostras hipotéticas, correspondentes a 23 espécies de cogumelos classificadas como "comestível" ou "venenoso", descritas por meio de 22 atributos físicos. Para tornar o modelo mais acessível ao usuário final, selecionaram-se apenas as cinco primeiras características para o treinamento.

Foram utilizados quatro algoritmos de classificação: KNN, Decision Tree, Naive Bayes e SVM. Todos apresentaram resultados bastante satisfatórios, com acurácia acima de 98%. Como as variáveis eram todas categóricas, foi necessário aplicar o OneHotEncoder no pré-processamento. Na etapa de otimização, diferentemente do exemplo apresentado na aula 02, não foram utilizados nem o StandardScaler nem o MinMaxScaler, sendo aplicado um conjunto próprio de parâmetros para cada algoritmo no GridSearchCV.

### Análise de resultados do modelo:

Ao comparar a acurácia média da validação cruzada antes e depois da otimização, observou-se uma variação muito pequena, em alguns casos até negativa:

| Modelo           | Acurácia CV Antes | Acurácia CV GridSearch | Variação |
| ---------------- | ----------------- | ---------------------- | -------- |
| **KNN**          | 0.9933            | 0.9937                 | +0.04%   |
| **DecisionTree** | 0.9930            | 0.9931                 | +0.01%   |
| **NaiveBayes**   | 0.9854            | 0.9851                 | -0.03%   |
| **SVM**          | 0.9944            | 0.9944                 | 0%       |

Nos testes com os dados não utilizados no treinamento, o modelo Decision Tree apresentou o melhor score: 0,9971.

Como esperado, o Naive Bayes foi o modelo com as menores acurácias, ainda que bastante altas (cerca de 98,6%).

Em alguns testes iniciais, o modelo KNN alcançou acurácia de 100% com os dados não treinados após otimização. Isso provavelmente ocorreu devido à aleatoriedade da divisão dos dados (mesmo utilizando diferentes seeds além da 42), resultando em conjuntos mais facilmente separáveis.

O modelo SVM, que obteve a maior acurácia média nas validações cruzadas, foi o escolhido para exportação. Para isso, foi necessário ativar a funcionalidade de cálculo de probabilidade, o que aumentou ligeiramente o tempo de treinamento.

Por fim, a aplicação backend foi desenvolvida com um endpoint que permite utilizar o modelo para classificação, e o front-end foi construído e integrado à API. Constatou-se que a escolha do modelo depende fortemente das características iniciais dos dados e do tratamento aplicado a eles. Algumas vezes, mesmo sem otimizações complexas, os modelos podem atingir resultados altamente satisfatórios; outras vezes, ajustes mais refinados serão necessários. Além disso, para cada tipo de dado, diferentes estratégias de pré-processamento e modelagem podem ser recomendadas, sendo essencial a consulta à documentação oficial e à bibliografia especializada.
