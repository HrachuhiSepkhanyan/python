from turtle import title
import xmltodict, json
import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg


response = requests.get("https://www.nytimes.com/services/xml/rss/nyt/World.xml")
print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
items = soup.select("item ")
print(items)

for item in items:

    titles = soup.select("item > title")
    print(titles)
    links=soup.select("item > link")
    
    
sg.Window(title="World", layout=[[sg.Text("there will be title of  general news")]], margins=(100, 50)).read()