from django.shortcuts import render

from selenium import webdriver
import time


target_url = 'https://auto.ru/catalog/cars/all/'

def get_source_html(target_url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(url=target_url)
        time.sleep(10)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    return driver.page_source


print(get_source_html(target_url))
