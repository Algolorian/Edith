import os
import random
import time
import webbrowser
from time import ctime
import pyautogui
from playsound import playsound  # pip install playsound==1.2.2
import pytesseract as tess
import speech_recognition as sr  # pip install SpeechRecognition
from gtts import gTTS


tess.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# voice engines
'''
online engines:
Microsoft Bing speech
recognize_bing()
Google web speech API
recognize_google()
Google cloud speech
recognize_google_cloud()
Houndify
recognize_houndify()
IBM speech to text
recognize_ibm()
Wit.AI
recognize_wit()

offline engines:
CMU Sphinx
recognize_sphinx()
'''

r = sr.Recognizer()
activate_term = 'Edith'
user_name = 'Timothy'
directory = 'D:\\Pycharm_Database\\Edith_Directory\\'
image_library = directory + 'Image_library\\'


#######################################################################
# SUB FUNCTIONS
#######################################################################


def click(grid):
    mouse = pyautogui.position(grid)
    pyautogui.click(grid)
    pyautogui.moveTo(mouse)


#######################################################################
# MAJOR FUNCTIONS
#######################################################################


def record_audio():
    global voice_data
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('''Sorry, I didn't get that''')
        except sr.RequestError:
            speak('''Sorry, my speech service is down''')
        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    rand = random.randint(1, 100000)
    audio_file = 'audio-' + str(rand) + '.mp3'
    # audio_file = 'audio-' + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)


def respond(respond_voice_data):
    if 'search' in respond_voice_data:
        search(respond_voice_data)
    elif 'start' in respond_voice_data:
        start(respond_voice_data)
    elif 'close' in respond_voice_data:
        close(respond_voice_data)
    elif 'what' in respond_voice_data:
        what(respond_voice_data)
    elif 'security' in respond_voice_data:
        security(respond_voice_data)
    elif 'execute' in respond_voice_data:
        execute(respond_voice_data)
    else:
        custom(respond_voice_data)


#######################################################################
# INPUT TYPES
#######################################################################


def search(voice_input):
    # web browsers
    if 'search Google for' in voice_input:
        search_point = voice_input.find('search') + 18
        url = 'https://google.com/search?q=' + voice_input[search_point:]
        webbrowser.get().open(url)
        speak('''here is what google found''')
    if 'search YouTube for' in voice_input:
        search_point = voice_input.find('search') + 19
        url = 'https://www.youtube.com/results?search_query=' + voice_input[search_point:]
        webbrowser.get().open(url)
    if 'search Bing for' in voice_input:
        search_point = voice_input.find('search') + 16
        url = 'https://www.bing.com/search?q=' + voice_input[search_point:]
        webbrowser.get().open(url)
        speak('''here is what Bing found''')
    if 'search tour for' in voice_input:
        search_point = voice_input.find('search') + 15
        term = voice_input[search_point:]
        os.system('''start C:\\Users\\tim3i\\Documents\\"Tor Browser"\\Browser\\firefox.exe''')
        time.sleep(4)
        pyautogui.click(230, 250)
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'e')
        pyautogui.write(term)
        pyautogui.press('enter')
        speak('''here is what Tor found''')
    if 'search DuckDuckGo for' in voice_input:
        search_point = voice_input.find('search') + 22
        url = 'https://duckduckgo.com/?=' + voice_input[search_point:] + '&va=b&t=hc&ia=web'
        webbrowser.get().open(url)
        speak('''here is what DuckDuckGo found''')
    if 'search location' in voice_input:
        search_point = voice_input.find('search location') + 16
        url = 'https://google.nl/maps/place/' + voice_input[search_point:] + '/&amp;'
        webbrowser.get().open(url)
        speak('''here is what google found''')
    # files
    if 'search documents for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write('documents')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search downloads for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('downloads')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search desktop for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('desktop')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search music for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('music')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search pictures for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('pictures')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search videos for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('videos')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search OneDrive for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('OneDrive')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search Dropbox for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('Dropbox')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search OS for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('C:')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search drive for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('D:')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search computer for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('This PC')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')
    if 'search external drive for' in voice_input:
        search_point = voice_input.find('for') + 4
        term = voice_input[search_point:]
        print(term)
        pyautogui.hotkey('win', 'e')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)
        pyautogui.write('E:')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write(term)
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here you go')


def start(voice_input):
    if 'notepad plus plus' in voice_input:
        pyautogui.press('win')
        time.sleep(0.1)
        pyautogui.write('notepad++')
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('here it is')
    else:
        search_point = voice_input.find('start') + 6
        search_term = voice_input[search_point:]
        pyautogui.press('win')
        time.sleep(0.1)
        pyautogui.write(search_term)
        time.sleep(0.2)
        pyautogui.press('enter')
        speak('here it is')


def close(voice_input):
    global directory, images
    if 'close app' in voice_input:
        pyautogui.hotkey('alt', 'f4')


def what(voice_input):
    if 'your name' in voice_input:
        speak('My name is Edith')
    if 'time is it' in voice_input:
        speak(ctime())
    if 'your favorite color' in voice_input:
        speak('I think periwinkle is pretty')
    if 'your favorite job' in voice_input:
        speak('I like security scanning')
    if 'you like to do' in voice_input:
        speak('wait for you to call me')
    if 'my name' in voice_input:
        speak('You should know your name, its ' + str(user_name))
    if 'do you know' in voice_input:
        speak('only what you programmed me to know')
    if 'your favorite game' in voice_input:
        speak('I do good at piano tiles')
    if 'can you do' in voice_input:
        speak('I have a list of operations involving searching the web, searching for files, '
              'starting and closing applications, security scanning, executing your programs, '
              'and some simple questions like this one.')
    if 'are you' in voice_input:
        speak('I am a simple robot programmed by Timothy Macfarlane using pythons '
              'online speech recognition module accompanied by Google web speech API')


def security(voice_input):
    if 'run smart scan' in voice_input:
        pyautogui.press('win')
        time.sleep(0.1)
        pyautogui.write('avast')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(519, 386)
        time.sleep(1)
        pyautogui.click(687, 362)
        time.sleep(0.75)
        pyautogui.click(730, 425)
        time.sleep(0.75)
        pyautogui.hotkey('alt', 'f4')
        speak('scanning now')
    elif 'status' in voice_input:
        pyautogui.press('win')
        time.sleep(0.1)
        pyautogui.write('avast')
        time.sleep(0.1)
        pyautogui.press('enter')
        speak('displaying security status')
    elif 'records' in voice_input:
        pyautogui.hotkey('win', 'r')
        time.sleep(0.1)
        pyautogui.write('C:\\ProgramData\\Avast Software\\Avast\\report')
        pyautogui.press('enter')
        speak('Here are the security records')


def execute(voice_input):
    if 'chess bot' in voice_input:
        pyautogui.hotkey('win', 'r')
        time.sleep(0.1)
        pyautogui.write('C:\\Users\\tim3i\\Desktop\\Typhon.exe')
        pyautogui.press('enter')
        speak('chess bot executed')
    if 'Mouse XY' in voice_input:
        pyautogui.hotkey('win', 'r')
        time.sleep(0.1)
        pyautogui.write('C:\\Users\\tim3i\\Desktop\\Mouse_XY.exe')
        pyautogui.press('enter')
        speak('Mouse X Y executed')


def custom(voice_input):
    global term_required
    if 'deactivate term' in voice_input:
        term_required = True
        speak("I'm listening")
    if 'activate term' in voice_input:
        term_required = False
        speak("Term now required")
    if 'spell' in voice_input:
        search_point = voice_input.find('spell') + 6
        spell_term = voice_input[search_point:]
        for i in range(len(spell_term)):
            speak(spell_term[i])
    if 'go to sleep' in voice_input:
        speak('''ok, good night''')
        exit(10)
    if 'repeat after me' in voice_input:
        search_point = voice_input.find('repeat after me') + 16
        speak_term = voice_input[search_point:]
        speak(speak_term)
    if 'Edith' == voice_input:
        speak('Yes ' + str(user_name))
    if 'read the screen' in voice_input:
        pic = pyautogui.screenshot(region=(0, 100, 1920, 940))
        speak('screen captured')
        speak('processing capture')
        text = tess.image_to_string(pic)
        speak(text)


os.system('title Edith Voice Assistant')
speak('I am Edith, How can I help you ' + str(user_name))
term_required = True
while True:
    time.sleep(0.25)
    voice_data = record_audio()
    print(voice_data)
    if term_required:
        if activate_term in voice_data:
            print('  -- ', voice_data, ' --')
            respond(voice_data)
    else:
        print('  -- ', voice_data, ' --')
        respond(voice_data)
