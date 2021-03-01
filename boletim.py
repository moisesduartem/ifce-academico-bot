def boletim(browser, callback = lambda: None) -> None:
    link_boletim = browser.find_element_by_xpath("//a[text()='Boletim']")
    link_boletim.click()

    callback(browser)