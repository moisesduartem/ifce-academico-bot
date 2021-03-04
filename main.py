from selenium import webdriver

from login import login
from boletim import get_boletim

browser = webdriver.Chrome('/usr/local/bin/chromedriver')

def go_to_boletim(browser, callback = lambda browser : None):
    link_boletim = browser.find_element_by_xpath("//a[text()='Boletim']")
    link_boletim.click()
    callback(browser)

login(browser, lambda browser :
    go_to_boletim(browser, lambda browser :
        get_boletim(browser, lambda browser :
            browser.quit()
        )
    )
)