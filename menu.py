"""
Recipe management application with graphical interface and cloud synchronization.

This module allows the user to:
- Add, view, and delete local recipes.
- Generate a random weekly menu.
- Sync recipes to a cloud API.
- Use an interactive visual interface with Gradio.
"""

import os
import json
import random
import requests
import gradio as gr
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Local file for storing recipes
ARCHIVO_RECETAS = "recetas.json"

# API configuration
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
    Reads a JSON file and returns its contents as a dictionary.

    Args:
        ruta (str): Path to the JSON file.

    Returns:
        dict: File contents or an empty dictionary in case of error.
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
    Writes a dictionary to a JSON file.

    Args:
        ruta (str): File path.
        datos (dict): Dictionary to be saved.
    """

    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)



def introducir_receta_gradio(nombre, categoria, ingredientes, instrucciones):

    """
    Adds a new recipe to the local storage.

    Args:
        nombre (str): Recipe name.
        categoria (str): Category (desayuno, almuerzo, cena).
        ingredientes (str): Comma-separated ingredients.
        instrucciones (str): Comma-separated instructions.

    Returns:
        str: Confirmation or error message.
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
    Returns a list of saved recipes.

    Returns:
        str: Recipes organized by category.
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
    Generates a random weekly menu using available recipes.

    Returns:
        str: Menu with breakfast, lunch, and dinner for each day.
    """

    recetas = leer_json(ARCHIVO_RECETAS)
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    menu = ""

    for dia in dias:
        menu += f"\n{dia}:\n"
        for cat in ["desayuno", "almuerzo", "cena"]:
            disponibles = recetas.get(cat, {})
            if disponibles:
                # Make sure there are recipes to choose from
                nombre = random.choice(list(disponibles.keys()))
                menu += f"  {cat.capitalize()}: {nombre}\n"
            else:
                menu += f"  {cat.capitalize()}: (no disponible)\n"
    return menu


def guardar_en_nube_gradio():
    
    """
    Saves local recipes to the cloud via API.

    Returns:
        str: Result of the synchronization.
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
    Loads recipes from the cloud and saves them locally.

    Returns:
        str: Result of the operation.
    """

    try:
        response = requests.get(API_URL, headers=HEADERS_API)
        response.raise_for_status()
        nube_recetas = response.json().get("record", {})
    except requests.RequestException as e:
        return f"Error al cargar desde la nube: {e}"
    
    # Save the synchronized recipes to the local file
    escribir_json(ARCHIVO_RECETAS, nube_recetas)
    return "Recetas cargadas desde la nube."


def eliminar_recetas_gradio(nombres):

    """
    Deletes one or more recipes by name.

    Args:
        nombres (str): Comma-separated recipe names.

    Returns:
        str: Result indicating which recipes were deleted or not found.
    """

    # Clean and split the input
    nombres = [nombre.strip() for nombre in nombres.split(",")]

    recetas = leer_json(ARCHIVO_RECETAS)
    if not recetas:
        return "No hay recetas para eliminar."
    
    nombres_eliminados = []
    nombres_no_encontrados = []
    
    for nombre in nombres:
        receta_eliminada = False

        # Search within each category
        for categoria, recetas_categoria in recetas.items():
            if nombre in recetas_categoria:
                del recetas_categoria[nombre]  # Delete recipe
                nombres_eliminados.append(nombre)
                receta_eliminada = True
                break  # Exit the loop once the recipe is deleted

        if not receta_eliminada:
            nombres_no_encontrados.append(nombre)
    
    # Save the changes
    escribir_json(ARCHIVO_RECETAS, recetas)
    
    # Result message
    if nombres_eliminados:
        resultado = f"Recetas eliminadas: {', '.join(nombres_eliminados)}."
    else:
        resultado = "No se eliminaron recetas."
    
    if nombres_no_encontrados:
        resultado += f"\nRecetas no encontradas: {', '.join(nombres_no_encontrados)}."

    return resultado


def iniciar_gradio():

    """
    Launches the graphical interface with tabs for each functionality.
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

    # Create an interface with tabs
    gr.TabbedInterface(
        [interfaz1, interfaz2, interfaz3, interfaz4, interfaz5, interfaz6], 
        ["Añadir Receta", "Ver Recetas", "Menú Semanal", "Guardar en Nube", "Cargar de Nube", "Eliminar Recetas"]
    ).launch()

# Start the app
if __name__ == "__main__":
    iniciar_gradio()
