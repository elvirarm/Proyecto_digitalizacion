*Ciclo de vida del dato (5b):*

- ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?

Los datos se generan al pedírselos al usuario a través de la consola mediante las funciones introducir_receta().
El usuario debe introducir el nombre de la receta, los ingredientes y las intrucciones.

Estos datos que se han pedido se guardan localmente en un *JSON* (recetas.json), pero también tiene la opción de subirlo a la nube mediante la función guardar_json().

Los datos recogidos se utilizan para mostrar las recetas disponibles a través de ver_recetas_disponibles() y para mostrar_menu_semanal() que genera un menú de lunes a domingo con las recetas guardadas de forma aleatoria.

La eliminación de los datos se puede hacer con la función eliminar_receta() que permite borrar los datos de forma local e incluso borrarlos de la nube. 

- ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?

La *consistencia* de los datos se garantiza cuando se sobreescribe el json al añadir y eliminar una receta.

La *integridad* actualmente no se está trabajando bien porque al guardar el json en la nube y al cargarlo se pueden pisar las recetas porque se trabaja con un único json. Esto podría mejorarlo trabajando para que cada usuario tuviese su propio json de recetas, pudiendo compartirla con su el *ID* del archivo.

- Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?

*Almacenamiento en la nube (5f):*

- Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?


En la API se utilizan *IDs de acceso privadas* para que nadie que no tenga los ids pueda tener acceso a los datos, garantizando la seguridad.
Además de crear el repositorio de datos privado y usar un *ID único en la URL* (donde el ID es *67d217508a456b796674a341*) que sirve de puntero hacia el repositorio.

        url = "https://api.jsonbin.io/v3/b/67d217508a456b796674a341"
        "X-Master-Key":"$2a$10$YPbdwuG2GnwUMcfvEDi9A.pCni9x8VOsAQhhOAU4L1w.Lex/KLnRK",
        "X-Access-Key":"$2a$10$h4AJh0OW/9KMuLXKOU/.Uui1mqXi2w58umcWVAXOdzdXRg0lHmk3G",
        "X-Bin-Private":"true"

Respecto a la *disponibilidad*, es cierto que los datos de la nube dependen de la disponibilidad de la API, pero como también se guardan de manera local no sería un problema.


- ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?

*Almacenamiento de los datos en local*

Al principio me planteé dónde almacenar los datos, considerando las opciones que hemos visto en programación, como *JSON* o *XML*. Finalmente, me decanté por *JSON* debido a su simplicidad y facilidad de uso, ya que me parece una opción mucho más intuitiva y sencilla de trabajar.


*Almacenamiento de los datos en la nube*

Estuve buscando diferentes APIs para guardar el Json en la nube, pero todas las que encontré eran más complejas que estas o de pago.
Es por la *sencillez* y la *versión gratuita* que he elegido esta opción.

Aunque no las he considerado, existen otras alternativas: *Firebase, AWS S3*, o una base de datos en la nube (*MongoDB Atlas, PostgreSQL en la nube*).

- Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?

*Seguridad y regulación (5i):*

- ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?

Utilizo *claves API* para autentificarme en *JSONBIN*, pero es cierto que están expuestas en el código.
Además, los datos se guardan de forma privada, pero podría mejorar la seguridad más cifrando los datos y descifrándolos al leer.


- ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?

Pues actualmente no estoy trabajando con datos sensibles, pero mi idea es que más adelante añadir un *login* para que el usuario tuviese acceso a sus recetas y poder añadir una capa extra de protección.

Si tratara con datos de usuario me afectaría el *Reglamento General de Protección de Datos (GDPR)* que es la normativa que se encarga de regular la protección de datos en la Unión Europea. Además en España los datos de los usuarios también se protegen a través de la *Ley Orgánica de Protección de Datos (LOPD)* que afectaría a mi proyecto.

- Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?

*Implicación de las THD en negocio y planta (2e):*

- ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?

La aplicación más básica que se me ocurre para mi software en un entorno de negocio sería en el ámbito de la *nutrición y dietética*. Por ejemplo, un/a nutricionista o dietista que se dedique a diseñar menús semanales para sus clientes podría beneficiarse enormemente de esta herramienta.

El software le permitiría tener una base de datos de recetas saludables predefinidas, lo que facilitaría la creación de menús personalizados de manera rápida y eficiente. Además, al generar menús automáticamente, el profesional ahorraría tiempo y podría centrarse en otras tareas, como la atención personalizada a sus clientes, respondiendo a posibles dudas que puedan surgir durante la sesión e implementando cambios.

- ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?

Mi software agiliza y simplifica el trabajo en varios aspectos:

## Automatización de tareas repetitivas:

En lugar de crear menús manualmente, el software genera automáticamente combinaciones de recetas, lo que reduce el tiempo dedicado a esta tarea.

## Flexibilidad y personalización:

Si el menú generado no es del todo adecuado, se puede regenerar fácilmente hasta obtener una opción que se ajuste a las necesidades del cliente.

## Organización y acceso rápido:

Al tener todas las recetas almacenadas y categorizadas, el acceso a la información es inmediato, lo que facilita la toma de decisiones.

- Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?

También se me ocurre que podría aplicarse a cualquier entorno donde se trabaje con alimentación. Por ejemplo: en hospitales que ofrecen la comida a los pacientes, en los comedores escolares e incluso a nivel particular, en casa para pensar rápidamente qué comer durante la semana, ahorrando tiempo. 

*Mejoras en IT y OT (2f):*

- ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?

- ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?

- Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?

Mi software no aplica a IT u OT porque está pensado más para facilitar la vida a nivel de usuario o a pequeños negocios.
Sin embargo, podría adaptarlo de esta forma:

## Integración con IT ##

1. Para conectarlo con sistemas empresariales:

- Integrar el software con un *ERP (Enterprise Resource Planning)* para gestionar inventarios de ingredientes y optimizar costes.

- Conectar con un *CRM (Customer Relationship Management)* para personalizar menús según las preferencias de los clientes.

2. Automatización avanzada:

- Usar *inteligencia artificial (IA)* para sugerir recetas basadas en ingredientes disponibles o preferencias del usuario.

- Implementar un sistema de notificaciones para recordar la compra de ingredientes o la preparación de comidas.

3. Análisis de datos:

- Usar herramientas de análisis para estudiar patrones de consumo y optimizar la planificación de menús.

## Integración con OT ##

1. Conexión con dispositivos IoT:

- Integrar el software con sensores en cocinas industriales para monitorear el uso de ingredientes en tiempo real.

- Conectar con dispositivos de medición (balanzas, termómetros) para garantizar que las recetas se sigan correctamente.

2. Gestión de inventarios en planta:

- Conectar el software con sistemas de gestión de inventarios para automatizar la compra de ingredientes cuando estos estén por agotarse.

*Tecnologías Habilitadoras Digitales (2g):*

- ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?

He utilizado *JSOBIN* par almacenar los datos en la nube y *APIs REST* para interactuar con servicios externos.


- ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?

*JSONBIN* aporta acceso remoto a los datos, lo que facilita su uso en diferentes dispositivos y respaldo de los datos lo que facilita la recuperación de los datos en caso de que se pierda el archivo local.

*APIs REST* permite que el programa se integre con otros servicios o aplicaciones, además facilita añadir nuevas funcionalidades en un futuro.

- Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?

Podría utilizar la *IA* para sugerir recetas o para darle el nombre de la receta que el usuario quiera y que esta genere automáticamente en el JSON los ingredientes y la receta con la estructura correcta.