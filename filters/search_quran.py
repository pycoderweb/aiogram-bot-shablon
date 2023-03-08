import requests

def quran_uzb(sura,oyat,url_uz):
    r = requests.get(url_uz).json()
    for quran in r["quran"]:
       if quran['chapter'] == sura and quran['verse'] == oyat:
           return str(quran['text'])

