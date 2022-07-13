#!/usr/bin/env python
# coding: utf-8


# Speech-to-Text Import.
import speech_recognition as sr
# Text-to-Speech Import.
import gtts
from playsound import playsound
# To remove the punctuation and upper case letters from the user's pre-made note.
import string

def prompter():
    
    """
    Prompts the cue word right next to the input word via text and sound.
    
    Raises
    ------
    UnknownValueError
        If no input has been detected by the system for more than 5 seconds.
    IndexError
        If the last word of the text has been entered.
    """
    
    users_note = """
                    New York is 3 hours ahead of California,
                    but it does not make California slow.
                    Someone graduated at the age of 22,
                    but waited 5 years before securing a good job!
                    Someone became a CEO at 25,
                    and died at 50.
                    While another became a CEO at 50,
                    and lived to 90 years.
                    Someone is still single,
                    while someone else got married.
                    Obama retires at 55,
                    but Trump starts at 70.
                    Charles Njonjo married at 52 and is now 96...his peers could have married at 25 and died at 50.
                    Absolutely everyone in this world works based on their Time Zone.
                    People around you might seem to go ahead of you,
                    some might seem to be behind you.
                    But everyone is running their own RACE, in their own TIME.
                    Don't envy them or mock them.
                    They are in their TIME ZONE, and you are in yours!
                    Life is about waiting for the right moment to act.
                    So, RELAX.
                    You are not LATE.
                    You are not EARLY.
                    You are very much ON TIME, and in your TIME ZONE Destiny set up for you.
                 """
    # Convert the string format of text into a list of strings.
    note_list = users_note.split()
    
    # Give user 5 attempts in total.
    for users_try in range(5):
        # Initialise the recognizer.
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                word_list = input('Forgot what you wanna say next? Type something: ').split()
                # Read the audio data from the default microphone, give user 5 seconds to respond.
                audio_data = r.record(source, duration = 5)
                print('Recognizing...')
                # Convert speech to text.
                text = r.recognize_google(audio_data)
                for word in word_list:
                    if word in note_list:
                        # Keep track of the user's position by allowing the system to search the text forward only.
                        note_list = note_list[note_list.index(word) + 1:]
                        # Remove punctuation and upper case letters for the system's output.
                        note_list = [''.join(letter.lower() for letter in word if letter not in string.punctuation) for word in note_list]
                        next_word = note_list[0]
                        print(next_word)
                        # Make request to Google to get synthesis.
                        tts = gtts.gTTS(next_word)
                        tts.save("word.mp3")
                        playsound("word.mp3")
                    else:
                        print('Sorry, try again')
                        tts2 = gtts.gTTS('Sorry, try again')
                        tts2.save("error.mp3")
                        playsound("error.mp3")
                print('\n')
                
            # When the user doesn't produce any response for more than 5 seconds.
            except sr.UnknownValueError: 
                print('Time limit exceeded, please try again')
                tts3 = gtts.gTTS('Time limit exceeded, please try again')
                tts3.save("exception1.mp3")
                playsound("exception1.mp3")
                print('\n')
            # When the user inputs the last word of his/her notes.
            except IndexError:
                print('This is the last word of the text, please try again')
                tts4 = gtts.gTTS('This is the last word of the text, please try again')
                tts4.save("exception2.mp3")
                playsound("exception2.mp3")
                print('\n')
        
    print('Thanks for using my teleprompter, bye')

prompter()


# Useful Links:
# https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
# https://www.thepythoncode.com/article/convert-text-to-speech-in-python
# https://www.techbeamers.com/python-multiline-string/
# https://stackoverflow.com/questions/17686809/how-to-find-word-next-to-a-word-in-python
# https://www.programcreek.com/python/example/107723/speech_recognition.UnknownValueError
# https://www.delftstack.com/howto/python/python-remove-punctuation-from-list/
# https://realpython.com/documenting-python-code/