from bs4 import BeautifulSoup
import urllib.request
import requests



def request_image(name, day, satellite, product, time, zoomlevel, row_column):
    baseURL = 'https://rammb-slider.cira.colostate.edu'
    src = '/data/imagery' + day + satellite + product + time + zoomlevel + row_column
    resourceLink = baseURL + src
    
    urllib.request.urlretrieve(resourceLink, name)
