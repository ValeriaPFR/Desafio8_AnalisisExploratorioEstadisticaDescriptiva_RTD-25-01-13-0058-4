"""
Desafío: Fundamentos de análisis exploratorio y estadística descriptiva.
Estudiante: Valeria Fariña
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def cargar_datos(ruta_archivo="videojuegos.csv"):
    """Realiza el Requerimiento 1: Carga y verificación del dataset."""
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(
            f"No se encontró el archivo '{ruta_archivo}'. "
            f"Por favor, asegúrate de que esté en el mismo directorio."
        )

    df = pd.read_csv(ruta_archivo)
    print("=================================================================")
    print("          REQUERIMIENTO 1: CARGA DEL CONJUNTO DE DATOS           ")
    print("=================================================================")
    print(f"Dataset '{ruta_archivo}' cargado exitosamente.\n")
    return df


def analisis_exploratorio_inicial(df):
    """Realiza el Requerimiento 2: Inspección básica e IDA."""
    print("=================================================================")
    print("            REQUERIMIENTO 2: ANÁLISIS EXPLORATORIO               ")
    print("=================================================================")

    # 1. Primeras y últimas 5 filas
    print("[1] Primeras 5 filas del DataFrame:")
    print(df.head(), "\n")

    print("[2] Últimas 5 filas del DataFrame:")
    print(df.tail(), "\n")

    # 2. Información general y nulos
    print("[3] Información estructural del DataFrame (.info()):")
    df.info()
    print()

    # 3. Dimensiones del DataFrame
    filas, columnas = df.shape
    print(f"[4] Dimensiones del DataFrame:")
    print(f"    - Número de registros (filas): {filas}")
    print(f"    - Número de variables (columnas): {columnas}\n")


def analisis_descriptivo_univariado(df):
    """Realiza el Requerimiento 3: Análisis de tendencias, dispersión y visualización."""
    print("=================================================================")
    print("          REQUERIMIENTO 3: ANÁLISIS DESCRIPTIVO Y UNIVARIADO     ")
    print("=================================================================")

    # --- VARIABLES NUMÉRICAS ---
    columnas_num = ["Ventas_NA", "Ventas_EU", "Ventas_JP", "Critica_Puntaje"]

    # Cálculo y descripción de medidas
    print("[1] Estadísticas descriptivas de las variables numéricas:")
    resumen = df[columnas_num].describe().T

    # Añadir manualmente la mediana y el rango para dar cumplimiento estricto
    resumen["median"] = df[columnas_num].median()
    resumen["rango"] = resumen["max"] - resumen["min"]

    # Reorganizar y renombrar columnas para una visualización limpia
    resumen_final = resumen[
        ["mean", "median", "std", "rango", "min", "max"]
    ].rename(
        columns={
            "mean": "Media",
            "median": "Mediana",
            "std": "Desv. Estándar",
            "rango": "Rango",
            "min": "Mínimo",
            "max": "Máximo",
        }
    )
    print(resumen_final.round(2), "\n")

    # --- VARIABLES CATEGÓRICAS ---
    print("[2] Tablas de frecuencia para variables categóricas:")
    print("\n--- Frecuencia por Plataforma ---")
    print(df["Plataforma"].value_counts())

    print("\n--- Frecuencia por Género ---")
    print(df["Genero"].value_counts())
    print()


def generar_visualizaciones(df):
    """Genera y guarda los gráficos requeridos en el análisis."""
    print("Generando visualizaciones y guardando imágenes...")

    # Configuración estética general
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({"font.size": 11, "figure.titlesize": 14})

    # 1. Histogramas: Ventas_NA y Critica_Puntaje
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    sns.histplot(
        df["Ventas_NA"],
        kde=True,
        ax=axes[0],
        color="skyblue",
        edgecolor="white",
    )
    axes[0].set_title("Distribución de Ventas en Norteamérica (Ventas_NA)")
    axes[0].set_xlabel("Ventas (Millones de USD)")
    axes[0].set_ylabel("Frecuencia (Cantidad de Juegos)")

    # Eliminamos nulos en Critica_Puntaje para graficar correctamente
    sns.histplot(
        df["Critica_Puntaje"].dropna(),
        kde=True,
        ax=axes[1],
        color="salmon",
        edgecolor="white",
    )
    axes[1].set_title("Distribución de Puntajes de la Crítica")
    axes[1].set_xlabel("Puntaje")
    axes[1].set_ylabel("Frecuencia (Cantidad de Juegos)")

    plt.tight_layout()
    plt.savefig("histograms.png", dpi=300)
    plt.close()
    print("  -> Guardado: 'histograms.png' (Histogramas de Ventas NA y Puntajes)")

    # 2. Boxplots de ventas por región (detección de atípicos)
    plt.figure(figsize=(10, 6))
    columnas_ventas = ["Ventas_NA", "Ventas_EU", "Ventas_JP"]

    sns.boxplot(data=df[columnas_ventas], palette="Set2")
    plt.title("Diagramas de Caja (Boxplots) de Ventas por Región")
    plt.ylabel("Ventas (Millones de USD)")
    plt.xlabel("Regiones de Distribución")

    plt.tight_layout()
    plt.savefig("boxplots.png", dpi=300)
    plt.close()
    print("  -> Guardado: 'boxplots.png' (Boxplots de Ventas por Región)")

    # 3. Gráfico de barras para la cantidad de juegos por Género
    plt.figure(figsize=(8, 5))
    orden_generos = df["Genero"].value_counts().index

    sns.countplot(
        data=df, x="Genero", order=orden_generos, palette="viridis", hue="Genero"
    )
    plt.title("Cantidad de Videojuegos por Género")
    plt.xlabel("Género")
    plt.ylabel("Cantidad de Juegos")

    plt.tight_layout()
    plt.savefig("genero_bars.png", dpi=300)
    plt.close()
    print("  -> Guardado: 'genero_bars.png' (Gráfico de barras por Género)\n")


def main():
    """Flujo principal de ejecución."""
    try:
        # 1. Requerimiento 1
        df = cargar_datos("videojuegos.csv")

        # 2. Requerimiento 2
        analisis_exploratorio_inicial(df)

        # 3. Requerimiento 3
        analisis_descriptivo_univariado(df)
        generar_visualizaciones(df)

        print("=================================================================")
        print("          ¡PROCESAMIENTO COMPLETADO EXITOSAMENTE!                ")
        print("=================================================================")

    except Exception as e:
        print(f"\n[ERROR] Ocurrió un fallo durante la ejecución: {e}") #En el caso de que haya algún error, se mostrará un mensaje de error en la consola.


if __name__ == "__main__":
    main()