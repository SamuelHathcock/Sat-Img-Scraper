from bs4 import BeautifulSoup
import urllib.request
import requests
import os

def makeSrc(date, satellite, product, time, zoomlevel, row_column):
    src = '/data/imagery' + date + satellite + product + time + zoomlevel + row_column
    return src

def request_image(name, date, satellite, product, time, zoomlevel, row_column):
    resourceLink = base_url + makeSrc(date, satellite, product, time, zoomlevel, row_column)
    urllib.request.urlretrieve(resourceLink, name)

base_url = 'https://rammb-slider.cira.colostate.edu'
productlist = ['eumetsat_ash', 'geocolor']

#2021 03 12 2330 17
year = '2021'
month = '03'
day = '12'
hour = '2330'
second = '17'

date = '/' + year + month + day
satellite = '/' + 'goes-16---full_disk'
product = '/' + productlist[1]
time = '/' + year + month + day + hour + second
zoomlevel = '/' + '04'
row_column = '/' + '003_002.png'

print('https://rammb-slider.cira.colostate.edu/data/imagery/20210312/goes-16---full_disk/geocolor/20210312233017/04/002_002.png')
print(base_url + makeSrc(date, satellite, product, time, zoomlevel, row_column) + '\n')

selected_imageID = 'test_img.jpg'
request_image(selected_imageID, date, satellite, product, time, zoomlevel, row_column)
os.system('display ' + selected_imageID)
