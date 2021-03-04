from bs4 import BeautifulSoup
import pandas as pd
import json
import inspect
from utils import table_to_dict, parse_tbody

def get_boletim(browser, callback = lambda browser : None) -> None:

    element = browser.find_element_by_xpath("//table [@width='97%'] [@border='0'] [@cellspacing='1'] [@cellpadding='1'] [@align='center'] [@style='margin-top: -15px; margin-bottom: 15px;']")
    html_content = element.get_attribute("outerHTML")


    soup = BeautifulSoup(html_content, "html.parser")

    table_body = parse_tbody(soup.find("tbody"))
    table_body.pop(0)
    table_head = table_body[0]
    table_body.pop(0)

    boletim = table_to_dict(table_head, table_body)

    with open("boletim.json", "w", encoding="utf8") as outfile:
        json.dump(boletim, outfile, indent=4, ensure_ascii=False)

    callback(browser)
