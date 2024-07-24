from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from GenericScrapper import GenericScrapper

if __name__ == "__main__":
    scraper = GenericScrapper("https://en.wikipedia.org/wiki/List_of_Game_of_the_Year_awards")

    # Espera a que la tabla esté presente
    selector = getattr(By, "CLASS_NAME")
    scraper.perform_action(selector, "select", "wikitable")
    
    # Encuentra todas las filas de la tabla
    selector = getattr(By, "TAG_NAME")
    rows = scraper.perform_action(selector, "select", "tr")

    # Almacena los datos de la tabla
    table_data = []

    for row in rows:
        # Encuentra todas las celdas de la fila (pueden ser td o th)
        cells = row.find_elements(By.XPATH, ".//td | .//th")
        row_data = [cell.text for cell in cells]
        table_data.append(row_data)
    
    # Crea un DataFrame con los datos de la tabla
    df = pd.DataFrame(table_data)
    df.to_excel("output.xlsx")

    # Imprime el DataFrame
    print(df)

    scraper.close()
