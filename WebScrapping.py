from bs4 import BeautifulSoup

import requests

url='https://en.wikipedia.org/wiki/Rose'

#we are sending the request to the url and taking the response
response=requests.get(url)
response

response.text

#parsing library - html.parser and second is lxml
soup=BeautifulSoup(response.text,"lxml")

print(soup)

for Alink in soup.find_all('a'):
  #print(Alink)
  print(Alink.get('href'))

for ptag in soup.find_all('p'):
  #print(ptag)
  #now second loop for ptag
  for btag in ptag.find_all('b'):
    print(btag.text)

#task: extract data of page scrape words make data frame from pandas visualise number of words according to their number of occurences

import pandas as pd
list1=[1,2,3,4]
list=[3,4,5,5]
df = pd.DataFrame([list,list1],columns=['age','value','name','marks'])

print(df)

import pandas as pd
list1=['Ajay',12,30]
list=['Vijay',14,50]
df = pd.DataFrame([list,list1],columns=['name','age','marks'])

print(df)

#numpy.random.ran
