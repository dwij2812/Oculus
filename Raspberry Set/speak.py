

# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
import numpy as np
import requests
import time
import shutil
while True:
    response = requests.get('http://192.168.43.209:8080/text.npy', stream=True)
    with open('haha.npy', 'wb') as fin:
        shutil.copyfileobj(response.raw, fin)

    k=np.load('haha.npy') # Works!
    print(k)
    data=k.astype(str)
    print(str(data))
    # This module is imported so that we can  
    # play the converted audio 
    import os 
      
    # The text that you want to convert to audio 
    mytext = 'The boy is running and 2 cars are approaching towards you'
      
    # Language in which you want to convert 
    language = 'en'
      
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=str(data), lang=language, slow=False) 
      
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3") 
      
    # Playing the converted file 
    os.system("omxplayer welcome.mp3")
    time.sleep(5)

