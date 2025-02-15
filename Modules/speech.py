# import pyttsx3  

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Set voice properties (optional)
# engine.setProperty('rate', 150)  # Speed of speech (words per minute)
# engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# # Text to speak
# text = "Hello! Welcome to Python text-to-speech."

# # Speak the text
# engine.say(text)

# # Wait for the speech to finish
# engine.runAndWait()
import pyttsx3
engine = pyttsx3.init()
engine.say("python is fun")
engine.runAndWait()
