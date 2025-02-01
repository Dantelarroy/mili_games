import streamlit as st
from PIL import Image

# Importar los juegos como módulos
import juegos_ingles_in_on_at  # Asegúrate de que 'juegos_ingles_in_on_at.py' esté en el mismo directorio
import juegos_ingles_tenses  # Asegúrate de que 'juegos_ingles_tenses.py' esté en el mismo directorio
import juegos_ingles_regular_verbs  # Nuevo juego añadido

# Título de la aplicación
st.title("Welcome!")

# Crear un selectbox para elegir el juego
game_choice = st.selectbox(
    "Which game would you like to play? Select an option and scroll down",
    [None, "Tenses Game", "In, At, On Game", "Regular Verbs Game"]  # Agregamos la nueva opción
)

# Cargar la imagen
image_path = "images/image.jpg"  # Ensure the relative path is correct
image = Image.open(image_path)

# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 6, 1])  # La columna central tiene mayor peso
with col2:
    st.image(image, caption="Have fun with the Mili Games!", width=500)

# Ejecutar el juego correspondiente si se selecciona una opción
if game_choice == "Tenses Game":
    juegos_ingles_tenses.play_game()  # Llamar a la función del primer juego
elif game_choice == "In, At, On Game":
    juegos_ingles_in_on_at.play_game()  # Llamar a la función del segundo juego
elif game_choice == "Regular Verbs Game":
    juegos_ingles_regular_verbs.play_game()  # Llamar a la función del nuevo juego
