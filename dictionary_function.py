from bs4 import BeautifulSoup
import requests

def diction(word):
    url = 'http://m.dictionary.com/definition/'
    soup = BeautifulSoup(requests.get(url+word).content)
    snippet = soup.findAll('div',{'class':'result'})
    print snippet[0]
    print snippet[1]

