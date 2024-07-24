from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from GenericScrapper import GenericScrapper

if __name__ == "__main__":
    scraper = GenericScrapper("https://www.mercadolibre.com.mx/")

    #Buscar el input de busqueda
    selector = (getattr(By, "CSS_SELECTOR"), "input.nav-search-input")
    scraper.perform_action(selector, "input", "Consolas")

    #Buscar el boton de busqueda
    selector = (getattr(By, "CLASS_NAME"), "nav-search-btn")
    scraper.perform_action(selector, "click")

    selector = getattr(By, "CLASS_NAME")
    products = scraper.perform_action(selector, "select", "ui-search-item__title")


    # Almacena los datos en un data frame
    table_data = []
    for product in products:
        table_data.append([product.text])

    # Crea un DataFrame con los datos de la tabla
    df = pd.DataFrame(table_data, columns=["Producto"])
    df.to_excel("ml.xlsx")

