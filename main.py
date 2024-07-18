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

    #Seleccionar los productos
    while True:
        selector = getattr(By, "CLASS_NAME")
        products = scraper.perform_action(selector, "select", "multi--titleText--nXeOvyr")

        selector = getattr(By, "CLASS_NAME")
        scraper.perform_action(selector, "scroll", "lazy-load")
        print("Scrolling...")

        #Verificar si siguen elementos sin cargar
        selector = getattr(By, "CLASS_NAME")
        lazy = scraper.perform_action(selector, "select", "lazy-load")
        print("Lazy elements: ", len(lazy))

        #cuando llegue al final de la pagina se rompe el ciclo
        if len(lazy) == 0:
            break
           

    for product in products:
        print(product.text)
