from selenium import webdriver
from bs4 import BeautifulSoup

from login import login
from boletim import boletim

browser = webdriver.Chrome('/usr/local/bin/chromedriver')

login(browser, boletim)