from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

edge_driver_path = "/home/lasha/Desktop/copart_myauto_integration/msedgedriver"
edge_service = Service(executable_path=edge_driver_path)

edge_options = Options()
edge_options.add_experimental_option('detach', True)

driver = webdriver.Edge(service=edge_service, options=edge_options)

car_site = 'https://www.copart.com/lot/59198554/salvage-2011-bmw-328-i-nb-moncton'

# driver.get(car_site)
def get_info():
    time.sleep(3)
    lot_num = WebDriverWait(driver, 7).until(ec.presence_of_element_located((By.XPATH, '//*[@id="LotNumber"]')))
    print(lot_num.text)


while True:
    driver.get(car_site)
    try:
        get_info()
        break
    except (NoSuchElementException, TimeoutException):
        driver.refresh()
        print('refreshed')








# driver.quit()