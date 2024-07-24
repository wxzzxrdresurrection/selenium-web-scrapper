from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ScrollOrigin
import pandas as pd

import time

class GenericScrapper:
    def __init__(self,url):
        self.driver = webdriver.Chrome()
        self.data = []
        self.load_page(url=url)

    def load_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def perform_action(self, element_selector, action_type, value=None):
        wait = WebDriverWait(self.driver, 20)
        if action_type == 'click' or action_type == 'input':
            element = wait.until(EC.element_to_be_clickable(element_selector))
   
        if action_type == 'click':
            element.click()
        elif action_type == 'input' and value:
            element.send_keys(value)
        elif action_type == 'scroll':
            selector, val = element_selector
            target = self.driver.find_element(selector, val)
            scroll_origin = ScrollOrigin.from_element(target, 0, -50)
            ActionChains(self.driver)\
                .scroll_from_origin(scroll_origin, 0, 200)\
                .perform()
            time.sleep(2)
        elif action_type == 'select':
            self.select_elements(element_selector)
        elif action_type == 'excel':
            data = self.get_data()
            self.write_excel(data, value)
        else:
            raise ValueError('Acción no soportada')
        
        time.sleep(2)

    def select_elements(self, element_selector):
        selector, value = element_selector
        elements = self.driver.find_elements(selector, value)
        for el in elements:
            print(el.text)
            self.data.append(el)
        

    def get_data(self):
        return self.data
    
    def write_excel(self, data, filename='output.xlsx'):
        table_data = []
        for element in data:
            table_data.append([element.text])
        df = pd.DataFrame(table_data, columns=["Data"])
        df.to_excel(filename)
        
    
    def close(self):
        self.driver.quit()