from dbm import error

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urllib.parse import urlparse, parse_qs
import time
from copart_data_fetching import Car
from constants import *


class MyautoAnalytics:
    def __init__(self, car: Car):
        self.car = car
        self.mans_n_models = None
        self.prices: list[int] = []
        self.driver: webdriver = None
        self.__init_web_driver()

    def __init_web_driver(self):
        edge_driver_path = DRIVER_PATH
        edge_service = Service(executable_path=edge_driver_path)
        edge_options = Options()
        # edge_options.add_argument('--headless')
        # edge_options.add_argument('--disable-gpu')
        edge_options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(service=edge_service, options=edge_options)

        self.driver.get('https://www.myauto.ge/en/')
    
    def __set_brand(self):
        brand_dropdown = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, BRAND_DROPDOWN_XPATH)))
        self.driver.execute_script('arguments[0].click();', brand_dropdown)
        brand_input_field = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, BRAND_INPUT_XPATH)))
        brand_input_field.send_keys(self.car.brand)
        first_brand_suggestion = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, FIRST_BRAND_SUGGESTION_XPATH))
        )
        self.driver.execute_script("arguments[0].click();", first_brand_suggestion)
        
    def __set_model(self):
        model_dropdown = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, MODEL_DROPDOWN_XPATH)))
        self.driver.execute_script('arguments[0].click();', model_dropdown)
        model_input_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, MODEL_INPUT_XPATH)))
        time.sleep(3)
        model = self.car.model
        while True:
            try:
                model_input_field.clear()
                model_input_field.send_keys(model)
                WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.XPATH, MODEL_NOT_FOUND_XPATH)))
                model = model[:-1]
            except(TimeoutException, NoSuchElementException):
                try:
                    model_search_dropdown = WebDriverWait(self.driver, 1).until(ec.element_to_be_clickable((By.XPATH, MODEL_SEARCHED_DROPDOWN_XPATH)))
                    self.driver.execute_script('arguments[0].click();', model_search_dropdown)
                    model_dropdown_first = WebDriverWait(self.driver, 1).until(ec.element_to_be_clickable((By.XPATH, MODEL_DROPDOWN_FIRST_XPATH)))
                    self.driver.execute_script('arguments[0].click();', model_dropdown_first)
                    break
                except(TimeoutException, NoSuchElementException):
                    model_first_suggestion = WebDriverWait(self.driver, 1).until(ec.element_to_be_clickable((By.XPATH, MODEL_FIRST_SUGGESTION_XPATH)))
                    self.driver.execute_script('arguments[0].click();', model_first_suggestion)
                    break


    def __search(self):
        search_btn = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, SEARCH_MYAUTO_XPATH)))
        self.driver.execute_script('arguments[0].click();', search_btn)

    def __get_mans_n_models(self):
        self.__set_brand()
        self.__set_model()
        self.__search()

        url = self.driver.current_url
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        self.mans_n_models = query_params.get('mansNModels', [None])[0]

    def __get_prices(self):
        prices = WebDriverWait(self.driver, 12).until(ec.presence_of_all_elements_located((By.XPATH, PRICES_XPATH)))
        prices = [int(num.text.replace(',', '')) for num in prices if  8 >= len(num.text) >= 5]
        self.prices += prices

    def go_to_search_page(self):
        self.__get_mans_n_models()

        page_num = 1
        while True:
            new_url = (f'{STANDARD_URL_START}mansNModels={self.mans_n_models}&locations={LOCATIONS}&y'
                       f'earFrom={self.car.year}&yearTo={self.car.year}&'
                       f'engineFrom={self.car.engine_type}&'
                       f'engineTo={self.car.engine_type}&'
                       f'currId=1&mileageType=1&fuelTypes={FUEL_TYPES[self.car.fuel]}{f'.{OTHER_FUEL_TYPES}' if self.car.fuel is not 'not_specified' else ''}&'
                       f'gearTypes={GEARBOX_TYPES[self.car.transmission]}&driveTypes={DRIVE_WHEELS[self.car.drive]}&'
                       f'page={page_num}&layoutId=1')
            self.driver.get(new_url)
            try:
                self.__get_prices()
            except (NoSuchElementException, TimeoutException):
                break
            finally:
                page_num += 1

        self.driver.close()

    def calculate(self):
        self.go_to_search_page()
        mean_value = int(sum(self.prices)/len(self.prices))
        min_value = min(self.prices)
        max_value = max(self.prices)
        count = len(self.prices)
        return {
            'Researched cars count': count,
            'Mean Price': mean_value,
            'Min Price': min_value,
            'Max Price': max_value
        }