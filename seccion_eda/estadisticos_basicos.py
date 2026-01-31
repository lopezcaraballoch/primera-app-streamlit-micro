import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.markdown("Lorem ipsum")

st.markdown("## Datos Crudos del dataset")
df = pd.read_csv("bike_dataset_day.csv")

st.markdown("## Datos sobre el dataset")
st.dataframe(df.head(100))

st.dataframe(df.describe().T)

st.markdown("## Estadísticos básicos")

st.dataframe(df[['dteday','temp','windspeed','cnt']].describe().T[['count','mean','std']])

st.markdown("## Distribución de las variables")

cols = st.columns(3)

with cols[0]:
    fig, ax = plt.subplots()
    sns.histplot(df['temp'],kde=True)
    plt.title("Distribución Temp.")
    st.pyplot(fig)

with cols[1]:
    fig, ax = plt.subplots()
    sns.histplot(df['hum'],kde=True)
    plt.title("Distribución Hum.")
    st.pyplot(fig)

with cols[2]:
    fig, ax = plt.subplots()
    sns.histplot(df['windspeed'],kde=True)
    plt.title("Distribución Vel. Viento")
    st.pyplot(fig)

st.markdown("---")

cols_target, = st.columns(1)
with cols_target:
    fig, ax = plt.subplots()
    sns.histplot(df['cnt'],kde=True)
    plt.title("Distribución CNT")
    st.pyplot(fig)


st.markdown("## Matriz de correlación")
cols_interes= ['temp','hum','windspeed','casual','cnt']
matriz_correlacion = df[cols_interes].corr()


fig0 = plt.figure()
sns.heatmap(matriz_correlacion,annot=True)
st.pyplot(fig0)


col, = st.columns(1)
with col:
    fig = plt.figure()
    sns.heatmap(matriz_correlacion)
    st.pyplot(fig)
