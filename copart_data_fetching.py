from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import constants
import time

class Car:
    def __init__(self, lot_number: str):
        self.lot_number = lot_number
        self.drive = None
        self.color = None
        self.keys = None
        self.estimated_retail_value = None
        self.brand = None
        self.model = None
        self.year = None
        self.odometer = None
        self.cylinders = None
        self.engine_type = None
        self.transmission = None
        self.fuel = None
        self.driver: webdriver
        self.__init_web_driver()
        self.__fetch_data()

    def __init_web_driver(self):
        edge_driver_path = constants.DRIVER_PATH
        edge_service = Service(executable_path=edge_driver_path)

        # proxy = RandomProxy().get_random_proxy()
        edge_options = Options()
        edge_options.add_experimental_option('detach', True)
        # edge_options.add_argument(f'--proxy-server={proxy}')

        self.driver = webdriver.Edge(service=edge_service, options=edge_options)

    def __get_website(self):
        self.driver.get(f'https://www.copart.com/lot/{self.lot_number}')
        while True:
            try:
                time.sleep(3)
                WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="top"]/div[1]/div/div[2]/div/div[1]/div[1]/div/div/a/img')))
                break
            except (NoSuchElementException, TimeoutException):
                self.driver.refresh()


    def __fill_attributes(self):
        descriptions_xpath = constants.DESCRIPTIONS_XPATH
        values_xpath = constants.VALUES_XPATH
        year_brand_model_xpath = constants.YEAR_BRAND_MODEL_XPATH
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, constants.GREEN_YELLOW_LIGHT_XPATH)))
            descriptions_xpath = constants.DESCRIPTIONS_XPATH_GR_YE
            values_xpath = constants.VALUES_XPATH_GR_YE
            year_brand_model_xpath = constants.YEAR_BRAND_MODEL_XPATH_GR_YE
        except (TimeoutException, NoSuchElementException):
            pass

        year_brand_model = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, year_brand_model_xpath)))
        year_brand_model = year_brand_model.text.split()

        self.year = year_brand_model[0].lower()
        self.brand = year_brand_model[1].lower()
        self.model = ' '.join(year_brand_model[2:]).lower()



        time.sleep(5) #temporary
        elements_all = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, descriptions_xpath)))
        time.sleep(5)#temporary
        all_values = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, values_xpath)))
        time.sleep(5)#temporary
        values_txt = [elem.text for elem in all_values]
        descriptions_txt = [elem.text for elem in elements_all]
        curr_len = min(len(values_txt), len(descriptions_txt))
        for i in range(curr_len):
            self.__setattr__(descriptions_txt[i].lower().replace(' ', '_').rstrip(':'), values_txt[i].lower())

        if self.engine_type:
            self.engine_type = self.engine_type.split()[0].replace('l', '')


    def __fetch_data(self):
        self.__get_website()
        self.__fill_attributes()
        self.driver.close()






