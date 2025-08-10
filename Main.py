import os
import webbrowser
import speech_recognition as sr
import win32com.client
from transformers import pipeline

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Rate = -2
    speaker.Speak("\u200B" + text)

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")
            return ""

legal_context = """
Section 420 of the Indian Penal Code (IPC) states that anyone who cheats and dishonestly induces another person to deliver any property shall be punished with imprisonment up to 7 years and a fine. 
Example: If someone sells a fake product as real gold, it falls under Section 420.

Section 41 of the Code of Criminal Procedure (CrPC) allows police to arrest a person without a warrant under certain circumstances, like committing a cognizable offense or being a repeat offender.
Example: If someone is caught stealing in a store, police can arrest without a warrant.

An FIR (First Information Report) is a written document prepared by the police when they receive information about a cognizable offense. It marks the beginning of the investigation process.
Example: If someone is assaulted, the victim or witness can file an FIR at the police station.
"""

# Text generation model for detailed answers
text_gen = pipeline("text2text-generation", model="google/flan-t5-base")

def is_legal_question(question: str) -> bool:
    """Check if the question is legal-related with enhanced keyword matching."""
    legal_keywords = [
        "section", "act", "law", "legal", "ipc", "article", "constitution", "penal",
        "rights", "duty", "court", "crime", "criminal", "civil", "suit", "offence",
        "offense", "trial", "judge", "judgment", "justice", "bail", "warrant", "arrest",
        "contract", "tort", "property", "liability", "penalty", "clause",
        "code of criminal procedure", "evidence", "procedure", "appeal", "jurisdiction",
        "tribunal", "bar council", "advocate", "litigation", "enactment", "rule",
        "regulation", "verdict", "plaintiff", "defendant", "writ", "habeas corpus",
        "fundamental rights", "directive principles", "preamble", "murder"
    ]
    return any(word.lower() in question.lower() for word in legal_keywords)

def generate_detailed_answer(question):
    prompt = f"Answer this legal question in detail with examples: {question}\nContext: {legal_context}"
    result = text_gen(prompt, max_new_tokens=200)[0]["generated_text"]
    print("Answer:", result)
    say(result)


def handle_basic_commands(query):
    if "open youtube" in query:
        say("Opening YouTube.")
        webbrowser.open("https://youtube.com")
        return True
    elif "open wikipedia" in query:
        say("Opening Wikipedia.")
        webbrowser.open("https://wikipedia.org")
        return True
    elif "exit" in query or "stop" in query:
        say("Okay Cyril, exiting ArguLex. Have a great day!")
        exit()
    return False

if __name__ == "__main__":
    say("Hello Cyril, ArguLex voice assistant is now active and ready to answer your legal questions.")
    
    while True:
        query = take_command()

        if not query:
            say("Sorry, I didn't catch that. Please repeat.")
            continue

        if not handle_basic_commands(query):
            if is_legal_question(query):
                generate_detailed_answer(query)
            else:
                say("Sorry, I can only answer questions related to legal terms and law.")
