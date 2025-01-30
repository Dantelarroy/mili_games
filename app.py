import streamlit as st
from PIL import Image

# Importar los juegos como módulos
import juegos_ingles_in_on_at  # Asegúrate de que 'game1.py' esté en el mismo directorio
import juegos_ingles_tenses  # Asegúrate de que 'game2.py' esté en el mismo directorio

# Título de la aplicación
st.title("¡Bienvenidos!")

# Crear un selectbox para elegir el juego
game_choice = st.selectbox(
    "¿Qué juego te gustaría jugar?",
    [None, "Juego de Tenses", "Juego de In,At,On"]  # El valor predeterminado es None
)

# Cargar la imagen
image_path = "images/image.jpg"  # Ensure the relative path is correct
image = Image.open(image_path)
# Mostrar la imagen en la portada
st.image(image, caption="¡Diviértete con los Mili Games!", width=int(st.beta_container().width * 0.7))

# Ejecutar el juego correspondiente si se selecciona una opción
if game_choice == "Juego de Tenses":
    juegos_ingles_tenses.play_game()  # Llamar a la función del primer juego
elif game_choice == "Juego de In,At,On":
    juegos_ingles_in_on_at.play_game()  # Llamar a la función del segundo juego
