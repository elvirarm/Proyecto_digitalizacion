¡Este es un proyecto open source, todas las aportaciones son bienvenidas!

## GUÍA PARA CONTRIBUIR AL PROYECTO ##

1. Clonar el repositorio

git clone <https://github.com/elvirarm/Proyecto_digitalizacion.git>
cd <nombre_del_directorio>

2.  Instalar las dependencias necesarias

Este proyecto requiere algunas bibliotecas de Python para funcionar correctamente. Para instalarlas, ejecuta:

pip install -r requirements.txt

3. Configurar las variables de Entorno

Este proyecto utiliza un archivo .env para cargar las variables de configuración necesarias, como las claves de la API y la URL del servidor. Debes crear un archivo .env en el directorio raíz y agregar las siguientes variables:

API_URL= https://api.jsonbin.io/v3/b/TU_BIN_ID
X_MASTER_KEY= <TU_X_MASTER_KEY>
X_ACCESS_KEY= <TU_X_ACCESS_KEY>
BIN_PRIVATE= true
BIN_NAME= NombreDelBin

IMPORTANTE: Sustituye TU_X_MASTER_KEY, TU_X_ACCESS_KEY y TU_BIN_ID por tus propias credenciales y el ID del bin de jsonbin.io.

¿No te queda claro de dónde sacar los datos?

- X_MASTER_KEY y X_ACCESS_KEY: se obtienen desde jsonbin.io una vez que creas una cuenta y generas una clave de API (en el dashboard).

- API_URL: está compuesto por https://api.jsonbin.io/v3/b/ seguido del ID del bin (que obtienes al crear el bin en jsonbin.io).

- BIN_NAME: es simplemente un nombre descriptivo para el bin (lo puedes elegir tú).

- BIN_PRIVATE: pon true si el bin es privado (recomendado), o false si es público.



4. Desarrollar y probar localmente

Una vez que hayas configurado todo correctamente, puedes ejecutar la aplicación de manera local usando:

python menu.py

5. Enviar un pull request

Si realizas mejoras o correcciones de errores, puedes enviar un pull request con tus cambios.

## AMPLIACIONES DE INTERÉS ##

Si quieres algunas ideas de cómo podrías contribuir al proyecto ahí te van unas cuantas, pero siéntete libre de aportar las tuyas propias:

1. Mejoras en la Gestión de Recetas

- Etiquetas o Descripción: Añadir la posibilidad de agregar etiquetas o descripciones breves a las recetas para facilitar la búsqueda.

- Ordenar Recetas: Implementar una función que permita ordenar las recetas por nombre, tiempo de preparación, dificultad, o popularidad.

- Imágenes de Recetas: Permitir que los usuarios suban imágenes para acompañar las recetas.

2. Generación de Menús Más Avanzados

- Menú por Preferencias Dietéticas: Añadir la opción de generar menús según preferencias como vegano, sin gluten, o bajo en calorías.

- Menú Aleatorio con Restricciones: Permitir la generación de menús semanales con restricciones dietéticas o alergias específicas.

3. Integración con APIs Externas

- API de Nutrición: Integrar una API que proporcione información nutricional de los ingredientes de las recetas para que los usuarios puedan ver el valor nutricional de sus platos.

- APIs de Compra de Ingredientes: Implementar una funcionalidad para consultar precios de los ingredientes en tiendas en línea y facilitar la compra directa desde la interfaz.