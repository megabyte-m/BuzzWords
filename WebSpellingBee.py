import streamlit as st
import pyttsx3
import random
import threading
import pathlib
import base64
from pydub import AudioSegment
import time


# Audio Duration

def get_audio_duration(file_path):
    audio_file = AudioSegment.from_file(file_path)
    duration = audio_file.duration_seconds
    return duration


# CSS READING

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")


# CSS LOADING

css_path = pathlib.Path("assets/styles.css")
load_css(css_path)


# READING THE FILES 

if 'word_list1' not in st.session_state:
    file_word = open("assets/Data/W1.txt") 
    file_data = file_word.read() 
    st.session_state.word_list1 = file_data.splitlines() 

if 'defs_list1' not in st.session_state:
    file_defs = open("assets/Data/Defs1.txt") 
    defs_data = file_defs.read() 
    st.session_state.defs_list1 = defs_data.splitlines() 


if 'word_list2' not in st.session_state:
    file_word = open("assets/Data/W2.txt") 
    file_data = file_word.read() 
    st.session_state.word_list2 = file_data.splitlines() 
    st.session_state.word_list = file_data.splitlines()

if 'defs_list2' not in st.session_state:
    file_defs = open("assets/Data/Defs2.txt") 
    defs_data = file_defs.read() 
    st.session_state.defs_list2 = defs_data.splitlines() 
    st.session_state.defs_list = defs_data.splitlines()


if 'word_list3' not in st.session_state:
    file_word = open("assets/Data/W3.txt") 
    file_data = file_word.read() 
    st.session_state.word_list3 = file_data.splitlines() 

if 'defs_list3' not in st.session_state:
    file_defs = open("assets/Data/Defs3.txt") 
    defs_data = file_defs.read() 
    st.session_state.defs_list3 = defs_data.splitlines() 



# THE SESSION STATES


if 'current_word' not in st.session_state:
    st.session_state.current_word = random.randint(1, 300)

if 'current_word_spelling' not in st.session_state:
    st.session_state.current_word_spelling = ""

if 'correct_output' not in st.session_state:
    st.session_state.correct_output = 2

if 'hearts_counter' not in st.session_state:
    st.session_state.hearts_counter = 3

if 'play_but_disabled' not in st.session_state:
    st.session_state.play_but_disabled = True

if 'check_but_disabled' not in st.session_state:
    st.session_state.check_but_disabled = True 

if 'def_but_disabled' not in st.session_state:
    st.session_state.def_but_disabled = True

if 'easy_but_disabled' not in st.session_state:
    st.session_state.easy_but_disabled = False

if 'moderate_but_disabled' not in st.session_state:
    st.session_state.moderate_but_disabled = False

if 'diff_but_disabled' not in st.session_state:
    st.session_state.diff_but_disabled = False

if 'correct_no' not in st.session_state:
    st.session_state.correct_no = 0

if 'reset_but_disabled' not in st.session_state:
    st.session_state.reset_but_disabled = True

if 'difficulty_level' not in st.session_state:
    st.session_state.difficulty_level = 2

if 'audio_file' not in st.session_state:
    st.session_state.audio_file = ""


# MAKING SURE BUTTONS CAN'T BE CLICKED AT THE SAME TIME


def disable_all_but():
    st.session_state.play_but_disabled = True
    st.session_state.check_but_disabled = True
    st.session_state.def_but_disabled = True
   # st.session_state.reset_but_disabled = True

def game_over():
    st.session_state.play_but_disabled = True
    st.session_state.check_but_disabled = True
    st.session_state.def_but_disabled = True
    st.session_state.easy_but_disabled = True
    st.session_state.moderate_but_disabled = True
    st.session_state.diff_but_disabled = True

def enable_all_but():
    st.session_state.play_but_disabled = False
    st.session_state.check_but_disabled = False
    st.session_state.def_but_disabled = False




# FUNCTIONS



def heart_emoji():

    if st.session_state.hearts_counter == 3:
        return "💖 💖 💖"
    
    if st.session_state.hearts_counter == 2:
        return "💖 💖 🤍"

    if st.session_state.hearts_counter == 1:
        return "💖 🤍 🤍"
    
    if st.session_state.hearts_counter == 0:
        return "🤍 🤍 🤍  ---------  You ran out of lives!"



def say_word(audio_file):

    # speaker = pyttsx3.init()
    # speaker.say(f'{word}')
    # speaker.runAndWait()
    
    # if speaker._inLoop:
    #     speaker.endLoop()

    st.session_state.audio_file = audio_file


def audio_button_clicked():
    
    # disable_all_but()
    # threading.Thread(target=say_word, args=(st.session_state.word_list[st.session_state.current_word],)).start()

    st.session_state.current_word = random.randint(0, 299)

    enable_all_but()
    st.session_state.correct_output = 2
    word_audio_file = f'assets/Data/Audio/L{st.session_state.difficulty_level}/{st.session_state.current_word}_{st.session_state.word_list[st.session_state.current_word]}.mp3'
    say_word(word_audio_file)



def defs_button_clicked():

    #disable_all_but()
    # threading.Thread(target=say_word, args=(st.session_state.defs_list[st.session_state.current_word],)).start()
    
    def_audio_file = f'assets/Data/Audio/L{st.session_state.difficulty_level}/{st.session_state.current_word}_{st.session_state.word_list[st.session_state.current_word]}_def.mp3'
    say_word(def_audio_file)
    


def check_spelling():
    
    if entry_word == "":
        return

    if entry_word.lower() == st.session_state.word_list[st.session_state.current_word]:
        st.session_state.correct_output = 1
        st.session_state.correct_no = st.session_state.correct_no + 1

    else:
        st.session_state.correct_output = 0
        st.session_state.hearts_counter = st.session_state.hearts_counter - 1
        st.session_state.current_word_spelling = st.session_state.word_list[st.session_state.current_word]

    if st.session_state.hearts_counter == 0:
        game_over()




def set_easy():
    st.session_state.word_list = st.session_state.word_list1
    st.session_state.defs_list = st.session_state.defs_list1
    st.session_state.easy_but_disabled = False
    st.session_state.moderate_but_disabled = True
    st.session_state.diff_but_disabled = True
    st.session_state.play_but_disabled = False
    st.session_state.reset_but_disabled = False
    st.session_state.difficulty_level = 1

def set_moderate():
    st.session_state.word_list = st.session_state.word_list2
    st.session_state.defs_list = st.session_state.defs_list2
    st.session_state.easy_but_disabled = True
    st.session_state.moderate_but_disabled = False
    st.session_state.diff_but_disabled = True
    st.session_state.play_but_disabled = False
    st.session_state.reset_but_disabled = False
    st.session_state.difficulty_level = 2

def set_difficult():
    st.session_state.word_list = st.session_state.word_list3
    st.session_state.defs_list = st.session_state.defs_list3
    st.session_state.easy_but_disabled = True
    st.session_state.moderate_but_disabled = True
    st.session_state.diff_but_disabled = False
    st.session_state.play_but_disabled = False
    st.session_state.reset_but_disabled = False
    st.session_state.difficulty_level = 3



def reset():
    st.session_state.hearts_counter = 3
    st.session_state.correct_no = 0
    st.session_state.easy_but_disabled = False
    st.session_state.moderate_but_disabled = False
    st.session_state.diff_but_disabled = False
    disable_all_but()
    st.session_state.correct_output = 2
    st.session_state.difficulty_level = 2



# THE UI


st.html(f'<p class="title"> BuzzWords </p>')



col_h, col_s = st.columns([4, 1])

with col_h:

    st.html(f'<p class="lives"> Lives: {heart_emoji()} </p>')

with col_s:
    st.html(f'<p class="alignright"> Correct Words: {st.session_state.correct_no} </p>')




col_du1, col_cor, col_du2 = st.columns([1,3,1])

with col_du1:
    st.write("")

with col_cor:
    if st.session_state.correct_output == 0:
       st.html(f'<p class="incorrect"> Incorrect! - {st.session_state.current_word_spelling} </p>')

    if st.session_state.correct_output == 1:
       st.html('<p class="correct"> Correct! </p>')

    if st.session_state.correct_output == 2:
        st.html('<p class="waiting"> Type it in! </p>')

with col_du2:
    st.write("")
    


col1, col2 = st.columns([3, 1])

with col1:
    entry_word = st.text_input(label="Spell here:",label_visibility="collapsed", placeholder="Spell the word here...", key="styledinput")
    attempt_button = st.button("Check Spelling", on_click=check_spelling, disabled=st.session_state.check_but_disabled, use_container_width=True)

with col2:
    audio_button = st.button("Play Word", on_click=audio_button_clicked, disabled=st.session_state.play_but_disabled, use_container_width=True)
    defs_button = st.button("Play Definition", on_click=defs_button_clicked, disabled=st.session_state.def_but_disabled, use_container_width=True)




separator = st.container(border=False)
separator.write("---")




col_e, col_m, col_d, col_r = st.columns(4)

with col_e:
    dif_1 = st.button("Easy", on_click=set_easy, disabled=st.session_state.easy_but_disabled, use_container_width=True)

with col_m:
    dif_2 = st.button("Moderate", on_click=set_moderate, disabled=st.session_state.moderate_but_disabled, use_container_width=True)

with col_d:
    dif_3 = st.button("Difficult", on_click=set_difficult, disabled=st.session_state.diff_but_disabled, use_container_width=True)

with col_r:
    reset_button = st.button("Reset Game", on_click=reset, disabled=st.session_state.reset_but_disabled, use_container_width=True)




if st.session_state.hearts_counter == 0:
    disable_all_but()
    disabled=st.session_state.reset_but_disabled = False


st.html('<div class="instructions"> <h3>How to play:</h3> <br><br> To start, pick a difficulty: "Easy", "Moderate", or "Difficult" <br><br> Click the "Play Word" button to hear the word you are supposed to spell <br><br> For guidance, use the "Play Definition" button to hear the definition of the word <br><br> Type in the word you hear in the input box, then press the large "Check Spelling" button <br><br> <br> For each correct word, 1 is added to the "Correct Words" counter <br><br> For each incorrect word, 1 life will be taken away. You have 3 lives <br><br> You will not hear the same word again if you get it wrong <br><br> To play again, click the "Reset Game" button</div>')


if not st.session_state.audio_file == '':
    audio = open(st.session_state.audio_file, "rb").read()

    duration = get_audio_duration(st.session_state.audio_file)

    st.audio(audio, format = "audtio/mp3", autoplay=True)
    st.html('<div class="cover"> &nbsp; </div>')

    time.sleep(duration)
    st.session_state.audio_file = ''
    st.rerun()