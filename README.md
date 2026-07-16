# Desafío: Fundamentos de Análisis Exploratorio y Estadística Descriptiva

Este repositorio contiene el desarrollo técnico, el código y las visualizaciones correspondientes al desafío de análisis exploratorio de datos (EDA) y caracterización estadística de un catálogo de distribución de videojuegos. 

El objetivo principal de este proyecto es transformar datos comerciales crudos en información útil y estructurada que sirva de apoyo directo para la toma de decisiones y el diseño de futuras estrategias de marketing.

---

## 📋 Estructura del Proyecto

El repositorio está organizado de la siguiente manera:

*   **`videojuegos.csv`**: Conjunto de datos de origen con 100 registros sobre ventas regionales (Norteamérica, Europa y Japón) y calificaciones de la crítica.
*   **`main.py`**: Script de procesamiento en Python que automatiza la carga de datos, el cálculo de las métricas estadísticas y la generación de las gráficas.
*   **Visualizaciones generadas:**
    *   `informe_histogramas.png`: Distribuciones de frecuencia para ventas en Norteamérica (`Ventas_NA`) y puntajes de la prensa (`Critica_Puntaje`).
    *   `informe_boxplots.png`: Comparativa del comportamiento y variabilidad de ventas en las tres regiones.
    *   `informe_generos.png`: Volumen de títulos clasificados por su género temático.
*   **`README.md`**: Guía de uso e información general del proyecto (este archivo).

---

## 🎯 Alcance del Informe vs. El Script Técnico

Es importante destacar la división de roles en este entregable:
*   **El Script de Python (`main.py`)**: Contiene todo el desarrollo técnico, las tareas de limpieza de datos, el manejo de valores nulos, el procesamiento matemático de las variables y el código de diseño de las visualizaciones.
*   **El Informe Escrito**: Su alcance se centra exclusivamente en la **interpretación analítica y estratégica** de los resultados[cite: 2]. El informe traduce los números y las gráficas en conclusiones y recomendaciones claras para el negocio, asumiendo que los aspectos técnicos y de programación ya han sido resueltos y validados mediante el código de este repositorio.

---

## 🛠️ Requisitos e Instalación

Para ejecutar el script técnico de manera local y replicar los resultados, asegúrate de contar con Python (versión 3.8 o superior) y las siguientes librerías de análisis de datos:

1. **Clonar este repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/desafio-descriptiva-videojuegos.git](https://github.com/tu-usuario/desafio-descriptiva-videojuegos.git)
   cd desafio-descriptiva-videojuegos
