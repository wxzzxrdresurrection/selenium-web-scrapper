from selenium.webdriver.common.by import By
from GenericScrapper import GenericScrapper
from JsonParser import JsonParser

if __name__ == "__main__":

    data = JsonParser("aliexpress.json").get_config()

    scraper = GenericScrapper(data["url"])

    actions = data["actions"]

    for action in actions:
        selector = (getattr(By, action["selector_type"]), action["selector_value"])
        scraper.perform_action(selector, action["action_type"], action["value"])
