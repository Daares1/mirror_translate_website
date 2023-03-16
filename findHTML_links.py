#Script used to fink links in the website
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def findHTML_links(strwebpage):
    ser = Service('./chromedriver_linux64')
    driver = webdriver.Chrome(service=ser)
    driver.get(strwebpage)
    links = driver.find_elements(by=By.TAG_NAME,value="a")
    str_links = []
    for link in links:
        str_links.append(link.get_attribute("href"))
    driver.quit()
    return str_links
