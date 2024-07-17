from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from GenericScrapper import GenericScrapper

if __name__ == "__main__":
    scraper = GenericScrapper("https://mx.aliexpress.com")

    #Cerra el pop-up
    selector = (getattr(By, "CLASS_NAME"), "pop-close-btn")
    scraper.perform_action(selector, "click")

    #Buscar el input de busqueda
    selector = (getattr(By, "ID"), "search-words")
    scraper.perform_action(selector, "input", "Relojes")

    #Buscar el boton de busqueda
    selector = (getattr(By, "CLASS_NAME"), "search--submit--2VTbd-T")
    scraper.perform_action(selector, "click")

