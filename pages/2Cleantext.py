from textblob import TextBlob
import streamlit as st

st.header('Spelling Correction')

def correct_spelling(sentence):
    # Use TextBlob to correct spelling mistakes
    corrected_sentence = TextBlob(sentence).correct()
    return corrected_sentence

def main():
    input_text = st.text_input('Enter Text: ')

    if input_text:
        corrected_text = correct_spelling(input_text)
        st.write('Corrected Text:', corrected_text)

if __name__ == "__main__":
    main()
