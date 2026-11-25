import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Habitos de Estudio y GPA", layout="wide")


datos = pd.read_csv("student_lifestyle_dataset.csv")

columnas_usar = ["Student_ID", "Study_Hours_Per_Day", "Sleep_Hours_Per_Day", "Stress_Level", "GPA"]
datos_usar = datos[columnas_usar]



def clasificar_estudio(horas):
    
    if horas < 6:
        return "Menos de 6 horas"
    elif horas < 8:
        return "Entre 6 y 8 horas"
    else:
        return "8 horas o mas"


def clasificar_sueño(horas):
   
    if horas < 6:
        return "Menos de 6 horas"
    elif horas <= 8:
        return "Entre 6 y 8 horas"
    else:
        return "Mas de 8 horas"


def porcentaje(notas, minimo):
  
    if len(notas) == 0:
        return 0
    contador = 0
    for nota in notas:
        if nota >= minimo:
            contador = contador + 1
    return round(contador / len(notas) * 100, 1)


def quitar_bordes():
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)



st.sidebar.header("Filtros")
st.sidebar.write("Cambia los filtros y mira como cambian los resultados.")

niveles_elegidos = st.sidebar.multiselect("Nivel de estres", ["Bajo", "Moderado", "Alto"],
                                          default=["Bajo", "Moderado", "Alto"])
sueño_maximo = st.sidebar.slider("Horas de sueño al dia (desde 5 hasta...)", 5.0, 10.0, 10.0, step=0.5)
meta = st.sidebar.select_slider("¿Que consideras un buen promedio?", options=[3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6,3.7,3.8, 3.9, 4.0], value=3.5)

nombre_a_nivel = {"Bajo": "Low", "Moderado": "Moderate", "Alto": "High"}
niveles = []
for nombre in niveles_elegidos:
    niveles.append(nombre_a_nivel[nombre])

filtro = datos_usar[datos_usar["Stress_Level"].isin(niveles)]
filtro = filtro[(filtro["Sleep_Hours_Per_Day"] >= 5.0) & (filtro["Sleep_Hours_Per_Day"] <= sueño_maximo)]



st.title("Panel de Habitos de Estudio y Promedio (GPA)")
st.write("Analisis de 2000 estudiantes: cuanto estudian, cuanto duermen, su nivel de estres y su promedio.")
st.info(f"Pregunta guia: ¿Cuantas horas de estudio al dia se asocian con un mejor promedio, y como influyen el sueño y el estres en ese resultado?")

if len(filtro) > 0:

    horas_estudio = filtro["Study_Hours_Per_Day"].to_numpy()
    horas_sueño = filtro["Sleep_Hours_Per_Day"].to_numpy()
    gpa = filtro["GPA"].to_numpy()


    st.subheader("Estadisticas clave")

    col1, col2, col3, col4, col5 = st.columns(5, border=True)

    col1.metric("Estudiantes", len(gpa))
    col2.metric("GPA promedio", round(np.mean(gpa), 2))
    col3.metric("Desviacion estandar", round(np.std(gpa), 2))
    col4.metric("Estudio promedio", f"{round(np.mean(horas_estudio), 1)} h")
    col5.metric(f"Con GPA de {meta} o mas", f"{porcentaje(gpa, meta)}%")


    st.subheader("¿Desde cuantas horas de estudio se llega a un buen promedio?")

    horas = np.arange(5, 10.5, 0.5)
    porcentajes_aceptable = []
    porcentajes_bueno = []

    for h in horas:
        notas = []
        for i in range(len(gpa)):
            if horas_estudio[i] >= h and horas_estudio[i] < h + 0.5:
                notas.append(gpa[i])
        porcentajes_aceptable.append(porcentaje(notas, 3.0))
        porcentajes_bueno.append(porcentaje(notas, meta))

    ancho = 0.2

    figura = plt.figure(figsize=(12, 4))
    plt.bar(horas - ancho / 2, porcentajes_aceptable, ancho, color="violet", label="Aceptable (3.0)")
    plt.bar(horas + ancho / 2, porcentajes_bueno, ancho, color="purple", label=f"Bueno ({meta})")

    plt.xticks(horas)
    plt.xlabel("Horas de estudio al dia")
    plt.ylabel("% de estudiantes")
    plt.legend(frameon=False)
    quitar_bordes()
    st.pyplot(figura)

    encontrado = False
    for i in range(len(horas)):
        if porcentajes_bueno[i] >= 25:
            st.success(f"Desde {horas[i]} horas de estudio al dia, 1 de cada 4 estudiantes tiene un promedio de {meta} o mas.")
            encontrado = True
            break

    if encontrado == False:
        st.warning(f"Con estos filtros ningun grupo llega a que 1 de cada 4 estudiantes tenga promedio de {meta} o mas.")

    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribucion del GPA")

        promedio = np.mean(gpa)

        figura = plt.figure(figsize=(6, 4))
        plt.hist(gpa, bins=20, color="violet", edgecolor="white")
        plt.ylim(0, plt.ylim()[1] * 1.3)

        plt.axvline(promedio, color="purple", linestyle="--", label=f"Promedio = {promedio:.2f}")
        plt.axvline(meta, color="black", linestyle=":", label=f"Buen promedio = {meta}")

        plt.xlabel("GPA")
        plt.ylabel("Cantidad de estudiantes")
        plt.legend(frameon=False, loc="upper left")
        quitar_bordes()
        st.pyplot(figura)

    with col2:
        st.subheader("GPA segun horas de sueño")

        notas_por_sueño = {
            "Menos de 6 horas": [],
            "Entre 6 y 8 horas": [],
            "Mas de 8 horas": []
        }

        for i in range(len(gpa)):
            grupo = clasificar_sueño(horas_sueño[i])
            notas_por_sueño[grupo].append(gpa[i])

        promedios_sueño = []
        for grupo in notas_por_sueño:
            notas = notas_por_sueño[grupo]
            if len(notas) > 0:
                promedios_sueño.append(np.mean(notas))
            else:
                promedios_sueño.append(0)

        figura = plt.figure(figsize=(6, 4))
        plt.bar(list(notas_por_sueño.keys()), promedios_sueño, color=["pink", "violet", "purple"])

        plt.axhline(3.0, color="gray", linestyle="--", label="Aceptable = 3.0")
        plt.axhline(meta, color="black", linestyle=":", label=f"Bueno = {meta}")

        plt.ylim(2.5, 4.0)
        plt.ylabel("GPA promedio")
        plt.legend(frameon=False)
        quitar_bordes()
        st.pyplot(figura)

   
    st.subheader("Estadisticas al detalle por horas de estudio")

    notas_por_grupo = {
        "Menos de 6 horas": [],
        "Entre 6 y 8 horas": [],
        "8 horas o mas": []
    }

    for i in range(len(gpa)):
        grupo = clasificar_estudio(horas_estudio[i])
        notas_por_grupo[grupo].append(gpa[i])

    tabla = []
    for grupo in notas_por_grupo:
        notas = notas_por_grupo[grupo]
        if len(notas) > 0:
            tabla.append({
                "Horas de estudio": grupo,
                "Estudiantes": len(notas),
                "GPA promedio": round(np.mean(notas), 2),
                "% Aceptable (3.0)": porcentaje(notas, 3.0),
                f"% Bueno ({meta})": porcentaje(notas, meta)
            })

    st.dataframe(pd.DataFrame(tabla), hide_index=True, width="stretch")

    #Conclusion
    st.subheader("Conclusion")
    st.write("Lo que mas influye en el GPA son las horas de estudio: desde 8.5 horas al dia el 90% de los estudiantes "
             "tiene promedio aceptable y desde 9 horas 1 de cada 4 llega a un buen promedio. "
             "Las horas de sueño casi no cambian el promedio.")

else:
    st.warning("No hay estudiantes con esos filtros, por favor cambia las opciones de la barra lateral.")