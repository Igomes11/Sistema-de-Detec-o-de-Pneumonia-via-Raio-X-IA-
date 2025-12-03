import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import sqlite3
import datetime

# --- SEU CÓDIGO DO APP AQUI ---
# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Detector de Pneumonia", page_icon="🫁")

# --- BANCO DE DADOS (SQLite) ---
def init_db():
    conn = sqlite3.connect('historico_diagnosticos.db')
    c = conn.cursor()
    # Cria tabela se não existir
    c.execute('''
        CREATE TABLE IF NOT EXISTS interacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            nome_arquivo TEXT,
            resultado_predicao TEXT,
            confianca TEXT
        )
    ''')
    conn.commit()
    conn.close()

def salvar_no_banco(nome_arquivo, resultado, confianca):
    conn = sqlite3.connect('historico_diagnosticos.db')
    c = conn.cursor()
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO interacoes (data_hora, nome_arquivo, resultado_predicao, confianca) VALUES (?, ?, ?, ?)",
              (data_atual, nome_arquivo, resultado, confianca))
    conn.commit()
    conn.close()

# Inicializa o banco ao abrir o app
init_db()

# --- CARREGAR MODELO ---
@st.cache_resource
def load_model():
    # Certifique-se que o arquivo .h5 está na mesma pasta
    model = tf.keras.models.load_model('modelo_pneumonia.h5')
    return model

try:
    model = load_model()
except:
    st.error("Erro: Arquivo 'modelo_pneumonia.h5' não encontrado. Faça o upload dele para a pasta do projeto.")

# --- INTERFACE ---
st.title("🫁 Sistema de Auxílio ao Diagnóstico - Pneumonia")
st.write("Faça upload de uma imagem de Raio-X de Tórax.")

file = st.file_uploader("Envie a imagem (JPG/PNG)", type=["jpg", "png", "jpeg"])

if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, caption='Imagem enviada', use_column_width=True)
    
    # Pré-processamento (IGUAL AO FEITO NO COLAB)
    size = (150, 150) # Mesmo tamanho usado no treino
    image_resized = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    img_array = np.array(image_resized)
    img_array = img_array / 255.0 # Normalização igual ao treino
    img_array = np.expand_dims(img_array, axis=0) # Cria o lote de 1 imagem

    # Botão para classificar
    if st.button("Analisar Raio-X"):
        prediction = model.predict(img_array)
        score = prediction[0][0] # Pega o valor da probabilidade
        
        # Lógica: Se > 0.5 é Pneumonia (dependendo de como suas pastas estavam em ordem alfabética)
        # Geralmente: 0 = Normal, 1 = Pneumonia. Ajuste se estiver invertido.
        label = "PNEUMONIA DETECTADA" if score > 0.5 else "NORMAL"
        probabilidade = score if score > 0.5 else 1 - score
        
        # Mostrar Resultado
        if label == "PNEUMONIA DETECTADA":
            st.error(f"Resultado: {label}")
        else:
            st.success(f"Resultado: {label}")
            
        st.info(f"Confiança do Modelo: {probabilidade*100:.2f}%")
        
        # Salvar no Banco
        salvar_no_banco(file.name, label, f"{probabilidade*100:.2f}%")
        st.toast("Interação salva no banco de dados com sucesso!")

# --- ÁREA ADMINISTRATIVA (SÓ PARA VER SE O BANCO ESTÁ FUNCIONANDO) ---
with st.expander("Ver Histórico (Área Médica)"):
    conn = sqlite3.connect('historico_diagnosticos.db')
    import pandas as pd
    df = pd.read_sql_query("SELECT * FROM interacoes ORDER BY id DESC", conn)
    st.dataframe(df)
    conn.close()
