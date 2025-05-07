# Proyecto_digitalizacion

# Weekly Recipe Book #

This project is a Python application that allows you to manage a personalized recipe book. With this tool, you can add recipes by category (breakfast, lunch, and dinner), view available recipes, generate a random weekly menu, and sync your recipes to the cloud using JSONBin.io.

# Motivation #

Eating shouldn't be a headache, but in today's hectic world, sometimes it is—whether it's because you're missing an ingredient due to lack of planning or you simply don’t know what to eat. That's why this project was created: to make your life a bit easier by offering the following:
- Register and categorize your recipes by meal type (breakfast, lunch, dinner).
- Generate a random weekly menu in seconds.
- Save and sync your recipes to the cloud so you’re not tied to one device.
- Keep everything in a simple format (.json) that’s easy to edit.

# Deployment Instructions #

You’ll need the following:

- Python >= 3.8
- Gradio
- Requests
- A .env file with the following variables:


API_URL = https://api.jsonbin.io/v3/b/YOUR_BIN_ID
X_MASTER_KEY = <YOUR_X_MASTER_KEY>
X_ACCESS_KEY = <YOUR_X_ACCESS_KEY>
BIN_PRIVATE = true
BIN_NAME = YourBinName


IMPORTANT: Replace YOUR_X_MASTER_KEY, YOUR_X_ACCESS_KEY, and YOUR_BIN_ID with your own credentials and the JSONBin.io bin ID.

Not sure where to get this info?

- X_MASTER_KEY and X_ACCESS_KEY: You get these from JSONBin.io after creating an account and generating an API key (in the dashboard).

- API_URL: This is made up of https://api.jsonbin.io/v3/b/ followed by the bin ID (which you get after creating a bin on JSONBin.io).

- BIN_NAME: This is just a descriptive name for the bin (you choose it).

- BIN_PRIVATE: Set to true if the bin is private (recommended), or false if it’s public.

# How to Run Locally #

1. Clone the repository:

git clone https://github.com/elvirarm/Proyecto_digitalizacion.git
cd Proyecto_digitalizacion

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # En Windows usa venv\Scripts\activate

3. Install the dependencies:

pip install -r requirements.txt

4. Create a .env file in the root directory with your API credentials.

5. Run the application:

python menu.py


# Main Features and How to Use Them #

Once the app is running, just copy the generated link into your browser to use the interface.



**Tab 1.  Add Recipes:** Allows the user to enter new recipes by category (breakfast, lunch, dinner).

You'll be asked to provide:

- Recipe name

- Category it belongs to

- Ingredients (comma-separated)

- Instructions (comma-separated)

**Example input:**

Nombre de la receta: Panqueques de avena
Categoría (desayuno, almuerzo, cena): desayuno
Ingredientes (separados por ','): avena, huevo, banana, canela
Instrucciones (separadas por ','): mezclar ingredientes, calentar sartén, cocinar por ambos lados

**Tab 2. View Available Recipes:** Displays a list of all locally stored recipes.

**Example output:**

- Desayuno:

Panqueques de avena

Tostadas con aguacate

- Almuerzo:

Ensalada de quinoa

- Cena:

Pizza casera

**Tab 3: Generate Weekly Menu:** Creates a random weekly menu based on the available recipes in each category.

The output is similar to the above but includes the days of the week.

**Tab 4: Upload Recipes to the Cloud:** Saves local recipes to a JSON file in the cloud.

**Tab 5: Load Recipes from the Cloud:** Retrieves recipes stored in the cloud and merges them with the local ones.

**Tab 6: Delete Recipes:** Allows you to delete recipes from both local storage and the cloud (you must enter the name of the recipe to delete).
