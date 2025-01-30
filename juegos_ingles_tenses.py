import random
import streamlit as st


# Lista de preguntas con opciones y respuestas correctas
questions = [{
        "question": "She ___ (work) in the office every day.",
        "options": ["a) work", "b) works", "c) is working"],
        "answer": "b",
        "explanation": "Use the Present Simple tense for habits or routines."
    },
    {
        "question": "Right now, he ___ (watch) TV in the living room.",
        "options": ["a) watch", "b) watches", "c) is watching"],
        "answer": "c",
        "explanation": "Use the Present Continuous tense to describe actions happening right now."
    },
    {
        "question": "I ___ (never/see) that movie before.",
        "options": ["a) never saw", "b) have never seen", "c) never see"],
        "answer": "b",
        "explanation": "Use the Present Perfect tense to express experiences that have happened at an unspecified time."
    },
    {
        "question": "They ___ (study) for their exams last night.",
        "options": ["a) study", "b) studied", "c) are studying"],
        "answer": "b",
        "explanation": "Use the Past Simple tense for actions that happened at a specific time in the past."
    },
    {
        "question": "She always ___ (arrive) early to work.",
        "options": ["a) arrive", "b) arrives", "c) is arriving"],
        "answer": "b",
        "explanation": "Use the Present Simple tense to describe habits or general truths."
    },
    {
        "question": "I ___ (eat) lunch when the phone rang.",
        "options": ["a) ate", "b) was eating", "c) have eaten"],
        "answer": "b",
        "explanation": "Use the Past Continuous tense for actions that were happening at a specific moment in the past."
    },
    {
        "question": "He ___ (not/finish) his homework yet.",
        "options": ["a) doesn't finish", "b) didn't finish", "c) hasn't finished"],
        "answer": "c",
        "explanation": "Use the Present Perfect tense for actions that haven't happened yet, but are related to the present."
    },
    {
        "question": "I ___ (study) English since I was 10 years old.",
        "options": ["a) studied", "b) am studying", "c) have been studying"],
        "answer": "c",
        "explanation": "Use the Present Perfect Continuous tense to show an action that started in the past and is still continuing."
    },
    {
        "question": "He ___ (leave) when I arrived at the party.",
        "options": ["a) leaves", "b) left", "c) has left"],
        "answer": "b",
        "explanation": "Use the Past Simple tense for actions that were completed at a definite time in the past."
    },
    {
        "question": "We ___ (live) in New York for five years before we moved to California.",
        "options": ["a) lived", "b) had lived", "c) have lived"],
        "answer": "b",
        "explanation": "Use the Past Perfect tense for actions that happened before another action in the past."
    },
    {
        "question": "I ___ (not/finish) reading the book yet.",
        "options": ["a) don't finish", "b) didn't finish", "c) haven't finished"],
        "answer": "c",
        "explanation": "Use the Present Perfect tense to indicate that something hasn't been completed yet, but is relevant to the present."
    },
    {
        "question": "She ___ (always/complain) about the weather.",
        "options": ["a) always complains", "b) is always complaining", "c) always complained"],
        "answer": "b",
        "explanation": "Use the Present Continuous tense with adverbs like 'always' to describe annoying habits."
    },
    {
        "question": "He ___ (travel) to Europe last summer.",
        "options": ["a) travels", "b) traveled", "c) is traveling"],
        "answer": "b",
        "explanation": "Use the Past Simple tense for actions that occurred at a specific time in the past."
    },
    {
        "question": "We ___ (not/see) that movie yet.",
        "options": ["a) haven't seen", "b) didn't see", "c) don't see"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense to talk about actions that have not happened up until now."
    },
    {
        "question": "By the time we arrived, they ___ (finish) their dinner.",
        "options": ["a) finished", "b) had finished", "c) finish"],
        "answer": "b",
        "explanation": "Use the Past Perfect tense to show that an action was completed before another action in the past."
    },
    {
        "question": "I ___ (not/like) the food at the restaurant.",
        "options": ["a) didn't like", "b) don't like", "c) haven't liked"],
        "answer": "b",
        "explanation": "Use the Present Simple tense to express preferences or general dislikes."
    },
    {
        "question": "They ___ (work) on the project for two hours when I called them.",
        "options": ["a) worked", "b) had worked", "c) were working"],
        "answer": "c",
        "explanation": "Use the Past Continuous tense to show an ongoing action in the past."
    },
    {
        "question": "I ___ (not/understand) the lesson before the teacher explained it again.",
        "options": ["a) didn't understand", "b) hadn't understood", "c) don't understand"],
        "answer": "b",
        "explanation": "Use the Past Perfect tense to describe an action completed before another action in the past."
    },
    {
        "question": "They ___ (already/finish) their homework by the time I arrived.",
        "options": ["a) already finished", "b) had already finished", "c) have already finished"],
        "answer": "b",
        "explanation": "Use the Past Perfect tense to talk about actions completed before another past event."
    },
    {
        "question": "He ___ (work) here for five years.",
        "options": ["a) works", "b) worked", "c) has worked"],
        "answer": "c",
        "explanation": "Use the Present Perfect tense for actions that started in the past and continue to the present."
    },
    {
        "question": "I ___ (like) ice cream, but I don't eat it often.",
        "options": ["a) like", "b) likes", "c) am liking"],
        "answer": "a",
        "explanation": "Use the Present Simple tense for general preferences."
    },
    {
        "question": "She ___ (not/go) to the gym yesterday because she was sick.",
        "options": ["a) doesn't go", "b) didn't go", "c) isn't going"],
        "answer": "b",
        "explanation": "Use the Past Simple tense for actions completed in the past."
    },
    {
        "question": "We ___ (wait) for the bus when it started to rain.",
        "options": ["a) were waiting", "b) are waiting", "c) waited"],
        "answer": "a",
        "explanation": "Use the Past Continuous tense for actions happening at a specific time in the past."
    },
    {
        "question": "By the time he arrives, I ___ (finish) my work.",
        "options": ["a) finish", "b) will finish", "c) will have finished"],
        "answer": "c",
        "explanation": "Use the Future Perfect tense to describe actions that will be completed before a specific point in the future."
    },
    {
        "question": "I ___ (not/see) her at the party last night.",
        "options": ["a) didn't see", "b) don't see", "c) haven't seen"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for actions completed in the past."
    },
    {
        "question": "They ___ (travel) to Spain this summer.",
        "options": ["a) travel", "b) are traveling", "c) will travel"],
        "answer": "c",
        "explanation": "Use the Future Simple tense for actions that will happen in the future."
    },
    {
        "question": "She ___ (always/help) me when I ask.",
        "options": ["a) helps", "b) is always helping", "c) always helps"],
        "answer": "c",
        "explanation": "Use the Present Simple tense for habitual actions or general truths."
    },
    {
        "question": "I ___ (finish) my homework when the phone rang.",
        "options": ["a) finished", "b) was finishing", "c) had finished"],
        "answer": "c",
        "explanation": "Use the Past Perfect tense for actions that were completed before another past event."
    },
    {
        "question": "He ___ (not/understand) the instructions, so he asked for help.",
        "options": ["a) doesn't understand", "b) didn't understand", "c) hasn't understood"],
        "answer": "b",
        "explanation": "Use the Past Simple tense for actions that happened and were completed in the past."
    },
    {
        "question": "By next month, I ___ (learn) how to play the guitar.",
        "options": ["a) will have learned", "b) will learn", "c) will be learning"],
        "answer": "a",
        "explanation": "Use the Future Perfect tense to talk about something that will be completed by a specific future time."
    },
    {
        "question": "I ___ (not/finish) reading the book yet.",
        "options": ["a) haven't finished", "b) didn't finish", "c) don't finish"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense for actions that haven't been completed yet but are relevant now."
    },
    {
        "question": "We ___ (wait) for the bus for 20 minutes when it finally arrived.",
        "options": ["a) were waiting", "b) have waited", "c) waited"],
        "answer": "a",
        "explanation": "Use the Past Continuous tense for actions that were ongoing in the past."
    },
    {
        "question": "I ___ (already/see) that movie twice.",
        "options": ["a) already saw", "b) have already seen", "c) had already seen"],
        "answer": "b",
        "explanation": "Use the Present Perfect tense for actions that have happened at an unspecified time and have relevance to the present."
    },
    {
        "question": "She ___ (not/come) to the party because she was busy.",
        "options": ["a) didn't come", "b) doesn't come", "c) hasn't come"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for actions that were completed in the past."
    },
    {
        "question": "We ___ (just/finish) our lunch.",
        "options": ["a) have just finished", "b) finished", "c) are just finishing"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense to talk about actions completed recently."
    },
    {
        "question": "I ___ (never/visit) Paris, but I want to go there someday.",
        "options": ["a) never visited", "b) never visit", "c) have never visited"],
        "answer": "c",
        "explanation": "Use the Present Perfect tense for experiences that happened at an unspecified time in the past."
    },
    {
        "question": "He ___ (work) on the project all day yesterday.",
        "options": ["a) worked", "b) has worked", "c) was working"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for actions that happened at a specific time in the past."
    },
    {
        "question": "I ___ (not/see) him for a long time.",
        "options": ["a) haven't seen", "b) didn't see", "c) don't see"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense to talk about something that has not happened yet but is relevant to the present."
    },
    {
        "question": "She ___ (not/arrive) at the station when the train left.",
        "options": ["a) didn't arrive", "b) hadn't arrived", "c) doesn't arrive"],
        "answer": "b",
        "explanation": "Use the Past Perfect tense to show an action that happened before another past event."
    },
    {
        "question": "By the time we arrive at the cinema, the movie ___ (already/start).",
        "options": ["a) has already started", "b) had already started", "c) will have already started"],
        "answer": "c",
        "explanation": "Use the Future Perfect tense to describe an action that will be completed before a specific point in the future."
    },
    {
        "question": "I ___ (never/forget) the time we went on a road trip together.",
        "options": ["a) never forgot", "b) have never forgotten", "c) never forget"],
        "answer": "b",
        "explanation": "Use the Present Perfect tense for experiences that have relevance to the present."
    },
    {
        "question": "I wish I ___ (be) able to visit you this weekend, but I have to work.",
        "options": ["a) am", "b) will be", "c) were"],
        "answer": "c",
        "explanation": "Use the past simple (were) after 'wish' for hypothetical situations in the present."
    },
    {
        "question": "She ___ (study) when I called her last night.",
        "options": ["a) was studying", "b) studied", "c) has studied"],
        "answer": "a",
        "explanation": "Use the Past Continuous tense for actions that were ongoing at a specific time in the past."
    },
    {
        "question": "I ___ (not/see) him since he moved to another city.",
        "options": ["a) haven't seen", "b) didn't see", "c) don't see"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense for actions that began in the past and continue to the present."
    },
    {
        "question": "If you ___ (be) more careful, you wouldn't have broken the vase.",
        "options": ["a) are", "b) were", "c) had been"],
        "answer": "b",
        "explanation": "Use 'were' for unreal past conditions in the Second Conditional."
    },
    {
        "question": "They ___ (live) in this neighborhood for over 10 years now.",
        "options": ["a) live", "b) have lived", "c) are living"],
        "answer": "b",
        "explanation": "Use the Present Perfect tense for actions that started in the past and continue to the present."
    },
    {
        "question": "By next year, we ___ (complete) the project.",
        "options": ["a) will complete", "b) will have completed", "c) completed"],
        "answer": "b",
        "explanation": "Use the Future Perfect tense to describe an action that will be completed before a specific future time."
    },
    {
        "question": "I ___ (work) in this company for five years when I get my promotion.",
        "options": ["a) work", "b) will be working", "c) will have been working"],
        "answer": "c",
        "explanation": "Use the Future Perfect Continuous tense to describe an ongoing action that will continue up to a point in the future."
    },
    {
        "question": "They ___ (already/finish) their homework before the teacher arrived.",
        "options": ["a) had already finished", "b) already finished", "c) have already finished"],
        "answer": "a",
        "explanation": "Use the Past Perfect tense for an action completed before another action in the past."
    },
    {
        "question": "She ___ (learn) French for three years when she goes to Paris next summer.",
        "options": ["a) has been learning", "b) will have learned", "c) will learn"],
        "answer": "b",
        "explanation": "Use the Future Perfect tense to describe an action that will be completed before a future event."
    },
    {
        "question": "If I ___ (know) you were coming, I would have baked a cake.",
        "options": ["a) know", "b) will know", "c) had known"],
        "answer": "c",
        "explanation": "Use the Past Perfect tense after 'if' in the Third Conditional for unreal past situations."
    },
    {
        "question": "I can't believe they ___ (buy) that house. It looks amazing!",
        "options": ["a) bought", "b) buy", "c) have bought"],
        "answer": "c",
        "explanation": "Use the Present Perfect tense to indicate a recent action that is relevant now."
    },
    {
        "question": "I ___ (not/finish) my homework yet. I still have a few questions to answer.",
        "options": ["a) haven't finished", "b) didn't finish", "c) don't finish"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense to talk about actions that have not been completed up until now."
    },
    {
        "question": "We ___ (arrive) at the station by the time the train left.",
        "options": ["a) arrived", "b) had arrived", "c) will have arrived"],
        "answer": "b",
        "explanation": "Use the Past Perfect tense to talk about an action completed before another past action."
    },
    {
        "question": "I ___ (never/understand) why people enjoy skydiving.",
        "options": ["a) never understood", "b) have never understood", "c) never understand"],
        "answer": "b",
        "explanation": "Use the Present Perfect tense for something that has never happened before up to now."
    },
    {
        "question": "If I ___ (be) you, I would take the job offer.",
        "options": ["a) am", "b) were", "c) will be"],
        "answer": "b",
        "explanation": "Use 'were' for unreal present conditions in the Second Conditional."
    },
    {
        "question": "When I was a child, I ___ (play) outside every day.",
        "options": ["a) played", "b) was playing", "c) had played"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for habitual actions in the past."
    },
    {
        "question": "I ___ (read) a great book at the moment. It's about ancient history.",
        "options": ["a) am reading", "b) have read", "c) read"],
        "answer": "a",
        "explanation": "Use the Present Continuous tense for actions happening right now."
    },
    {
        "question": "We ___ (not/meet) before, have we?",
        "options": ["a) haven't met", "b) didn't meet", "c) don't meet"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense for something that has not happened up until now."
    },
    {
        "question": "She ___ (take) the bus to work every morning, but today she is driving.",
        "options": ["a) takes", "b) is taking", "c) has taken"],
        "answer": "a",
        "explanation": "Use the Present Simple tense for regular habits or routines."
    },
    {
        "question": "I ___ (feel) so tired after that long walk yesterday.",
        "options": ["a) felt", "b) feel", "c) have felt"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for emotions felt at a specific time in the past."
    },
        {
        "question": "She ___ (work) at a café every weekend.",
        "options": ["a) works", "b) worked", "c) is working"],
        "answer": "a",
        "explanation": "Use the Present Simple tense for routines and habitual actions."
    },
    {
        "question": "By the time we arrive, they ___ (finish) their dinner.",
        "options": ["a) will have finished", "b) finished", "c) will finish"],
        "answer": "a",
        "explanation": "Use the Future Perfect tense for actions that will be completed before a specific point in the future."
    },
    {
        "question": "I ___ (never/see) that movie before.",
        "options": ["a) never saw", "b) have never seen", "c) never see"],
        "answer": "b",
        "explanation": "Use the Present Perfect tense for actions that happened at an unspecified time and are relevant to the present."
    },
    {
        "question": "He ___ (not/eat) any vegetables since he was a child.",
        "options": ["a) hasn't eaten", "b) didn't eat", "c) doesn't eat"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense to talk about actions that started in the past and continue to the present."
    },
    {
        "question": "They ___ (study) for their exams right now.",
        "options": ["a) study", "b) are studying", "c) studied"],
        "answer": "b",
        "explanation": "Use the Present Continuous tense for actions happening at the moment of speaking."
    },
    {
        "question": "If we ___ (know) about the traffic, we would have left earlier.",
        "options": ["a) knew", "b) have known", "c) had known"],
        "answer": "c",
        "explanation": "Use the Past Perfect tense in the Third Conditional to talk about unreal situations in the past."
    },
    {
        "question": "I ___ (go) to the gym every morning, but today I am too tired.",
        "options": ["a) go", "b) am going", "c) went"],
        "answer": "a",
        "explanation": "Use the Present Simple tense for regular actions or habits."
    },
    {
        "question": "He ___ (already/finish) the project by the time I asked him.",
        "options": ["a) had already finished", "b) already finished", "c) has already finished"],
        "answer": "a",
        "explanation": "Use the Past Perfect tense for actions that were completed before another past action."
    },
    {
        "question": "I wish I ___ (not/miss) the meeting yesterday.",
        "options": ["a) don't miss", "b) didn't miss", "c) hadn't missed"],
        "answer": "c",
        "explanation": "Use the Past Perfect tense after 'wish' for unreal past situations."
    },
    {
        "question": "By this time next year, she ___ (graduate) from college.",
        "options": ["a) has graduated", "b) will have graduated", "c) will graduate"],
        "answer": "b",
        "explanation": "Use the Future Perfect tense to talk about actions that will be completed before a specific future time."
    },
    {
        "question": "I ___ (watch) TV when you called me.",
        "options": ["a) watched", "b) am watching", "c) was watching"],
        "answer": "c",
        "explanation": "Use the Past Continuous tense for actions that were in progress at a specific time in the past."
    },
    {
        "question": "She ___ (travel) to Paris next month.",
        "options": ["a) will travel", "b) is traveling", "c) travels"],
        "answer": "a",
        "explanation": "Use the Future Simple tense for planned future actions."
    },
    {
        "question": "They ___ (live) in that house for over 20 years now.",
        "options": ["a) have lived", "b) live", "c) are living"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense for actions that started in the past and continue to the present."
    },
    {
        "question": "I ___ (not/finish) my homework yet.",
        "options": ["a) haven't finished", "b) didn't finish", "c) don't finish"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense to talk about actions that have not been completed yet."
    },
    {
        "question": "We ___ (not/go) to the cinema last weekend.",
        "options": ["a) don't go", "b) didn't go", "c) haven't gone"],
        "answer": "b",
        "explanation": "Use the Past Simple tense for actions completed at a specific time in the past."
    },
    {
        "question": "If she ___ (study) more, she would have passed the exam.",
        "options": ["a) studies", "b) studied", "c) had studied"],
        "answer": "c",
        "explanation": "Use the Past Perfect tense in the Third Conditional for unreal past situations."
    },
    {
        "question": "I ___ (see) him yesterday at the store.",
        "options": ["a) saw", "b) seen", "c) have seen"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for actions that happened at a specific time in the past."
    },
    {
        "question": "They ___ (not/come) to the party because they were sick.",
        "options": ["a) didn't come", "b) aren't coming", "c) haven't come"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for actions that were completed in the past."
    },
    {
        "question": "She ___ (not/want) to go to the park yesterday.",
        "options": ["a) didn't want", "b) doesn't want", "c) hasn't wanted"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for actions that happened and were completed in the past."
    },
    {
        "question": "I ___ (read) the book when you called me.",
        "options": ["a) was reading", "b) read", "c) am reading"],
        "answer": "a",
        "explanation": "Use the Past Continuous tense for actions that were ongoing in the past."
    },
    {
        "question": "She ___ (never/try) sushi before, but she liked it when she did.",
        "options": ["a) never tried", "b) has never tried", "c) never tries"],
        "answer": "b",
        "explanation": "Use the Present Perfect tense for experiences up to the present."
    },
    {
        "question": "He ___ (play) football for 10 years before he injured his leg.",
        "options": ["a) played", "b) had played", "c) plays"],
        "answer": "b",
        "explanation": "Use the Past Perfect tense for an action that was completed before another action in the past."
    },
    {
        "question": "I wish I ___ (be) on vacation right now.",
        "options": ["a) am", "b) were", "c) will be"],
        "answer": "b",
        "explanation": "Use 'were' for unreal present conditions in the Second Conditional."
    },
    {
        "question": "By the time we finish, they ___ (already/leave).",
        "options": ["a) will have already left", "b) had already left", "c) have already left"],
        "answer": "a",
        "explanation": "Use the Future Perfect tense for actions that will be completed before a specific time in the future."
    },
    {
        "question": "I ___ (be) very busy lately, that's why I haven't called you.",
        "options": ["a) am", "b) have been", "c) was"],
        "answer": "b",
        "explanation": "Use the Present Perfect Continuous tense to describe an action that started in the past and continues into the present."
    },
    {
        "question": "She ___ (never/be) to Italy.",
        "options": ["a) has never been", "b) never was", "c) is never"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense to talk about life experiences up until now."
    },
    {
        "question": "I ___ (be) to that restaurant several times.",
        "options": ["a) have been", "b) was", "c) am"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense for actions that happened at an unspecified time."
    },
    {
        "question": "I ___ (not/see) him recently. Have you?",
        "options": ["a) haven't seen", "b) didn't see", "c) don't see"],
        "answer": "a",
        "explanation": "Use the Present Perfect tense for actions that haven't happened yet but are relevant now."
    },
    {
        "question": "By the time I finish this book, I ___ (read) 10 novels this year.",
        "options": ["a) will have read", "b) will read", "c) will be reading"],
        "answer": "a",
        "explanation": "Use the Future Perfect tense to talk about something that will be completed before a specific future time."
    },
    {
        "question": "If she ___ (study) harder, she would have passed the exam.",
        "options": ["a) studied", "b) had studied", "c) studies"],
        "answer": "b",
        "explanation": "Use the Past Perfect tense after 'if' in the Third Conditional for unreal past situations."
    },
    {
        "question": "He ___ (not/answer) the phone when I called him yesterday.",
        "options": ["a) didn't answer", "b) hasn't answered", "c) wasn't answering"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for actions completed at a specific time in the past."
    },
    {
        "question": "I ___ (take) the train tomorrow to avoid the traffic.",
        "options": ["a) am taking", "b) will take", "c) will be taking"],
        "answer": "b",
        "explanation": "Use the Future Simple tense for planned actions in the future."
    },
    {
        "question": "When I ___ (arrive), they were already eating.",
        "options": ["a) arrived", "b) had arrived", "c) arrive"],
        "answer": "b",
        "explanation": "Use the Past Perfect tense to describe an action that was completed before another action in the past."
    },
    {
        "question": "She ___ (travel) to Japan next year for a vacation.",
        "options": ["a) travels", "b) will travel", "c) is traveling"],
        "answer": "b",
        "explanation": "Use the Future Simple tense to describe planned events in the future."
    },
    {
        "question": "If I ___ (have) more time, I would visit you more often.",
        "options": ["a) have", "b) had", "c) will have"],
        "answer": "b",
        "explanation": "Use 'had' for unreal present conditions in the Second Conditional."
    },
    {
        "question": "They ___ (watch) a movie when the power went out.",
        "options": ["a) watched", "b) were watching", "c) have watched"],
        "answer": "b",
        "explanation": "Use the Past Continuous tense for actions that were ongoing in the past."
    },
    {
        "question": "I ___ (not/feel) well, so I stayed at home yesterday.",
        "options": ["a) didn't feel", "b) don't feel", "c) haven't felt"],
        "answer": "a",
        "explanation": "Use the Past Simple tense for actions completed at a specific time in the past."
    },
    {
        "question": "By the time you arrive, I ___ (finish) all my work.",
        "options": ["a) will finish", "b) have finished", "c) will have finished"],
        "answer": "c",
        "explanation": "Use the Future Perfect tense to describe an action that will be completed before a specific future time."
    },
    {
    "question": "I ___ (never/see) such a beautiful sunset before.",
    "options": ["a) have never seen", "b) never saw", "c) had never seen"],
    "answer": "a",
    "explanation": "Use the Present Perfect tense to describe experiences up to the present."
    }]

# Función para jugar el juego
def play_game():
    st.title("Welcome to the Tenses Game!")
        # Game description
    st.write("""
    In this game, you will test your knowledge of English verb tenses. The questions are related to the following tenses:
    - **Present Simple**
    - **Present Continuous**
    - **Past Simple**
    - **Present Perfect**
    """)
    
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
