from bs4 import BeautifulSoup
import urllib.request
import requests

baseURL = 'https://rammb-slider.cira.colostate.edu'

def request_image(img_name, date, satellite, product, time, zoomlevel, row_column):
    src = '/data/imagery' + date + satellite + product + time + zoomlevel + row_column
    resourceLink = baseURL + src
    
    urllib.request.urlretrieve(resourceLink, img_name)

