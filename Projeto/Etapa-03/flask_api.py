import sys
import os
import shutil
import time
import traceback

from flask import Flask, request, jsonify
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)

# Como citado no README.md, as colunas do arquivo CSV tem que por obrigação serem
# separadas por vírgula E a coluna "status" tem que estar com valores numéricos
# para esse exemplo foi escolhido os 2 tipos de status (CANCELADO = 1; ATIVO = 0)
# Ou seja, na saída da previsão, o valor 1 será o sócio com a previsão de cancelamento.
training_data = 'data/data-set-clube-new-v2.csv'

# selecionando as colunas escolhidas para a previsão. Nessa estapa a Matrícula não
# foi escolhida
include = ['status', 'qtde_em_aberto', 'qtde_em_dia', 'qtde_em_atraso', 'qtde_frequencia_ano']

# variável dependente para análise
dependent_variable = 'status'

# modelos para treino
model_directory = 'model'
model_file_name = f'{model_directory}/model.pkl'
model_columns_file_name = f'{model_directory}/model_columns.pkl'

# Estes serão preenchidos no momento do treinamento
model_columns = None
clf = None


# Create http://host:9999/predict
@app.route('/predict', methods=['POST'])
def predict():
    if clf:
        try:
            json_ = request.json 
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(clf.predict(query))

            return jsonify({'Previsão': [int(x) for x in prediction]})

        except Exception as e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print('Treine um modelo primeiro')
        return 'no model here'


# Create http://host:9999/train
@app.route('/train', methods=['GET']) 
def train():
    # usando random forest como exemplo
    # pode fazer o treinamento separadamente e apenas atualizar os picles
    from sklearn.ensemble import RandomForestClassifier as rf

    df = pd.read_csv(training_data)
    df_ = df[include]

    # Codificando variáveis categóricas
    categoricals = []  

    for col, col_type in df_.dtypes.iteritems():
        if col_type == 'O':
            categoricals.append(col)
        else:
            # Preenchendo possíveis valores com 0
            df_[col].fillna(0, inplace=True)  

    # get_dummies efetivamente cria variáveis codificadas de uma só vez
    df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

    x = df_ohe[df_ohe.columns.difference([dependent_variable])]
    y = df_ohe[dependent_variable]

    # Capturando a lista de colunas que serão usadas para previsão
    global model_columns
    model_columns = list(x.columns)
    joblib.dump(model_columns, model_columns_file_name)

    global clf
    clf = rf()
    start = time.time()
    clf.fit(x, y)

    # Tempo do treino
    print('Treinado em %.1f segundos' % (time.time() - start))

    # Acurácia: em média 91% nos testes executados
    print('Acurácia do treinamento do modelo: %s' % clf.score(x, y))

    joblib.dump(clf, model_file_name)

    return 'Modelo Treinado com successo!'


# Create http://host:9999/wipe
@app.route('/wipe', methods=['GET']) 

# limpa o modelo de treinamento
def wipe():
    try:
        shutil.rmtree('model')
        os.makedirs(model_directory)
        return 'Modelo limpo com sucesso!'

    except Exception as e:
        print(str(e))
        return 'Não foi possível remover e recriar o diretório do modelo'


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80

    try:
        clf = joblib.load(model_file_name)
        print('Modelo Carregado = OK')
        model_columns = joblib.load(model_columns_file_name)
        print('Colunas do Modelo Carregadas = OK')

    except Exception as e:
        print('Nenhum modelo encontrado. Treine primeiro.')
        print(str(e))
        clf = None

    app.run(host='0.0.0.0', port=port, debug=False)
