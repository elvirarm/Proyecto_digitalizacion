from datetime import datetime, timedelta
import os
import json
import requests
import random

archivo_json = "recetas.json"
calendario_json = "calendario.json"

def leer_json(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return data if isinstance(data, (list, dict)) else {}
            except json.JSONDecodeError:
                return {}
    return {}

def escribir_json(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)

def introducir_receta():
    recetas = leer_json(archivo_json)
    
    if not isinstance(recetas, dict):
        print("Recetas vacío, regenerando json...")
        recetas = {}

    nombre = input("Introduce el nombre de la nueva receta: ")
    ingredientes = input(f"Introduce los ingredientes de {nombre} separados por ',': ").split(",")
    instrucciones = input(f"Introduce las instrucciones de {nombre} separadas por ',': ").split(",")

    nueva_receta = {nombre: {"ingredientes": ingredientes, "instrucciones": instrucciones}}
    recetas = recetas | nueva_receta
    escribir_json(archivo_json, recetas)
    print(f"{nombre} añadida con éxito.")

def ver_recetas_disponibles():
    recetas = leer_json(archivo_json)
    if recetas:
        claves_recetas = list(recetas)
        for x in range(len(recetas)):
            print(f"{x + 1}. {claves_recetas[x]}")
    else:
        print("No hay recetas disponibles.")


def recetas_random(recetas):
    recetas_generadas = []
    for x in range(7):
        array_nombre_recetas = list(recetas)
        clave_receta_actual = array_nombre_recetas[random.randint(0, len(array_nombre_recetas)-1)]
        # print("Añadiendo receta: "+clave_receta_actual)
        recetas_generadas += {clave_receta_actual: recetas.get(clave_receta_actual)}
    return recetas_generadas


def generar_menu():
    recetas = leer_json(archivo_json)
    menu = recetas_random(recetas)
    return menu


def mostrar_menu_semanal():
    semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    menu = generar_menu()
    
    for x in range(7):
        dia_actual = semana[x]
        recetas_dia_actual = menu[x]

        print("El " + dia_actual + " hay: " + recetas_dia_actual)


def guardar_json():
    recetas = leer_json(archivo_json)

    headers = {
        "Content-Type":"application/json",
        "X-Master-Key":"$2a$10$YPbdwuG2GnwUMcfvEDi9A.pCni9x8VOsAQhhOAU4L1w.Lex/KLnRK",
        "X-Access-Key":"$2a$10$h4AJh0OW/9KMuLXKOU/.Uui1mqXi2w58umcWVAXOdzdXRg0lHmk3G",
        "X-Bin-Private":"true",
        "X-Bin-Name":"testingbin"
    }

    url = "https://api.jsonbin.io/v3/b/67d217508a456b796674a341"
    response = requests.put(url, json=recetas, headers=headers)
    # print(response)





def cargar_json():
    recetas = leer_json(archivo_json)

    headers = {
        "Content-Type":"application/json",
        "X-Master-Key":"$2a$10$YPbdwuG2GnwUMcfvEDi9A.pCni9x8VOsAQhhOAU4L1w.Lex/KLnRK",
        "X-Access-Key":"$2a$10$h4AJh0OW/9KMuLXKOU/.Uui1mqXi2w58umcWVAXOdzdXRg0lHmk3G",
        "X-Bin-Private":"true",
        "X-Bin-Name":"testingbin"
    }

    url = "https://api.jsonbin.io/v3/b/67d217508a456b796674a341"
    response = json.loads(requests.get(url, headers=headers).content)["record"]
    for nombreReceta, cosasReceta in recetas.items():
        if nombreReceta not in response:
            response[nombreReceta] = cosasReceta
        else:
            print("Receta " + nombreReceta + " duplicada, prevalece la recuperada de la API")
    # print(response)
    escribir_json(archivo_json, response)
    return response


def mostrar_menu():
    print("-- MENÚ --")
    print("1 -> Introducir receta nueva")
    print("2 -> Ver recetas disponibles")
    print("3 -> Mostrar menú semanal")
    print("4 -> Subir a la nube las recetas")
    print("5 -> Cargar recetas a la nube")
    print("6 -> Eliminar receta del recetario")
    print("7 -> Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            introducir_receta()
        elif opcion == "2":
            ver_recetas_disponibles()
        elif opcion == "3":
            mostrar_menu_semanal()
    
        elif opcion == "4":
            guardar_json()

        elif opcion == "5":
            cargar_json()

        elif opcion == "6":
            recetas = input("¿Que recetas quieres eliminar? (separado por ',')").split(',')
            opcion2 = input("¿Deseas eliminar la receta también de la nube? (s/n)")
            if(opcion2 == "s"):
                eliminar_receta(True, recetas)
            else:
                eliminar_receta(False, recetas)


        elif opcion == "7":
    
            print("Saliendo...")
            break
            
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    
def eliminar_receta(eliminarNube, recetasBorrar):
    recetas = None
    if eliminarNube:
        recetas = cargar_json()
    else:
        recetas = leer_json(archivo_json)
    
    for nombreReceta in recetasBorrar:
        print("Borrando "+nombreReceta)
        recetas.pop(nombreReceta)

    print(recetas)
    escribir_json(archivo_json, recetas)
    if eliminarNube:
        guardar_json()

if __name__ == "__main__":
    main()
