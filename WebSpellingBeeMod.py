import streamlit as st
import pyttsx3
import random
import threading
import pathlib
from streamlit_TTS import text_to_speech


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


# MAKING SURE BUTTONS CAN'T BE CLICKED AT THE SAME TIME


def disable_all_but():
    st.session_state.play_but_disabled = True
    st.session_state.check_but_disabled = True
    st.session_state.def_but_disabled = True
    st.session_state.reset_but_disabled = True

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



def say_word(word):

    # speaker = pyttsx3.init()
    # speaker.say(f'{word}')
    # speaker.runAndWait()

    text_to_speech(text=word, language='en')
    
    # if speaker._inLoop:
    #     speaker.endLoop()


def audio_button_clicked():
    
    #disable_all_but()
    #threading.Thread(target=say_word, args=(st.session_state.word_list[st.session_state.current_word],)).start()

    say_word(st.session_state.word_list[st.session_state.current_word])

    enable_all_but()
    st.session_state.correct_output = 2


def defs_button_clicked():

    #disable_all_but()
    #threading.Thread(target=say_word, args=(st.session_state.defs_list[st.session_state.current_word],)).start()

    say_word(st.session_state.defs_list[st.session_state.current_word])
        
    

def check_spelling():
    
    if entry_word == "":
        return

    if entry_word == st.session_state.word_list[st.session_state.current_word]:
        st.session_state.correct_output = 1
        st.session_state.correct_no = st.session_state.correct_no + 1

    else:
        st.session_state.correct_output = 0
        st.session_state.hearts_counter = st.session_state.hearts_counter - 1

    if st.session_state.hearts_counter == 0:
        game_over()


    st.session_state.current_word = random.randint(1, 300)



def set_easy():
    st.session_state.word_list = st.session_state.word_list1
    st.session_state.defs_list = st.session_state.defs_list1
    st.session_state.easy_but_disabled = False
    st.session_state.moderate_but_disabled = True
    st.session_state.diff_but_disabled = True
    st.session_state.play_but_disabled = False
    st.session_state.reset_but_disabled = False

def set_moderate():
    st.session_state.word_list = st.session_state.word_list2
    st.session_state.defs_list = st.session_state.defs_list2
    st.session_state.easy_but_disabled = True
    st.session_state.moderate_but_disabled = False
    st.session_state.diff_but_disabled = True
    st.session_state.play_but_disabled = False
    st.session_state.reset_but_disabled = False

def set_difficult():
    st.session_state.word_list = st.session_state.word_list3
    st.session_state.defs_list = st.session_state.defs_list3
    st.session_state.easy_but_disabled = True
    st.session_state.moderate_but_disabled = True
    st.session_state.diff_but_disabled = False
    st.session_state.play_but_disabled = False
    st.session_state.reset_but_disabled = False



def reset():
    st.session_state.hearts_counter = 3
    st.session_state.correct_no = 0
    st.session_state.easy_but_disabled = False
    st.session_state.moderate_but_disabled = False
    st.session_state.diff_but_disabled = False
    disable_all_but()
    st.session_state.correct_output = 2



# THE UI


st.html(f'<p class="title"> BuzzWords </p>')



col_h, col_s = st.columns([4, 1])

with col_h:
    #st.write(f'Lives: {heart_emoji()}')
    st.html(f'<p class="lives"> Lives: {heart_emoji()} </p>')

with col_s:
    st.html(f'<p class="alignright"> Correct Words: {st.session_state.correct_no} </p>')




col_du1, col_cor, col_du2 = st.columns(3)

with col_du1:
    st.write("")

with col_cor:
    if st.session_state.correct_output == 0:
       st.html('<p class="incorrect"> Incorrect! </p>')

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
    audio_button = st.button("Play word", on_click=audio_button_clicked, disabled=st.session_state.play_but_disabled, use_container_width=True)
    defs_button = st.button("Play definition", on_click=defs_button_clicked, disabled=st.session_state.def_but_disabled, use_container_width=True)




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
    reset_button = st.button("Reset the Game", on_click=reset, disabled=st.session_state.reset_but_disabled, use_container_width=True)




if st.session_state.hearts_counter == 0:
    disable_all_but()
    disabled=st.session_state.reset_but_disabled = False


