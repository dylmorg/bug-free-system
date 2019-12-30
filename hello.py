from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
content = driver.get("https://www.mtggoldfish.com/archetype/pioneer-izzet-phoenix#paper")
aaah = driver.page_source
onlineButton = driver.find_elements_by_xpath()
onlineButton.click()
soup = BeautifulSoup(aaah, 'html.parser')
products = []
prices = [] 
ratings = []
for tr in (soup.find_all('tr')):

    for b in (tr.find_all(attrs={'class':'deck-col-card'}) ):
        for a in(b.findAll('a')):
            print(a.text)
    for b in (tr.find_all(attrs={'class':'deck-col-price'}) ):
            print(b.text)