import pyttsx3
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Noman")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    while True:
        x = input("Enter what do you want to Speak (type 'q' to quit): ")
        if x.lower() == 'q':
            engine.say('Glad to help you ')
            engine.runAndWait()
            break

        # Speak the input text
        engine.say(x)
        engine.runAndWait()
