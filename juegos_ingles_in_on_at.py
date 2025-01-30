import random
import streamlit as st


# Lista de preguntas con opciones y respuestas correctas
questions = [    {
        "question": "I will meet you ___ the airport at 3 p.m.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific places like airports, stations, or locations in general."
    },
    {
        "question": "She is studying ___ the library right now.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for enclosed spaces like rooms, buildings, and vehicles."
    },
    {
        "question": "We will go to the park ___ Sunday afternoon.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for days and dates."
    },
    {
        "question": "I have a meeting ___ the morning tomorrow.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for parts of the day (morning, afternoon, evening)."
    },
    {
        "question": "He always arrives ___ 9 a.m. for work.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific times."
    },
    {
        "question": "They are going to meet ___ the restaurant for dinner.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like restaurants, shops, and events."
    },
    {
        "question": "I haven't seen her ___ Monday.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific days."
    },
    {
        "question": "We are going to stay ___ a hotel for the weekend.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for places where you stay temporarily, such as hotels or someone’s house."
    },
    {
        "question": "They always visit their grandparents ___ Christmas.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific holidays or dates."
    },
    {
        "question": "I saw her ___ the supermarket last night.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for enclosed spaces like stores or rooms."
    },
    {
        "question": "We stayed ___ a lovely cottage during our holiday.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for enclosed spaces, such as rooms or buildings, or for general areas like a city."
    },
    {
        "question": "I'll see you ___ the concert tonight.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations or events, like concerts or meetings."
    },
    {
        "question": "She is traveling ___ Europe this summer.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for countries, cities, or large areas."
    },
    {
        "question": "I was born ___ November 5th, 1990.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific dates."
    },
    {
        "question": "I usually go for a walk ___ the morning before work.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for parts of the day (morning, afternoon, evening)."
    },
    {
        "question": "We met ___ the bus stop this morning.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific places, such as bus stops or entrances."
    },
    {
        "question": "They got married ___ 2020.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for years, months, and seasons."
    },
    {
        "question": "The party will be held ___ my house tomorrow.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific places, especially homes or events."
    },
    {
        "question": "I prefer to exercise ___ the gym rather than at home.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for indoor places or locations that are enclosed."
    },
    {
        "question": "She was sitting ___ the couch, reading a book.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for surfaces like chairs, couches, or tables."
    },
    {
        "question": "He was born ___ the 21st of March.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific dates or days."
    },
    {
        "question": "They live ___ New York City.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for cities, countries, and larger areas."
    },
    {
        "question": "I'll meet you ___ the park at noon.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations, like parks or schools."
    },
    {
        "question": "The meeting will be held ___ the office on Monday.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific places, such as buildings or locations."
    },
    {
        "question": "They met ___ the coffee shop yesterday.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for places where events or meetings happen."
    },
    {
        "question": "The event is scheduled ___ the evening of July 5th.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for parts of the day such as morning, afternoon, and evening."
    },
    {
        "question": "My birthday is ___ December.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for months, years, or seasons."
    },
    {
        "question": "She usually works ___ an office, but today she's working from home.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for enclosed spaces or general areas like an office."
    },
    {
        "question": "The concert will be held ___ Friday evening.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific days of the week."
    },
    {
        "question": "We usually go for a run ___ the morning.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for parts of the day like morning, afternoon, or evening."
    },
    {
        "question": "We went for a walk ___ the beach during our vacation.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for surfaces like beaches, streets, or roads."
    },
    {
        "question": "He will arrive ___ the airport at 6 p.m.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations such as airports or stations."
    },
    {
        "question": "They are having a party ___ the weekend.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for longer periods of time such as months, years, or weekends."
    },
    {
        "question": "I met him ___ the restaurant last night.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like restaurants, stores, or events."
    },
    {
        "question": "She was born ___ 1992.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for years."
    },
    {
        "question": "The meeting is scheduled ___ 10 a.m. tomorrow.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific times of the day."
    },
    {
        "question": "We are going to visit her ___ Christmas.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for holidays or periods like Christmas or New Year."
    },
    {
        "question": "She works ___ a large company in the city center.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for organizations, places, or areas."
    },
    {
        "question": "We met ___ the library after class.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for meeting points or specific places."
    },
    {
        "question": "I will call you ___ Tuesday afternoon.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific days of the week."
    },
     {
        "question": "I like to read books ___ the evening, after dinner.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for parts of the day such as morning, afternoon, or evening."
    },
    {
        "question": "They met each other ___ the party last night.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific events or locations."
    },
    {
        "question": "I live ___ the third floor of the building.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for floors or surfaces."
    },
    {
        "question": "We are going to travel ___ the summer to Europe.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for seasons or long periods of time."
    },
    {
        "question": "The meeting is scheduled ___ 10 o'clock sharp.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific times."
    },
    {
        "question": "The conference will be held ___ a famous hotel downtown.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like a hotel or venue."
    },
    {
        "question": "I will finish the project ___ the end of this month.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for longer periods of time, like months or years."
    },
    {
        "question": "He arrived ___ the airport just in time for his flight.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific places, such as airports or stations."
    },
    {
        "question": "The painting was created ___ the 18th century.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for centuries or periods of time."
    },
    {
        "question": "I haven't seen you ___ ages! How have you been?",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' to talk about long periods of time (e.g., ages, years)."
    },
    {
        "question": "My friends are coming over ___ Saturday evening.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific days of the week."
    },
    {
        "question": "The car was parked ___ the garage for the night.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for enclosed spaces like rooms, buildings, or garages."
    },
    {
        "question": "She is currently studying ___ Harvard University.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for institutions like universities or schools."
    },
    {
        "question": "We went for a walk ___ the park last weekend.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for larger areas like parks or countries."
    },
    {
        "question": "I usually jog ___ the morning before work.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for times of the day like morning, afternoon, or evening."
    },
    {
        "question": "They celebrated their anniversary ___ Paris last year.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for cities and countries."
    },
        {
        "question": "We are meeting ___ the train station at 3 p.m.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like stations or airports."
    },
    {
        "question": "She moved to the city ___ 2010, and she has lived there ever since.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for years or periods of time."
    },
    {
        "question": "The office is located ___ the second floor of the building.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for floors or surfaces."
    },
    {
        "question": "He was born ___ the middle of the 20th century.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for centuries or long periods of time."
    },
    {
        "question": "We will have finished the project ___ the end of the year.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for periods of time like months, years, or seasons."
    },
    {
        "question": "I will see you ___ Monday morning for our meeting.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific days of the week."
    },
    {
        "question": "My parents are coming to visit me ___ Christmas this year.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for holidays like Christmas, New Year, etc."
    },
    {
        "question": "I left my keys ___ the kitchen table.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for surfaces like tables, desks, or counters."
    },
    {
        "question": "The concert is going to be held ___ the central park this weekend.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like venues or events."
    },
    {
        "question": "They arrived ___ the airport late, so they missed their flight.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific places like airports or train stations."
    },
    {
        "question": "We will be there ___ 8 o'clock sharp, so please be on time.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific times."
    },
    {
        "question": "She always goes jogging ___ the park every Sunday morning.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for larger areas such as parks or cities."
    },
    {
        "question": "The hotel is located ___ the corner of the street.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations such as corners or intersections."
    },
    {
        "question": "I found your letter ___ the bottom of the drawer.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for enclosed spaces such as drawers or boxes."
    },
    {
        "question": "We have to leave ___ 15 minutes if we want to catch the bus.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for periods of time like minutes or hours."
    },
    {
        "question": "I met him ___ the library last week while I was studying.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like libraries or events."
    },
        {
        "question": "She was born ___ July 1st, 1995.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific dates."
    },
    {
        "question": "They are planning to travel ___ the summer holidays.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for months, seasons, and years."
    },
    {
        "question": "I will see you ___ the airport around noon.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations such as airports."
    },
    {
        "question": "They live ___ a small town near the beach.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for cities, towns, or countries."
    },
    {
        "question": "I’m meeting my friends ___ the café later.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like cafés or restaurants."
    },
    {
        "question": "The concert is going to be held ___ the weekend.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for days and dates."
    },
    {
        "question": "We have to leave ___ the next two hours.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for a period of time from now (e.g., in two hours)."
    },
    {
        "question": "She works ___ a large company in the city center.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for places of work like companies or offices."
    },
    {
        "question": "The museum is located ___ the north side of the city.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for areas or parts of a location, like 'in the north side'."
    },
    {
        "question": "I’ll meet you ___ the bus stop in 10 minutes.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like bus stops."
    },
    {
        "question": "The book is placed ___ the shelf, next to the window.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for surfaces like shelves."
    },
    {
        "question": "We’re going to visit them ___ Christmas Eve.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for specific days, including holidays."
    },
    {
        "question": "The meeting is scheduled ___ 3 p.m. tomorrow.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific times."
    },
    {
        "question": "He lives ___ the 10th floor of a building.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for floors in a building."
    },
    {
        "question": "I will arrive ___ the station at noon.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for locations like stations."
    },
    {
        "question": "The restaurant is located ___ the corner of the street.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like corners."
    },
    {
        "question": "We’re going to spend the night ___ a hotel.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for enclosed spaces like hotels."
    },
    {
        "question": "I will see you ___ the park later today.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for larger areas like parks."
    },
    {
        "question": "The kids are playing ___ the garden right now.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for enclosed spaces like gardens."
    },
    {
        "question": "She’s coming back ___ the afternoon.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for parts of the day like afternoon, morning, evening."
    },
    {
        "question": "The train will arrive ___ 10 minutes.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for periods of time."
    },
    {
        "question": "I saw her ___ the library yesterday.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for locations like libraries."
    },
    {
        "question": "The party will be ___ Friday night, not Saturday.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for days of the week."
    },
    {
        "question": "I will be on vacation ___ August.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for months or years."
    },
    {
        "question": "I found my phone ___ the bed this morning.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for surfaces like beds, tables, etc."
    },
    {
        "question": "We will meet ___ the restaurant at 7 p.m.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "a",
        "explanation": "Use 'at' for specific locations like restaurants."
    },
    {
        "question": "The festival is held ___ the summer months.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "b",
        "explanation": "Use 'in' for months, seasons, or periods of time."
    },
    {
        "question": "The cat is sitting ___ the window.",
        "options": ["a) at", "b) in", "c) on"],
        "answer": "c",
        "explanation": "Use 'on' for surfaces like windows."
    }
    ]

# Función para jugar el juego
def play_game():
    st.title("¡Bienvenido al juego de 'in', 'on' and 'at'!")
    
    score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Pregunta {i + 1}: {q['question']}")
        option_selected = st.radio(f"Selecciona una opción:", q["options"], key=f"question_{i}", index=None)

        # Esperar que el jugador seleccione una opción
        if option_selected:
            # Verificar la respuesta
            if option_selected == q["options"][ord(q["answer"]) - 97]:
                st.success("¡Correcto!")
                score += 1
                st.write(f"Explicación: {q['explanation']}")
            else:
                st.error("Incorrecto.")
                st.write(f"Explicación: {q['explanation']}")

    st.subheader(f"\nTu puntuación final: {score} de {len(questions)}")

# Ejecutar el juego
if __name__ == "__main__":
    play_game()
