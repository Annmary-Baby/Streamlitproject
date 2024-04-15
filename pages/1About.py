import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def show_about_page():
    st.title('About')
    st.write('Welcome to the About Page!')
    
    st.header('Text Extraction from Image')
    st.write('This project involves extracting text from images using Optical Character Recognition (OCR) techniques. Users can upload an image containing text, and the app will extract the text from the image and display it below.')
   
    
    st.header('Text Cleaner')
    st.write('This module generates cleaned text from the input we give.Means if we input some wrong words it will almost correct the word according to the pattern the word is in.')
  
    
    st.header('Text Analysis')
    st.write('The text analysis module provides various analysis tools for paragraphs or texts. It includes generating word clouds, analyzing word frequencies, and visualizing data through graphs.')
    
   

if __name__ == '__main__':
    show_about_page()
