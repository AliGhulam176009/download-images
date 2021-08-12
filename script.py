from selenium import webdriver    # install selenium by "pip install selenium" in terminal
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup   # for Beautifulsoap (pip install Beautiful Soap)
import requests
import os
import pandas as pd
from urllib3 import request

def getSoup(driver): #for getting soup of current window

    "returns a Bs4-soup instance of the current window"

    return BeautifulSoup(driver.execute_script('return document.documentElement.outerHTML'), 'html.parser')

def chromeDriver(): # This function is for opening chromeDriver

    options = Options()

    options.add_argument("--disable-extensions")

    # options.add_argument("--headless") # Runs Chrome in headless mode.

    # options.add_argument('--no-sandbox') # Bypass OS security model

    # options.add_argument('--disable-gpu')  # applicable to win	dows os only

    # options.add_argument('start-maximized') # start maximize

    # options.add_argument('disable-infobars')

    driver = webdriver.Chrome(options=options)

    return driver

#dictionary for saving scraped details

data = {
#    'title' : [],
#    'price' : [],
    'image_url' : []
}


def scraping(soup): # This function will get all required data

#    title1 = soup.find('h1', class_='a-size-large a-spacing-none')

#    title = title1.find('span', class_ = 'a-size-large product-title-word-break')


    try:

        image1 = soup.find('div', class_ = 'imgTagWrapper')


        image = image1.find('img')['src']

 #   data['title'].append(title)

  #  data['price'].append(price)

        data['image_url'].append(image)

        return image


    except Exception as e:
        #print(e)
        pass
def main(): # This is main function which will do all the things for collecting required info

    driver = chromeDriver()
#    driver.get(url)

#    soup = getSoup(driver)
    data = pd.read_excel ('New Mubarak sheet.xlsx',  sheet_name='USA PRODUCTS')

    urllist=list(data['Product link/ASIN'])
    deslist=list(data['Description'])

    #url=urllist[0]
    #print(len(urllist))


    for i in range(len(urllist)):
        print(i)
        try:
            url=urllist[i]
            driver.get(url)
            soup = getSoup(driver)

	#print(url)
            link = scraping(soup)
            imagename=deslist[i]+".jpg"


            with open(imagename, 'wb') as f:
                img = requests.get(link)
                f.write(img.content)
        except Exception as e:
        #print(e)
            pass




#    imagename=deslist[0]
 #   with open(imagename, 'wb') as f:

#        img = requests.get(link)
#
#        f.write(img.content)
main()
