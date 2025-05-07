This is an open-source project, and all contributions are welcome!

## GUIDE TO CONTRIBUTE TO THE PROJECT ##

1. Clone the repository

git clone <https://github.com/elvirarm/Proyecto_digitalizacion.git>
cd <directory_name>

2.  Install the required dependencies

This project requires some Python libraries to function properly. To install them, run:

pip install -r requirements.txt

3. Set up the Environment Variables

This project uses a .env file to load the necessary configuration variables, such as the API keys and server URL. You need to create a .env file in the root directory and add the following variables:

API_URL= https://api.jsonbin.io/v3/b/YOUR_BIN_ID
X_MASTER_KEY= <YOUR_X_MASTER_KEY>
X_ACCESS_KEY= <YOUR_X_ACCESS_KEY>
BIN_PRIVATE= true
BIN_NAME= BinName

IMPORTANT: Replace YOUR_X_MASTER_KEY, YOUR_X_ACCESS_KEY, and TU_BIN_ID with your own credentials and the bin ID from jsonbin.io.

Not sure where to get these values?

- X_MASTER_KEY and X_ACCESS_KEY: These are obtained from jsonbin.io once you create an account and generate an API key (on the dashboard).

- API_URL: This is composed of https://api.jsonbin.io/v3/b/ followed by the bin ID (which you get when creating the bin on jsonbin.io).

- BIN_NAME: This is just a descriptive name for the bin (you can choose it).

- BIN_PRIVATE: Set this to true if the bin is private (recommended), or false if it is public.


4. Develop and test locally

Once you've configured everything correctly, you can run the application locally using:

python menu.py

5. Submit a pull request

If you make improvements or bug fixes, you can submit a pull request with your changes.


## INTERESTING EXTENSIONS ##

If you are looking for ideas on how you could contribute to the project, here are a few suggestions, but feel free to add your own:

1. Recipe Management Improvements

- Tags or Descriptions: Add the ability to add tags or brief descriptions to recipes to make searching easier.

- Sort Recipes: Implement a function that allows users to sort recipes by name, preparation time, difficulty, or popularity.

- Recipe Images: Allow users to upload images to accompany the recipes.

2. Advanced Menu Generation

- Menu Based on Dietary Preferences: Add the option to generate menus based on preferences such as vegan, gluten-free, or low-calorie.

- Random Menu with Restrictions: Allow for generating weekly menus with dietary restrictions or specific allergies.

3. Integration with External APIs

- Nutrition API: Integrate an API that provides nutritional information for the ingredients in the recipes so that users can view the nutritional value of their dishes.

- Ingredient Purchase APIs: Implement functionality to check the prices of ingredients in online stores and facilitate direct purchasing from the interface.