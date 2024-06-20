import speech_recognition as sr

def listen(timeout=10):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=timeout)
            return r.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("Timeout error: No speech detected within the timeout period.")
            return ""
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Example usage
while True:
    command = listen().lower()
    if command == "":
        continue  # Handle empty command
    elif "hello" in command:
        print("Hello! How can I assist you?")
    elif "goodbye" in command or "bye" in command:
        print("Goodbye!")
        break
    else:
        print("Sorry, I didn't understand that command.")