import xmltodict, json
import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg


response = requests.get("https://www.nytimes.com/services/xml/rss/nyt/Sports.xml")
print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
items = soup.select("item ")
print(items)

for item in items:

    titles = soup.select("item > title")
    links=soup.select("item > link")

    print(titles)
    print(links)

    
sg.Window(title="Sport", layout=[[sg.Text("There will be title of sport news")]], margins=(100, 50)).read()
