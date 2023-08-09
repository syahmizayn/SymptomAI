import os
import openai
from gtts import gTTS
import streamlit as st
from IPython.display import Audio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Symptom Analysis AI
def symptom_analysis_ai(symptoms):
    prompt = f"Patient presents the following symptoms: {symptoms}. Analyze and provide a possible diagnosis, recommended tests, and treatment options."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        top_p=0.98,
        frequency_penalty=0.2,
        presence_penalty=0.2
    )

    analysis = response.choices[0].text.strip()
    return analysis

# Generate speech using gTTS
def generate_speech(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)

# Streamlit UI
def main():
    st.title("🏥🏥🏥Symptom Analysis AI with Speech Generator🏥🏥🏥")

    patient_symptoms = st.text_input("Enter patient symptoms:")
    if st.button("Analyze Symptoms"):
        if patient_symptoms:
            analysis_result = symptom_analysis_ai(patient_symptoms)
            st.write("Analysis Result:")
            st.write(analysis_result)

            output_file = "analysis_speech.mp3"
            generate_speech(analysis_result, output_file)

            st.audio(output_file, format="audio/mp3")

if __name__ == "__main__":
    main()
