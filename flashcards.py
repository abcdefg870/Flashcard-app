import streamlit as st
from transformers import pipeline

# Load NLP model
qg = pipeline("question-generation")

st.title("AI Flashcard Generator")
st.write("Paste your text below and get flashcards!")

# Input text
text = st.text_area("Enter your study material here:")

if st.button("Generate Flashcards"):
    if text.strip():
        flashcards = qg(text)
        st.subheader("Your Flashcards:")
        for i, card in enumerate(flashcards, 1):
            with st.expander(f"Flashcard {i} (Click to see Answer)"):
                st.write("**Q:**", card['question'])
                st.write("**A:**", card['answer'])
    else:
        st.warning("Please enter some text!")
