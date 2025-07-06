import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Parâmetros    
url_dados = "./test/dados_teste.csv"
colunas = ['cap-shape','cap-surface','cap-color','bruises','odor','classificacao']

# Carga dos dados
dataset = pd.read_csv(url_dados, names=colunas, header=0,skiprows=0, delimiter=',')

X_test = dataset[colunas[:-1]] # Atributos
y_test = dataset['classificacao']

def test_model():
    modelo = joblib.load("best_model_mushroom.pkl")
    predicoes = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, predicoes)
    assert accuracy >= 0.8, "Acurácia do modelo abaixo de 80%"