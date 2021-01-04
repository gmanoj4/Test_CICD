software’s to be installed:

Anaconda 3
conda install -c conda-forge/label/cf201901 speechrecognition
conda install -c anaconda pyaudio
pip install goslate

libraries used :

speech recognition
goslate
BeautifulSoup
html.parser"
Regex

Implementation:

The code will take voice from user any language(now only Hindi/English)and translate to English. 
Translated test will go and search for response from given URL (now it is google)
The response from google will be scraped.
And with html parser it will be parsed, parsed list will be converted to string.
The regex  will be applied on converted string to extract HS-CODE
Finally HS-Code will Displayed.
