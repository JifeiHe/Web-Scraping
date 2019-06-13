#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re
import urllib
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas.core.frame import DataFrame
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options



df = pd.read_csv("Headquarter Update2.csv")
df.head()


def find_headquarter(LinkedinPage):
    driver.get(LinkedinPage)
    driver.implicitly_wait(3)
    try:
        elem = driver.find_elements_by_class_name("org-top-card-summary__headquarter")[0].text
        #return elem
    except (NoSuchElementException, IndexError):
        try:
            driver.find_element_by_id("ember32")
            elem = "No headquarter"
        except:
            elem = "Oops"
    return elem


driver = webdriver.Chrome()
driver.get('https://www.linkedin.com')



for i, page in enumerate(df["LinkedIn Company Page"]):
    df["0 - Global Headquarter"].iloc[i]=find_headquarter(page)


df.to_excel("Headquarter_updated2.xlsx",index=False)
