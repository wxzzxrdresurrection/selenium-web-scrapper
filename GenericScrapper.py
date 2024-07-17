from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        element = wait.until(EC.element_to_be_clickable(element_selector))

        if action_type == 'click':
            element.click()
        elif action_type == 'input' and value:
            element.send_keys(value)
        elif action_type == 'scroll':
            target = self.driver.find_element(By.CLASS_NAME, "element_selector")
            delta_y = target.rect["y"]
            delta_y = int(delta_y)
            time.sleep(1)
            ActionChains(self.driver)\
                    .scroll_by_amount(0, delta_y)\
                    .perform()
        else:
            raise ValueError('Acción no soportada')
        
        time.sleep(5)

    def select_elements(self, element_selector):
        return self.driver.find_elements(*element_selector)

    def get_data(self):
        return self.data
    
    def close(self):
        self.driver.quit()