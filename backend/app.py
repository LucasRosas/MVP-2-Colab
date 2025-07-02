from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from flask_cors import CORS
from pydantic import BaseModel, Field

import joblib
import pandas as pd

info = Info(title="Pode comer? - API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

class ClassifyViewSchema(BaseModel):
    """Representação do schema de classificação."""
    p: float
    e: float

class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    mesage: str

class ClassifySchemaSearch(BaseModel):
    """ Define como deve ser a estrutura que representa a busca.
    """
    capShape: str = Field(example="x", description="Formato do chapéu")
    capSurface: str = Field(example="y", description="Superfície do chapéu")
    capColor: str = Field(example="z", description="Cor do chapéu")
    bruises: str = Field(example="t", description="Presença de manchas")
    odor: str = Field(example="u", description="Odor do cogumelo")
    

# definindo tags
classify_tag = Tag(name="Classificação", description="Classificação")

@app.get('/')
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/classify', tags=[classify_tag],
         responses={"200": ClassifyViewSchema, "404": ErrorSchema})
def get_classify(query: ClassifySchemaSearch):
    """
    """
    capShape = query.capShape
    capSurface = query.capSurface
    capColor = query.capColor
    bruises = query.bruises
    odor = query.odor  

    # Carrega o modelo
    modelo = joblib.load("modelo_knn_cogumelos.pkl")

    # Lista completa de atributos (exceto o alvo)
    atributos = ['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor']

    # Dado parcial (exemplo real)
    entrada_parcial = {
        'cap-shape': capShape,
        'cap-surface': capSurface,
        'cap-color': capColor,
        'bruises': bruises,
        'odor': odor
    }

    # Preenche os outros com valores neutros ou '?'
    entrada_completa = {col: entrada_parcial.get(col, '?') for col in atributos}

    # Cria DataFrame com uma linha
    df_teste = pd.DataFrame([entrada_completa])

    # Faz a previsão
    probabilidades = modelo.predict_proba(df_teste)

    # Mapear o índice da classe
    classes = modelo.classes_
    mapa_classes = {0: 'comestível', 1: 'venenoso'}

    result = {}

    # Mostra as chances
    for classe, prob in zip(classes, probabilidades[0]):
        nome_legivel = mapa_classes.get(classe, classe)
        result[nome_legivel] = prob

    return {"result": result}, 200    

if __name__ == "__main__":
    app.run(debug=True)