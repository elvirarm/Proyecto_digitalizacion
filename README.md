# Proyecto_digitalizacion

# Recetario Semanal #

Este proyecto es una aplicación en Python que permite gestionar un recetario personalizado. Con esta herramienta, puedes añadir recetas por categorías (desayuno, almuerzo y cena), ver las recetas disponibles, generar un menú semanal aleatorio, y sincronizar tus recetas con la nube utilizando JSONBin.io.

# Motivación #

Alimentarnos no debería de ser un quebradero de cabeza, sin embargo en este mundo tan ajetreado, a veces lo es... bien porque vas a hacer una receta y te falta algún ingrediente por la falta de planificación o simplemente no se te ocurre qué comer.
Por eso, surge este proyecto, para ayudarte a hacer tu vida un poco más fácil ofreciéndote lo siguiente:

- Registrar y clasificar tus recetas por tipo de comida (desayuno, almuerzo, cena).
- Generar un menú semanal aleatorio en segundos.
- Guardar y sincronizar tus recetas en la nube, para no depender de un solo dispositivo.
- Mantener todo en un formato sencillo (`.json`) que se pueda editar fácilmente.

# Instrucciones de despliegue #

Necesitas lo siguiente:


- Python >= 3.8
- Gradio
- Requests
- Archivo `.env` con las siguientes variables:
  ```env
  API_URL= https://api.jsonbin.io/v3/b/TU_BIN_ID
  X_MASTER_KEY= <TU_X_MASTER_KEY>
  X_ACCESS_KEY= <TU_X_ACCESS_KEY>
  BIN_PRIVATE= true
  BIN_NAME= NombreDelBin

  IMPORTANTE: Sustituye TU_X_MASTER_KEY, TU_X_ACCESS_KEY y TU_BIN_ID por tus propias credenciales y el ID del bin de jsonbin.io.

¿No te queda claro de dónde sacar los datos?

X_MASTER_KEY y X_ACCESS_KEY: se obtienen desde jsonbin.io una vez que creas una cuenta y generas una clave de API (en el dashboard).

API_URL: está compuesto por https://api.jsonbin.io/v3/b/ seguido del ID del bin (que obtienes al crear el bin en jsonbin.io).

BIN_NAME: es simplemente un nombre descriptivo para el bin (lo puedes elegir tú).

BIN_PRIVATE: pon true si el bin es privado (recomendado), o false si es público.

# ¿Cómo ejecutarlo en local? #

1. Clona el repositorio

git clone https://github.com/elvirarm/Proyecto_digitalizacion.git
cd Proyecto_digitalizacion

2. Crea un entorno virtual y actívalo

python -m venv venv
source venv/bin/activate  # En Windows usa venv\Scripts\activate

3. Instala las dependencias

pip install -r requirements.txt

4. Crea un archivo .env en el directorio raíz con tus credenciales de API.

5. Ejecuta la aplicación:

python menu.py


# Funcionalidades principales y cómo utilizarlas#

Una vez que ejecutes la aplicación simplemente tienes que copiar el link que se te ha generado en el navegador y utilizar la aplicación.


**Pestaña 1.  Añadir recetas:** Permite al usuario introducir nuevas recetas por categorías (desayuno, almuerzo y cena).

Se pide al introducir la receta:

- Nombre de la receta

- Categoría a la que pertenece

- Ingredientes separados por comas

- Instrucciones de la receta separadas por comas

**Ejemplo de entrada:**

Nombre de la receta: Panqueques de avena
Categoría (desayuno, almuerzo, cena): desayuno
Ingredientes (separados por ','): avena, huevo, banana, canela
Instrucciones (separadas por ','): mezclar ingredientes, calentar sartén, cocinar por ambos lados

**Pestaña 2. Ver recetas disponibles:** Muestra un listado de todas las recetas almacenadas localmente.

**Ejemplo de salida:**

- Desayuno:

Panqueques de avena

Tostadas con aguacate

- Almuerzo:

Ensalada de quinoa

- Cena:

Pizza casera

**Pestaña 3. Generar menú semanal:** Crea un menú semanal aleatorio basado en las recetas disponibles en cada categoría.

El ejemplo de salida sería similar al anterior, pero añadiéndole los días de la semana.

**Pestaña 4. Subir recetas a la nube:** Guarda las recetas locales en un archivo JSON en la nube.

**Pestaña 5. Cargar recetas desde la nube:** Recupera las recetas almacenadas en la nube y las combina con las locales.

**Pestaña 6. Eliminar recetas:** Permite eliminar recetas tanto del archivo local como de la nube (debes introducir el nombre de la receta que quieras eliminar).

7. Salir.