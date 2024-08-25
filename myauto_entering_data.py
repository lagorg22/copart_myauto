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
import constants


class MyautoAnalytics:
    def __init__(self, car: Car):
        self.car = car
        self.mans_n_models = None
        self.prices: list[int] = []
        self.driver: webdriver = None
        self.__init_web_driver()

    def __init_web_driver(self):
        edge_driver_path = "/home/lasha/Desktop/copart_myauto_integration/msedgedriver"
        edge_service = Service(executable_path=edge_driver_path)

        # proxy = RandomProxy().get_random_proxy()
        edge_options = Options()
        edge_options.add_experimental_option('detach', True)
        # edge_options.add_argument(f'--proxy-server={proxy}')

        self.driver = webdriver.Edge(service=edge_service, options=edge_options)

        self.driver.get('https://www.myauto.ge/en/')
    
    def __set_brand(self):
        time.sleep(7)
        brand_dropdown_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div'
        brand_dropdown = WebDriverWait(self.driver, 13).until(
            ec.element_to_be_clickable((By.XPATH, brand_dropdown_xpath)))
        self.driver.execute_script('arguments[0].click();', brand_dropdown)
        brand_input_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/input'
        brand_input_field = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, brand_input_xpath)))
        brand_input_field.send_keys(self.car.brand)
        first_brand_suggestion_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[1]/label/span'
        time.sleep(3)
        first_brand_suggestion = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, first_brand_suggestion_xpath))
        )
        self.driver.execute_script("arguments[0].click();", first_brand_suggestion)
        
    def __set_model(self):
        model_dropdown_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div'

        model_dropdown = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, model_dropdown_xpath)))

        self.driver.execute_script('arguments[0].click();', model_dropdown)

        model_input_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/input'
        model_input_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, model_input_xpath)))
        time.sleep(3)
        model = self.car.model
        while True:
            try:
                model_input_field.clear()
                model_input_field.send_keys(model)

                first_model_suggestion_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/label/span'
                time.sleep(3)
                first_model_suggestion = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, first_model_suggestion_xpath))
                )
                self.driver.execute_script("arguments[0].click();", first_model_suggestion)
                break
            except (TimeoutException, NoSuchElementException):
                model = ' '.join(model.split()[:-1])

    def __search(self):
        search_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[9]/button'
        search_btn = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, search_xpath)))
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
        price_xpath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div/div/div[1]/p'
        prices = WebDriverWait(self.driver, 12).until(ec.presence_of_all_elements_located((By.XPATH, price_xpath)))
        prices = [int(num.text.replace(',', '')) for num in prices if len(num.text) >= 5]
        self.prices += prices
    def go_to_search_page(self):
        self.__get_mans_n_models()
        # new_url = f'https://www.myauto.ge/en/s/for-sell-cars?vehicleType=0&bargainType=0&mansNModels={self.mans_n_models}&locations=2.3.4.7.15.30.113.52.37.48.47.44.41.31.40.39.38.36.53.54.16.14.13.12.11.10.9.8.6.5.55.56.57.59.58.61.62.63.64.66.71.72.74.75.76.77.78.80.81.82.83.84.85.86.87.88.91.96.97.101.109.116.119.122.127.131.133&yearFrom={self.car.year}&yearTo={self.car.year}&engineFrom={self.car.engine_type}&engineTo={self.car.engine_type}&currId=1&mileageType=1&fuelTypes={constants.FUEL_TYPES[self.car.fuel]}.{constants.OTHER_FUEL_TYPES}&gearTypes={constants.GEARBOX_TYPES[self.car.transmission]}&driveTypes={constants.DRIVE_WHEELS[self.car.drive]}&page=&layoutId=1'



        page_num = 1
        while True:
            new_url = f'https://www.myauto.ge/en/s/for-sell-cars?vehicleType=0&bargainType=0&mansNModels={self.mans_n_models}&locations=2.3.4.7.15.30.113.52.37.48.47.44.41.31.40.39.38.36.53.54.16.14.13.12.11.10.9.8.6.5.55.56.57.59.58.61.62.63.64.66.71.72.74.75.76.77.78.80.81.82.83.84.85.86.87.88.91.96.97.101.109.116.119.122.127.131.133&yearFrom={self.car.year}&yearTo={self.car.year}&engineFrom={self.car.engine_type}&engineTo={self.car.engine_type}&currId=1&mileageType=1&fuelTypes={constants.FUEL_TYPES[self.car.fuel]}.{constants.OTHER_FUEL_TYPES}&gearTypes={constants.GEARBOX_TYPES[self.car.transmission]}&driveTypes={constants.DRIVE_WHEELS[self.car.drive]}&page={page_num}&layoutId=1'
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
        mean = int(sum(self.prices)/len(self.prices))
        print(f'Mean Price: {mean}\n'
                f'Min Price: {min(self.prices)}\n'
                f'Max Price: {max(self.prices)}')