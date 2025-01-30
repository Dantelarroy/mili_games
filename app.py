import streamlit as st
from PIL import Image

# Importar los juegos como módulos
import juegos_ingles_in_on_at  # Asegúrate de que 'game1.py' esté en el mismo directorio
import juegos_ingles_tenses  # Asegúrate de que 'game2.py' esté en el mismo directorio

# Título de la aplicación
st.title("Welcome!")

# Crear un selectbox para elegir el juego
game_choice = st.selectbox(
    "Which game would you like to play?",
    [None, "Tenses Game", "In, At, On Game"]  # El valor predeterminado es None
)

# Cargar la imagen
image_path = "images/image.jpg"  # Ensure the relative path is correct
image = Image.open(image_path)
# Mostrar la imagen en la portada
st.image(image, caption="¡Diviértete con los Mili Games!", use_container_width=True)

# Ejecutar el juego correspondiente si se selecciona una opción
if game_choice == "Tenses Game":
    juegos_ingles_tenses.play_game()  # Llamar a la función del primer juego
elif game_choice == "In, At, On Game":
    juegos_ingles_in_on_at.play_game()  # Llamar a la función del segundo juego
