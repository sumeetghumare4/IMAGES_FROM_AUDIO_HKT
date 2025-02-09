import time, os, getpass
import logging
import streamlit as st
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
from PIL import Image
from settings import RESOURCES_DIR, IMAGE_DIR, DURATION, WAVE_OUTPUT_FILE, IMAGE_OUPUT_FILE
from src.sound import sound
from src.transcript import get_text_from_audio
from src.imagine import save_image_from_prompt

##setup_logging()
logger = logging.getLogger('app')

def main():
    title = "Room Interior from Audio"
    st.set_page_config(page_title=title,page_icon=None, layout='centered')
    st.title(title)
    image = Image.open(os.path.join(RESOURCES_DIR, 'furniture.jpg'))
    st.image(image, use_column_width=True)

    if st.button('Record'):
        with st.spinner(f'Recording for {DURATION} seconds ....'):
            sound.record()
        st.success("Recording completed")

    if st.button('Play'):
        # sound.play()
        try:
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except:
            st.write("Please record sound first")

def takeCommand():
    """

    Takes microphone input from server
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please..")
        return "None"
    return query



    if st.button('Get images from file'):
      text_from_audio = get_text_from_audio(WAVE_OUTPUT_FILE)
      print("$$$"+text_from_audio)
      save_image_from_prompt(text_from_audio)
      st.subheader("Text: "+text_from_audio)
      st.write("Output Image")
      output_image=image = Image.open(IMAGE_OUPUT_FILE)

      st.image(output_image, use_column_width=True)
      
      #TODO: This will be consumed and diaplayed by fronted

if __name__ == '__main__':
    main()