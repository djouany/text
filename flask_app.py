
import pandas as pd
import numpy as np
import pickle

from flask import Flask, request
from bs4 import BeautifulSoup
import string
import regex as re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer


tokenizer = RegexpTokenizer(r'\w+')
stop = stopwords.words('english')
stemmer = SnowballStemmer("english")

my_dict = {'c#':'csharp',
           'c\+\+':'cpplus',
           '\.net':'dotnet',
           'd3\.js':'d3js',
           'sql\-server' : 'sqlserver',
           'visual-studio': 'visualstudio',
           'vb\.net': 'vbnet',
           'ruby\-on\-rails': 'rubyonrails',
           'language\-agnostic': 'languageagnostic',
           r"\bc\b": 'langc'
       }


# Suppression des balises html
def balises(text):
    text = BeautifulSoup(text).get_text()
    return text

# Minuscule
def minuscule(text):
        text = text.lower()
        return text

# Premiere suppression des stopwords
def remove_stop(text, stop_list):
    text = text.split()
    result  = [word for word in text if word not in stop_list]
    result = ' '.join(result)
    return result

# Gestion des noms particuliers
def keep_dico(text, dico):
    for k, v in dico.items():
        text = text.replace(k, v)
    return text

# Suppression de la ponctuation
def remove_punc(text):
    token = tokenizer.tokenize(text)
    sentence = " ".join(token)
    return sentence

# Suppression des mots d'un seul caractère
def remove_short(text):
    text = ' '.join(word for word in text.split() if len(word)>1)
    return text

# Stemming
def stemming(value):
    words = value.split(' ')
    liste = []
    mystring = []
    for word in words:
        word = stemmer.stem(word)
        liste.append(word)
    mystring = " ".join(liste)
    return(mystring)


app = Flask(__name__)
@app.route('/text', methods=['POST'])
def text ():
    value = request.get_json(force=True)
    texte = str(value["texte"])
    result = balises(texte)
    result = minuscule(result)
    result = remove_stop(result, stop)
    result = keep_dico(result, my_dict)
    result = remove_punc(result)
    result = remove_short(result)
    result = stemming(result)
    print(result)
    
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)