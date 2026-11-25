# Dashboard de habitos de estudio  y promediio (GPA) con streamlit

# Descripción

Esta aplicacion wed interactiva muestra el analisi de 2000 estudiantes, cuantas horas estudian, cuantas horas duermen, su nivel de estres y su promedi. Con los fitros de la barra lateral se puede ver como los resultados  cambian.

Es el proyecto integrados  de primer semestre de Ingenieria de Datos e IA de la Universidas Santo Tomas, de las materias introduccion a la ingenieria de datos e ia y logica computacional.

**Integrantes**: Maria Jose Pinto Peréz y Laura Sofia Vargas Lesmes

**Enlace de la app:**

# Pregunta guia

¿Cuántas horas de estudio al día se asocia con un mejor promedio, y cómo influyen el sueño y el estrés en ese resultado?

# Dataset 

Para este proyecto usamos el dataset Student Lifestyle Dataset de kaggle: https://www.kaggle.com/datasets/steve1215rogg/student-lifestyle-dataset
Tiene 2000 estudiantes y 8 varibles, pero para la aplicacion usams solo 5: Student_ID, Study_Hours_Per_Day, Sleep_Hours_Per_Day, Stress_Level GPA que es el proemdio academico de 0 a 4.

# Archivos del proyecto

app,py
student_lifestyle_dataset.csv
requirements.txt
Proyecto.ipynb

# Funcionalidades 

**Widgets:**

*Nivel de estres (multiselect):* Bajo, Moderado y Alto
*Horas de sueño al dia (slider):* Rango de 5 a 10 horas
*¿Que considera un bbuen promedio?:* (select_slider): de 3.0 a 4.0

**Lo que muestra la aplicación**

La aplicación mustra las esadisticas clave con el numero de estudiantes, el  GPA promedio, la desviacion estandar, las horas de estudio promedio y el porcentaje de estudiantes que llegan a un buen promedio. Tambien tiene una grafica de barras con el porcentaje de estudiantes que tienen un promedio aceptable (3.0) y bueno (3.5) segun las horas de estudio estudio. 
Ademas incluye un historigrama con la distribución del GPA, una grafica de barras con el GPA pomedio segun las goras de sueño  una tabla con estadisticas por grupos de horas de estudio y al final muestra una conclusion.

**En el codigo usamos:**

*Funiones:* clasificar_estudio, clasificar_sueño, pocentajes.
Condiciones como if, elif, else y ciclos for con break.
Listas y diccionarios para agrupar.

# Resultados 
Desde 8.5 horas de estudio al dia el 90% de los estudiantes tienen un promedio aceptable, dessde las 9 horas, 1 de cada 4 estudiantes tienen un buen promedio 3.5. Las horas de sueño casi no cambia el promedio y  los estudiantes con estres alto tiene mejor promedio, pero es porque estudian más.

# Tecnologias Utilizadas
**Streamlit**
**Pandas**
**Numpy**
**Matplotlib**
**Python**

# Instalación

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Ejecución

streamlit run app.py