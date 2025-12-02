import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator
from playsound import playsound
import uuid
import os

def record_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Speak now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except:
        print("❌ Could not understand speech.")
        return None

def text_to_speech(text, lang):
    try:
        tts = gTTS(text, lang=lang)
        filename = f"{uuid.uuid4()}.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except:
        print("❌ Audio generation error.")

def translate_speech(target_lang, lang_name):
    text = record_voice()
    if text:
        try:
            translated = GoogleTranslator(source="en", target=target_lang).translate(text)
            print(f"🌐 {lang_name}: {translated}")
            text_to_speech(translated, target_lang)
        except:
            print("❌ Translation failed.")

def main_menu():
    while True:
        print("\n" + "="*50)
        print("🌍  MULTI-LANGUAGE VOICE TRANSLATOR")
        print("="*50)
        print("1️⃣  English → Hindi")
        print("2️⃣  English → Telugu")
        print("3️⃣  English → Tamil")
        print("4️⃣  English → Kannada")
        print("5️⃣  English → French")
        print("6️⃣  English → Spanish")
        print("7️⃣  Exit / Quit")
        print("="*50)

        choice = input("👉 Enter your choice (1–7): ")

        if choice == "1":
            translate_speech("hi", "Hindi")
        elif choice == "2":
            translate_speech("te", "Telugu")
        elif choice == "3":
            translate_speech("ta", "Tamil")
        elif choice == "4":
            translate_speech("kn", "Kannada")
        elif choice == "5":
            translate_speech("fr", "French")
        elif choice == "6":
            translate_speech("es", "Spanish")
        elif choice == "7":
            print("\n👋 Exiting program... Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Try again.")

main_menu()
