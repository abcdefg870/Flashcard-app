import streamlit as st
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

st.title("Flashcard Generator")

st.write("Enter a passage of text, and this app will create flashcards for you!")

# Text input box
text = st.text_area("Enter your text here:")

if st.button("Generate Flashcards"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        doc = nlp(text)
        flashcards = []

        # Use named entities as answers
        for ent in doc.ents:
            question = f"What is {ent.label_} related to '{ent.text}'?"
            answer = ent.text
            flashcards.append((question, answer))

        if len(flashcards) == 0:
            st.info("No entities found to make flashcards. Try longer or different text.")
        else:
            st.success("Here are your flashcards:")
            for q, a in flashcards:
                st.write(f"**Q:** {q}")
                st.write(f"**A:** {a}")
                st.write("---")

