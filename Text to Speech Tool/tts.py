from gtts import gTTS # Google TTS Plugin (1)
lan = 'en' # Language (2)
main = input("Stronkfish Brand TTS\n\nText: ") # User Input (3-4)
fn = input("File name: ")
speech = gTTS(text=main, lang=lan, slow=False) # TTS File Create & Save (5-7)
speech.save(f"{fn}.mp3")
print("Audio Saved.")