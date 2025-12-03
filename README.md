# 🫁 Sistema de Detecção de Pneumonia via Raio-X (IA)

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## 💻 Sobre o Projeto

Este projeto foi desenvolvido como parte da avaliação **AV2** do curso de Inteligência Artificial. O objetivo é aplicar conceitos de **Visão Computacional** e **Deep Learning** para auxiliar no diagnóstico médico.

A aplicação recebe uma imagem de Raio-X de tórax, processa através de uma Rede Neural Convolucional (CNN) e retorna o diagnóstico provável (**Normal** ou **Pneumonia**), registrando todas as interações em um banco de dados para histórico médico.

### 🎯 Funcionalidades

* **Upload de Imagens:** Suporte para arquivos JPG, JPEG e PNG.
* **Diagnóstico via IA:** Classificação automática utilizando modelo treinado com TensorFlow/Keras.
* **Histórico de Pacientes:** Gravação automática de cada exame (Data, Nome do Arquivo, Resultado e Confiança) em banco de dados **SQLite**.
* **Interface Web:** Dashboard interativo e amigável criado com **Streamlit**.

---

## 🛠 Tecnologias Utilizadas

* **Linguagem:** Python
* **Frontend:** Streamlit
* **Machine Learning:** TensorFlow & Keras
* **Processamento de Imagem:** Pillow (PIL) & Numpy
* **Banco de Dados:** SQLite 3
* **Dataset:** [Chest X-Ray Images (Pneumonia) - Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

---

## 📂 Estrutura do Projeto
/   ├── app.py # Código principal da aplicação Web 
    ├── modelo_pneumonia.h5 # Modelo de IA treinado (Rede Neural) 
    ├── historico_diagnosticos.db # Banco de dados (criado automaticamente) 
    ├── requirements.txt # Dependências do projeto 
    └── README.md

# Documentação

---

## 🚀 Como Executar o Projeto

### Opção 1: Rodando Localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)
    cd NOME-DO-REPO
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```

### Opção 2: Rodando no Google Colab (Recomendado se tiver problemas com TensorFlow local)

Devido ao peso da biblioteca TensorFlow, recomenda-se executar o projeto em nuvem:

1.  Faça upload do arquivo `app.py` e do modelo `modelo_pneumonia.h5` no Colab.
2.  Instale as dependências no notebook:
    ```python
    !pip install streamlit pyngrok tensorflow
    ```
3.  Utilize o **Ngrok** para criar o túnel de acesso externo.

---

## 📊 Resultados e Métricas

O modelo foi treinado utilizando uma arquitetura CNN (Convolutional Neural Network) e atingiu métricas competitivas em relação ao estado da arte:

* **Acurácia de Treino:** ~94%
* **Acurácia de Validação:** ~90%

O sistema registra logs de confiança para evitar falsos negativos, recomendando avaliação médica humana em casos de incerteza.

---

## 👨‍💻 Autores

* **Igor Gomes** - *Desenvolvimento e Treinamento do Modelo*
* [Nome dos outros integrantes do grupo]

---

**Aviso Legal:** Este software é um protótipo acadêmico e **não deve ser utilizado como única fonte para diagnósticos médicos reais**.