import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

'''
This module has two function 
1) englishtofrench(text)
2) frenchtoenglish(text)

These function translate the given text using IBM watson
language translator

'''
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

translator_instance = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator_instance.set_service_url(url)

def englishtofrench(englishtext):
    '''
    Function Converts Enlgish Text to French
    '''
    #write the code here
    if englishtext is None:
        return None
    frenchtext = translator_instance.translate(text=englishtext,
    model_id='en-fr').get_result()
    frenchtext = frenchtext['translations'][0]['translation']
    return frenchtext

def frenchtoenglish(frenchtext):
    '''
    Function Converts French Text to Engligh
    '''
    #write the code here
    if frenchtext is None:
        return None
    englishtext = translator_instance.translate(text=frenchtext,
    model_id='fr-en').get_result()
    englishtext = englishtext['translations'][0]['translation']
    return englishtext
