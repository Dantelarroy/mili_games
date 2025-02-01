import random
import streamlit as st


# Lista de preguntas con opciones y respuestas correctas
questions = [
{"question": "She ___ (talk) to her friend for hours.",
    "options": ["a) talked (/t/)", "b) talked (/d/)", "c) talked (/ɪd/)",],
    "answer": "a",
    "explanation": "'Talk' ends in a voiceless sound (/k/), so the -ed ending is pronounced as /t/."},

{"question": "They ___ (decide) to go out for dinner.",
    "options": ["a) decided (/ɪd/)", "b) decideed (/d/)", "c) decidd (/t/)",],
    "answer": "a",
    "explanation": "'Decide' ends in a /d/ sound, so the -ed ending is pronounced as /ɪd/."},

{"question": "Which past tense form has the /d/ pronunciation?",
    "options": ["a) Laughed", "b) Cleaned", "c) Waited"],
    "answer": "b",
    "explanation": "'Clean' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."},

{"question": "Which verb has the -ed pronounced as /t/?",
    "options": ["a) Played", "b) Watched", "c) Needed"],
    "answer": "b",
    "explanation": "'Watch' ends in a voiceless sound (/ʧ/), so the -ed ending is pronounced as /t/."},

{"question": "Which sentence contains a verb with the -ed pronounced as /ɪd/?",
    "options": ["a) She helped her sister.", "b) They painted the wall.", "c) He washed his car."],
    "answer": "b",
    "explanation": "'Paint' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."},

{"question": "She ___ (dance) at the party last night.",
    "options": ["a) danced (/t/)", "b) danced (/d/)", "c) danced (/ɪd/)",],
    "answer": "a",
    "explanation": "'Dance' ends in a voiceless sound (/s/), so the -ed ending is pronounced as /t/."},

{"question": "He ___ (need) help with his project.",
    "options": ["a) needed (/ɪd/)", "b) needd (/d/)", "c) needed (/t/)",],
    "answer": "a",
    "explanation": "'Need' ends in a /d/ sound, so the -ed ending is pronounced as /ɪd/."},

{"question": "They ___ (work) on the assignment together.",
    "options": ["a) worked (/t/)", "b) worked (/d/)", "c) worked (/ɪd/)",],
    "answer": "a",
    "explanation": "'Work' ends in a voiceless sound (/k/), so the -ed ending is pronounced as /t/."},

{"question": "She ___ (love) the movie.",
    "options": ["a) loved (/t/)", "b) loved (/d/)", "c) loved (/ɪd/)",],
    "answer": "b",
    "explanation": "'Love' ends in a voiced sound (/v/), so the -ed ending is pronounced as /d/."},

{"question": "He ___ (shout) at the game.",
    "options": ["a) shouted (/t/)", "b) shouted (/d/)", "c) shouted (/ɪd/)",],
    "answer": "c",
    "explanation": "'Shout' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."},
    {
        "question": "She ___ (ask) a question in class.",
        "options": ["a) asked (/t/)", "b) asked (/d/)", "c) asked (/ɪd/)"],
        "answer": "a",
        "explanation": "'Ask' ends in a voiceless sound (/k/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "He ___ (clean) his room before leaving.",
        "options": ["a) cleaned (/t/)", "b) cleaned (/d/)", "c) cleaned (/ɪd/)"],
        "answer": "b",
        "explanation": "'Clean' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (wait) for an hour.",
        "options": ["a) waited (/t/)", "b) waited (/d/)", "c) waited (/ɪd/)"],
        "answer": "c",
        "explanation": "'Wait' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "They ___ (laugh) at the joke.",
        "options": ["a) laughed (/t/)", "b) laughed (/d/)", "c) laughed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Laugh' ends in a voiceless sound (/f/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "He ___ (play) soccer yesterday.",
        "options": ["a) played (/t/)", "b) played (/d/)", "c) played (/ɪd/)"],
        "answer": "b",
        "explanation": "'Play' ends in a voiced sound (/j/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (call) her friend in the evening.",
        "options": ["a) called (/t/)", "b) called (/d/)", "c) called (/ɪd/)"],
        "answer": "b",
        "explanation": "'Call' ends in a voiced sound (/l/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "We ___ (start) a new project.",
        "options": ["a) started (/t/)", "b) started (/d/)", "c) started (/ɪd/)"],
        "answer": "c",
        "explanation": "'Start' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "They ___ (help) the elderly lady cross the street.",
        "options": ["a) helped (/t/)", "b) helped (/d/)", "c) helped (/ɪd/)"],
        "answer": "a",
        "explanation": "'Help' ends in a voiceless sound (/p/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "She ___ (enjoy) the concert.",
        "options": ["a) enjoyed (/t/)", "b) enjoyed (/d/)", "c) enjoyed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Enjoy' ends in a voiced sound (/j/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (finish) his homework early.",
        "options": ["a) finished (/t/)", "b) finished (/d/)", "c) finished (/ɪd/)"],
        "answer": "a",
        "explanation": "'Finish' ends in a voiceless sound (/ʃ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "They ___ (wash) their car on Sunday.",
        "options": ["a) washed (/t/)", "b) washed (/d/)", "c) washed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Wash' ends in a voiceless sound (/ʃ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "She ___ (change) her outfit before leaving.",
        "options": ["a) changed (/t/)", "b) changed (/d/)", "c) changed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Change' ends in a voiced sound (/ʤ/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (fix) his bike yesterday.",
        "options": ["a) fixed (/t/)", "b) fixed (/d/)", "c) fixed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Fix' ends in a voiceless sound (/ks/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "They ___ (decide) to travel abroad.",
        "options": ["a) decided (/t/)", "b) decided (/d/)", "c) decided (/ɪd/)"],
        "answer": "c",
        "explanation": "'Decide' ends in a /d/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "She ___ (agree) with his opinion.",
        "options": ["a) agreed (/t/)", "b) agreed (/d/)", "c) agreed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Agree' ends in a voiced sound (/iː/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "We ___ (finish) our work early.",
        "options": ["a) finished (/t/)", "b) finished (/d/)", "c) finished (/ɪd/)"],
        "answer": "a",
        "explanation": "'Finish' ends in a voiceless sound (/ʃ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "They ___ (borrow) some books from the library.",
        "options": ["a) borrowed (/t/)", "b) borrowed (/d/)", "c) borrowed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Borrow' ends in a voiced sound (/oʊ/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (visit) his grandmother last weekend.",
        "options": ["a) visited (/t/)", "b) visited (/d/)", "c) visited (/ɪd/)"],
        "answer": "c",
        "explanation": "'Visit' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "She ___ (type) a long email this morning.",
        "options": ["a) typed (/t/)", "b) typed (/d/)", "c) typed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Type' ends in a voiceless sound (/p/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "They ___ (plan) a surprise party.",
        "options": ["a) planned (/t/)", "b) planned (/d/)", "c) planned (/ɪd/)"],
        "answer": "b",
        "explanation": "'Plan' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (open) the window to let in fresh air.",
        "options": ["a) opened (/t/)", "b) opened (/d/)", "c) opened (/ɪd/)"],
        "answer": "b",
        "explanation": "'Open' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (help) their friend move to a new house.",
        "options": ["a) helped (/t/)", "b) helped (/d/)", "c) helped (/ɪd/)"],
        "answer": "a",
        "explanation": "'Help' ends in a voiceless sound (/p/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "He ___ (start) a new job last month.",
        "options": ["a) started (/t/)", "b) started (/d/)", "c) started (/ɪd/)"],
        "answer": "c",
        "explanation": "'Start' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "We ___ (close) the store early yesterday.",
        "options": ["a) closed (/t/)", "b) closed (/d/)", "c) closed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Close' ends in a voiced sound (/z/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (dance) beautifully at the event.",
        "options": ["a) danced (/t/)", "b) danced (/d/)", "c) danced (/ɪd/)"],
        "answer": "a",
        "explanation": "'Dance' ends in a voiceless sound (/s/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "He ___ (clean) his room before leaving.",
        "options": ["a) cleaned (/t/)", "b) cleaned (/d/)", "c) cleaned (/ɪd/)"],
        "answer": "b",
        "explanation": "'Clean' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (want) to go to the concert.",
        "options": ["a) wanted (/t/)", "b) wanted (/d/)", "c) wanted (/ɪd/)"],
        "answer": "c",
        "explanation": "'Want' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "She ___ (smile) when she saw the surprise.",
        "options": ["a) smiled (/t/)", "b) smiled (/d/)", "c) smiled (/ɪd/)"],
        "answer": "b",
        "explanation": "'Smile' ends in a voiced sound (/l/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (watch) a movie last night.",
        "options": ["a) watched (/t/)", "b) watched (/d/)", "c) watched (/ɪd/)"],
        "answer": "a",
        "explanation": "'Watch' ends in a voiceless sound (/ʧ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "They ___ (enjoy) the trip to the mountains.",
        "options": ["a) enjoyed (/t/)", "b) enjoyed (/d/)", "c) enjoyed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Enjoy' ends in a voiced sound (/j/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (call) her friend in the evening.",
        "options": ["a) called (/t/)", "b) called (/d/)", "c) called (/ɪd/)"],
        "answer": "b",
        "explanation": "'Call' ends in a voiced sound (/l/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (miss) the bus this morning.",
        "options": ["a) missed (/t/)", "b) missed (/d/)", "c) missed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Miss' ends in a voiceless sound (/s/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "He ___ (need) some help with his homework.",
        "options": ["a) needed (/t/)", "b) needed (/d/)", "c) needed (/ɪd/)"],
        "answer": "c",
        "explanation": "'Need' ends in a /d/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "We ___ (visit) our grandparents last weekend.",
        "options": ["a) visited (/t/)", "b) visited (/d/)", "c) visited (/ɪd/)"],
        "answer": "c",
        "explanation": "'Visit' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "She ___ (fix) the broken chair.",
        "options": ["a) fixed (/t/)", "b) fixed (/d/)", "c) fixed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Fix' ends in a voiceless sound (/ks/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "He ___ (listen) to music all afternoon.",
        "options": ["a) listened (/t/)", "b) listened (/d/)", "c) listened (/ɪd/)"],
        "answer": "b",
        "explanation": "'Listen' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (wash) the car together.",
        "options": ["a) washed (/t/)", "b) washed (/d/)", "c) washed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Wash' ends in a voiceless sound (/ʃ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "She ___ (decide) to study abroad.",
        "options": ["a) decided (/t/)", "b) decided (/d/)", "c) decided (/ɪd/)"],
        "answer": "c",
        "explanation": "'Decide' ends in a /d/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "He ___ (enjoy) the concert a lot.",
        "options": ["a) enjoyed (/t/)", "b) enjoyed (/d/)", "c) enjoyed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Enjoy' ends in a voiced sound (/j/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (work) late last night.",
        "options": ["a) worked (/t/)", "b) worked (/d/)", "c) worked (/ɪd/)"],
        "answer": "a",
        "explanation": "'Work' ends in a voiceless sound (/k/), so the -ed ending is pronounced as /t/."
    }
]
# Función para jugar el juego
def play_game():
    st.title("Welcome to the regular verbs game!")
    
    score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i + 1}: {q['question']}")
        option_selected = st.radio(f"Select an option:", q["options"], key=f"question_{i}", index=None)

        # Wait for the player to select an option
        if option_selected:
            # Check the answer
            if option_selected == q["options"][ord(q["answer"]) - 97]:
                st.success("Correct!")
                score += 1
                st.write(f"Explanation: {q['explanation']}")
            else:
                st.error("Incorrect.")
                st.write(f"Explanation: {q['explanation']}")

    st.subheader(f"\nYour final score: {score} out of {len(questions)}")

# Run the game
if __name__ == "__main__":
    play_game()
