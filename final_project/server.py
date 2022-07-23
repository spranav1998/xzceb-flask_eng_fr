from machinetranslation import translator
from flask import Flask, render_template, request
import json
import sys

sys.path.append('/home/project/xzceb-flask_eng_fr/final_project/machinetranslation/')

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frenchtext = translator.englishtofrench(textToTranslate)
    return frenchtext

@app.route("/frenchToEnglish")
def frenchtoenglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    englishtext = translator.frenchtoenglish(textToTranslate)
    return englishtext

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
