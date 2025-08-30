import streamlit as st
import spacy
import subprocess
import sys

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

st.title("Flashcards Generator")

text = st.text_area("Enter some text to generate flashcards:")

if text:
    doc = nlp(text)
    # Extract keywords (nouns, proper nouns)
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]

    if keywords:
        st.subheader("Flashcards")
        for i, word in enumerate(set(keywords), start=1):
            with st.expander(f"Flashcard {i}"):
                st.write(f"**Word:** {word}")
                st.write("(You can write your own definition/answer here)")
    else:
        st.info("No keywords found. Try entering a longer text!")
