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
    },
 {
        "question": "He ___ (play) soccer with his friends.",
        "options": ["a) played (/t/)", "b) played (/d/)", "c) played (/ɪd/)"],
        "answer": "b",
        "explanation": "'Play' ends in a voiced sound (/j/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (wash) their car on Sunday.",
        "options": ["a) washed (/t/)", "b) washed (/d/)", "c) washed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Wash' ends in a voiceless sound (/ʃ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "She ___ (open) the window for fresh air.",
        "options": ["a) opened (/t/)", "b) opened (/d/)", "c) opened (/ɪd/)"],
        "answer": "b",
        "explanation": "'Open' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (start) a new job last week.",
        "options": ["a) started (/t/)", "b) started (/d/)", "c) started (/ɪd/)"],
        "answer": "c",
        "explanation": "'Start' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "They ___ (fix) the broken chair.",
        "options": ["a) fixed (/t/)", "b) fixed (/d/)", "c) fixed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Fix' ends in a voiceless sound (/ks/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "She ___ (enjoy) the party a lot.",
        "options": ["a) enjoyed (/t/)", "b) enjoyed (/d/)", "c) enjoyed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Enjoy' ends in a voiced sound (/j/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (push) the door open.",
        "options": ["a) pushed (/t/)", "b) pushed (/d/)", "c) pushed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Push' ends in a voiceless sound (/ʃ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "They ___ (paint) the house blue.",
        "options": ["a) painted (/t/)", "b) painted (/d/)", "c) painted (/ɪd/)"],
        "answer": "c",
        "explanation": "'Paint' ends in a /t/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "She ___ (call) her friend last night.",
        "options": ["a) called (/t/)", "b) called (/d/)", "c) called (/ɪd/)"],
        "answer": "b",
        "explanation": "'Call' ends in a voiced sound (/l/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (hope) to see his family soon.",
        "options": ["a) hoped (/t/)", "b) hoped (/d/)", "c) hoped (/ɪd/)"],
        "answer": "a",
        "explanation": "'Hope' ends in a voiceless sound (/p/), so the -ed ending is pronounced as /t/."
    },
 {
        "question": "She ___ (help) him with his homework.",
        "options": ["a) helped (/t/)", "b) helped (/d/)", "c) helped (/ɪd/)"],
        "answer": "b",
        "explanation": "'Help' ends in a voiced sound (/p/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (jump) over the fence.",
        "options": ["a) jumped (/t/)", "b) jumped (/d/)", "c) jumped (/ɪd/)"],
        "answer": "a",
        "explanation": "'Jump' ends in a voiceless sound (/p/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "He ___ (study) all night for the exam.",
        "options": ["a) studied (/t/)", "b) studied (/d/)", "c) studied (/ɪd/)"],
        "answer": "b",
        "explanation": "'Study' ends in a voiced sound (/d/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "We ___ (try) to solve the problem.",
        "options": ["a) tried (/t/)", "b) tried (/d/)", "c) tried (/ɪd/)"],
        "answer": "a",
        "explanation": "'Try' ends in a voiceless sound (/r/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "She ___ (open) the window to get some fresh air.",
        "options": ["a) opened (/t/)", "b) opened (/d/)", "c) opened (/ɪd/)"],
        "answer": "b",
        "explanation": "'Open' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (finish) their project on time.",
        "options": ["a) finished (/t/)", "b) finished (/d/)", "c) finished (/ɪd/)"],
        "answer": "c",
        "explanation": "'Finish' ends in a sound /ʃ/, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "He ___ (work) hard all week.",
        "options": ["a) worked (/t/)", "b) worked (/d/)", "c) worked (/ɪd/)"],
        "answer": "b",
        "explanation": "'Work' ends in a voiced sound (/k/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "We ___ (talk) about our plans for the weekend.",
        "options": ["a) talked (/t/)", "b) talked (/d/)", "c) talked (/ɪd/)"],
        "answer": "b",
        "explanation": "'Talk' ends in a voiced sound (/k/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (work) as a teacher for many years.",
        "options": ["a) worked (/t/)", "b) worked (/d/)", "c) worked (/ɪd/)"],
        "answer": "b",
        "explanation": "'Work' ends in a voiced sound (/k/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (celebrate) their anniversary last month.",
        "options": ["a) celebrated (/t/)", "b) celebrated (/d/)", "c) celebrated (/ɪd/)"],
        "answer": "c",
        "explanation": "'Celebrate' ends in a sound /t/, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "She ___ (work) at the hospital last year.",
        "options": ["a) worked (/t/)", "b) worked (/d/)", "c) worked (/ɪd/)"],
        "answer": "b",
        "explanation": "'Work' ends in a voiced sound (/k/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (play) football on Sunday.",
        "options": ["a) played (/t/)", "b) played (/d/)", "c) played (/ɪd/)"],
        "answer": "b",
        "explanation": "'Play' ends in a voiced sound (/l/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (call) his friend last night.",
        "options": ["a) called (/t/)", "b) called (/d/)", "c) called (/ɪd/)"],
        "answer": "b",
        "explanation": "'Call' ends in a voiced sound (/l/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "We ___ (clean) the house yesterday.",
        "options": ["a) cleaned (/t/)", "b) cleaned (/d/)", "c) cleaned (/ɪd/)"],
        "answer": "b",
        "explanation": "'Clean' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "I ___ (arrive) early this morning.",
        "options": ["a) arrived (/t/)", "b) arrived (/d/)", "c) arrived (/ɪd/)"],
        "answer": "b",
        "explanation": "'Arrive' ends in a voiced sound (/v/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (help) her mother with cooking.",
        "options": ["a) helped (/t/)", "b) helped (/d/)", "c) helped (/ɪd/)"],
        "answer": "b",
        "explanation": "'Help' ends in a voiced sound (/p/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (finish) the report this morning.",
        "options": ["a) finished (/t/)", "b) finished (/d/)", "c) finished (/ɪd/)"],
        "answer": "c",
        "explanation": "'Finish' ends in a /ʃ/ sound, so the -ed ending is pronounced as /ɪd/."
    },
    {
        "question": "We ___ (visit) our grandparents last weekend.",
        "options": ["a) visited (/t/)", "b) visited (/d/)", "c) visited (/ɪd/)"],
        "answer": "b",
        "explanation": "'Visit' ends in a voiced sound (/t/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (plan) a surprise party for her.",
        "options": ["a) planned (/t/)", "b) planned (/d/)", "c) planned (/ɪd/)"],
        "answer": "b",
        "explanation": "'Plan' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (start) his new job yesterday.",
        "options": ["a) started (/t/)", "b) started (/d/)", "c) started (/ɪd/)"],
        "answer": "b",
        "explanation": "'Start' ends in a voiced sound (/t/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (laugh) at the funny joke.",
        "options": ["a) laughed (/t/)", "b) laughed (/d/)", "c) laughed (/ɪd/)"],
        "answer": "a",
        "explanation": "'Laugh' ends in a voiceless sound (/f/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "They ___ (shout) at the concert.",
        "options": ["a) shouted (/t/)", "b) shouted (/d/)", "c) shouted (/ɪd/)"],
        "answer": "a",
        "explanation": "'Shout' ends in a voiceless sound (/tʃ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "He ___ (close) the door before leaving.",
        "options": ["a) closed (/t/)", "b) closed (/d/)", "c) closed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Close' ends in a voiced sound (/z/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "We ___ (watch) a movie together last night.",
        "options": ["a) watched (/t/)", "b) watched (/d/)", "c) watched (/ɪd/)"],
        "answer": "a",
        "explanation": "'Watch' ends in a voiceless sound (/ʧ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "I ___ (wait) for my friend at the park.",
        "options": ["a) waited (/t/)", "b) waited (/d/)", "c) waited (/ɪd/)"],
        "answer": "b",
        "explanation": "'Wait' ends in a voiced sound (/t/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (play) the piano for hours.",
        "options": ["a) played (/t/)", "b) played (/d/)", "c) played (/ɪd/)"],
        "answer": "b",
        "explanation": "'Play' ends in a voiced sound (/l/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (enjoy) the concert very much.",
        "options": ["a) enjoyed (/t/)", "b) enjoyed (/d/)", "c) enjoyed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Enjoy' ends in a voiced sound (/j/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (cook) a delicious dinner for his family.",
        "options": ["a) cooked (/t/)", "b) cooked (/d/)", "c) cooked (/ɪd/)"],
        "answer": "a",
        "explanation": "'Cook' ends in a voiceless sound (/k/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "We ___ (clean) the kitchen yesterday.",
        "options": ["a) cleaned (/t/)", "b) cleaned (/d/)", "c) cleaned (/ɪd/)"],
        "answer": "b",
        "explanation": "'Clean' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (visit) her grandparents last weekend.",
        "options": ["a) visited (/t/)", "b) visited (/d/)", "c) visited (/ɪd/)"],
        "answer": "b",
        "explanation": "'Visit' ends in a voiced sound (/t/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "He ___ (study) for the exam all day.",
        "options": ["a) studied (/t/)", "b) studied (/d/)", "c) studied (/ɪd/)"],
        "answer": "b",
        "explanation": "'Study' ends in a voiced sound (/d/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (jump) over the puddle.",
        "options": ["a) jumped (/t/)", "b) jumped (/d/)", "c) jumped (/ɪd/)"],
        "answer": "a",
        "explanation": "'Jump' ends in a voiceless sound (/p/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "We ___ (enroll) in the new course.",
        "options": ["a) enrolled (/t/)", "b) enrolled (/d/)", "c) enrolled (/ɪd/)"],
        "answer": "b",
        "explanation": "'Enroll' ends in a voiced sound (/l/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (talk) to her friend on the phone.",
        "options": ["a) talked (/t/)", "b) talked (/d/)", "c) talked (/ɪd/)"],
        "answer": "b",
        "explanation": "'Talk' ends in a voiced sound (/k/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (enjoy) their vacation in the mountains.",
        "options": ["a) enjoyed (/t/)", "b) enjoyed (/d/)", "c) enjoyed (/ɪd/)"],
        "answer": "b",
        "explanation": "'Enjoy' ends in a voiced sound (/j/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "I ___ (watch) a documentary last night.",
        "options": ["a) watched (/t/)", "b) watched (/d/)", "c) watched (/ɪd/)"],
        "answer": "a",
        "explanation": "'Watch' ends in a voiceless sound (/ʧ/), so the -ed ending is pronounced as /t/."
    },
    {
        "question": "He ___ (help) his brother with the homework.",
        "options": ["a) helped (/t/)", "b) helped (/d/)", "c) helped (/ɪd/)"],
        "answer": "b",
        "explanation": "'Help' ends in a voiced sound (/p/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (arrive) at the airport just in time.",
        "options": ["a) arrived (/t/)", "b) arrived (/d/)", "c) arrived (/ɪd/)"],
        "answer": "b",
        "explanation": "'Arrive' ends in a voiced sound (/v/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "She ___ (clean) the house all morning.",
        "options": ["a) cleaned (/t/)", "b) cleaned (/d/)", "c) cleaned (/ɪd/)"],
        "answer": "b",
        "explanation": "'Clean' ends in a voiced sound (/n/), so the -ed ending is pronounced as /d/."
    },
    {
        "question": "They ___ (finish) their project last week.",
        "options": ["a) finished (/t/)", "b) finished (/d/)", "c) finished (/ɪd/)"],
        "answer": "c",
        "explanation": "'Finish' ends in a voiceless sound (/ʃ/), so the -ed ending is pronounced as /ɪd/."
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
