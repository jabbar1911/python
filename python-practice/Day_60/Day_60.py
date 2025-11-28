import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator
from playsound import playsound
import uuid
import os

print("\n" + "-"*30)
print("🎙️  Voice Translator – English → Telugu 🌐")
print("-"*30 + "\n")

def listen_and_translate():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🗣️  Speak something in English...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # Step 1: Convert speech to text
        text = r.recognize_google(audio)
        print(f"✅ You said: {text}")

        # Step 2: Translate to Telugu
        translated = GoogleTranslator(source='auto', target='te').translate(text)
        print(f"🌐 Translated (Telugu): {translated}")

        # Step 3: Convert translated text to speech
        tts = gTTS(translated, lang='te')
        filename = f"voice_{uuid.uuid4()}.mp3"
        tts.save(filename)

        # Step 4: Play the translated audio
        print("🔊 Playing translated audio...")
        playsound(filename)

        # Step 5: Clean up file
        os.remove(filename)

    except sr.UnknownValueError:
        print("❌ Could not understand your speech.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    listen_and_translate()
    print("\n" + "-"*30 + "\n")