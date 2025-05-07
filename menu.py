"""
Aplicación de gestión de recetas con interfaz gráfica y sincronización en la nube.

Este módulo permite al usuario:
- Añadir, ver y eliminar recetas locales.
- Generar un menú semanal aleatorio.
- Sincronizar recetas con una API en la nube.
- Usar una interfaz visual interactiva con Gradio.
"""

import os
import json
import random
import requests
import gradio as gr
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Archivos locales
ARCHIVO_RECETAS = "recetas.json"

# Configuración de la API
API_URL = os.getenv("API_URL")
HEADERS_API = {
    "Content-Type": "application/json",
    "X-Master-Key": os.getenv("X_MASTER_KEY"),
    "X-Access-Key": os.getenv("X_ACCESS_KEY"),
    "X-Bin-Private": os.getenv("BIN_PRIVATE", "true"),
    "X-Bin-Name": os.getenv("BIN_NAME", "defaultbin")
}


def leer_json(ruta):
 
    """
    Lee un archivo JSON y devuelve su contenido como diccionario.

    Args:
        ruta (str): Ruta del archivo JSON.

    Returns:
        dict: Contenido del archivo o diccionario vacío si hay error.
    """

    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
        except json.JSONDecodeError:
            return {}
    return {}


def escribir_json(ruta, datos):

    """
    Escribe un diccionario en un archivo JSON.

    Args:
        ruta (str): Ruta del archivo.
        datos (dict): Diccionario con datos a guardar.
    """

    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)



def introducir_receta_gradio(nombre, categoria, ingredientes, instrucciones):

    """
    Añade una receta nueva a la base local.

    Args:
        nombre (str): Nombre de la receta.
        categoria (str): Categoría (desayuno, almuerzo, cena).
        ingredientes (str): Ingredientes separados por coma.
        instrucciones (str): Instrucciones separadas por coma.

    Returns:
        str: Mensaje de confirmación o error.
    """

    recetas = leer_json(ARCHIVO_RECETAS)
    categorias_validas = ["desayuno", "almuerzo", "cena"]

    if categoria not in categorias_validas:
        return "Categoría inválida. Usa: desayuno, almuerzo o cena."

    receta = {
        "ingredientes": [i.strip() for i in ingredientes.split(",")],
        "instrucciones": [i.strip() for i in instrucciones.split(",")]
    }

    if categoria not in recetas:
        recetas[categoria] = {}

    recetas[categoria][nombre] = receta
    escribir_json(ARCHIVO_RECETAS, recetas)
    return f"'{nombre}' añadida con éxito a la categoría '{categoria}'."


def ver_recetas_gradio():

    """
    Devuelve una lista de recetas guardadas.

    Returns:
        str: Lista de recetas por categoría.
    """

    recetas = leer_json(ARCHIVO_RECETAS)
    if not recetas:
        return "No hay recetas guardadas."
    
    salida = ""
    for categoria, items in recetas.items():
        salida += f"\n{categoria.capitalize()}:\n"
        for nombre in items:
            salida += f" - {nombre}\n"
    return salida


def generar_menu_gradio():

    """
    Genera un menú semanal aleatorio con recetas.

    Returns:
        str: Menú con desayuno, almuerzo y cena por día.
    """

    recetas = leer_json(ARCHIVO_RECETAS)
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    menu = ""

    for dia in dias:
        menu += f"\n{dia}:\n"
        for cat in ["desayuno", "almuerzo", "cena"]:
            disponibles = recetas.get(cat, {})
            if disponibles:
                # Verificamos que haya recetas para elegir
                nombre = random.choice(list(disponibles.keys()))
                menu += f"  {cat.capitalize()}: {nombre}\n"
            else:
                menu += f"  {cat.capitalize()}: (no disponible)\n"
    return menu


def guardar_en_nube_gradio():
    
    """
    Guarda las recetas locales en la nube usando una API.

    Returns:
        str: Resultado del intento de sincronización.
    """

    recetas = leer_json(ARCHIVO_RECETAS)
    try:
        response = requests.put(API_URL, json=recetas, headers=HEADERS_API)
        response.raise_for_status()
        return "Recetas guardadas en la nube."
    except requests.RequestException as e:
        return f"Error al guardar en la nube: {e}"


def cargar_desde_nube_gradio():

    """
    Carga recetas desde la nube y las guarda localmente.

    Returns:
        str: Resultado de la operación.
    """

    try:
        response = requests.get(API_URL, headers=HEADERS_API)
        response.raise_for_status()
        nube_recetas = response.json().get("record", {})
    except requests.RequestException as e:
        return f"Error al cargar desde la nube: {e}"
    
    # Guardamos las recetas sincronizadas en el archivo local
    escribir_json(ARCHIVO_RECETAS, nube_recetas)
    return "Recetas cargadas desde la nube."


def eliminar_recetas_gradio(nombres):

    """
    Elimina una o varias recetas por nombre.

    Args:
        nombres (str): Nombres separados por coma.

    Returns:
        str: Resultado indicando recetas eliminadas o no encontradas.
    """

    # Limpiar y dividir la entrada
    nombres = [nombre.strip() for nombre in nombres.split(",")]

    recetas = leer_json(ARCHIVO_RECETAS)
    if not recetas:
        return "No hay recetas para eliminar."
    
    nombres_eliminados = []
    nombres_no_encontrados = []
    
    for nombre in nombres:
        receta_eliminada = False

        # Buscar en cada categoría
        for categoria, recetas_categoria in recetas.items():
            if nombre in recetas_categoria:
                del recetas_categoria[nombre]  # Eliminar receta
                nombres_eliminados.append(nombre)
                receta_eliminada = True
                break  # Sale del bucle cuando se elimina la receta

        if not receta_eliminada:
            nombres_no_encontrados.append(nombre)
    
    # Guardar los cambios
    escribir_json(ARCHIVO_RECETAS, recetas)
    
    # Mensaje de resultado
    if nombres_eliminados:
        resultado = f"Recetas eliminadas: {', '.join(nombres_eliminados)}."
    else:
        resultado = "No se eliminaron recetas."
    
    if nombres_no_encontrados:
        resultado += f"\nRecetas no encontradas: {', '.join(nombres_no_encontrados)}."

    return resultado


def iniciar_gradio():

    """
    Inicia la interfaz gráfica de usuario con pestañas para cada función.
    """

    interfaz1 = gr.Interface(
        fn=introducir_receta_gradio,
        inputs=[
            gr.Textbox(label="Nombre de la receta"),
            gr.Radio(choices=["desayuno", "almuerzo", "cena"], label="Categoría"),
            gr.Textbox(label="Ingredientes (separados por coma)"),
            gr.Textbox(label="Instrucciones (separadas por coma)")
        ],
        outputs="text",
        title="Añadir Receta"
    )

    interfaz2 = gr.Interface(
        fn=ver_recetas_gradio,
        inputs=[],
        outputs="text",
        title="Ver Recetas Guardadas"
    )

    interfaz3 = gr.Interface(
        fn=generar_menu_gradio,
        inputs=[],
        outputs="text",
        title="Generar Menú Semanal"
    )

    interfaz4 = gr.Interface(
        fn=guardar_en_nube_gradio,
        inputs=[],
        outputs="text",
        title="Guardar Recetas en la Nube"
    )

    interfaz5 = gr.Interface(
        fn=cargar_desde_nube_gradio,
        inputs=[],
        outputs="text",
        title="Cargar Recetas desde la Nube"
    )

    interfaz6 = gr.Interface(
        fn=eliminar_recetas_gradio,
        inputs=gr.Textbox(label="Nombres de las recetas a eliminar (separadas por coma)"),
        outputs="text",
        title="Eliminar Recetas"
    )

    # Crear una interfaz con pestañas
    gr.TabbedInterface(
        [interfaz1, interfaz2, interfaz3, interfaz4, interfaz5, interfaz6], 
        ["Añadir Receta", "Ver Recetas", "Menú Semanal", "Guardar en Nube", "Cargar de Nube", "Eliminar Recetas"]
    ).launch()

# Iniciar la aplicación
if __name__ == "__main__":
    iniciar_gradio()
