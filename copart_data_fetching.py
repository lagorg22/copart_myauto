from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.expected_conditions import element_attribute_to_include
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from rand_proxies import RandomProxy
import time

class Car:
    def __init__(self, url: str):
        self.url = url
        self.lot = None
        self.vin = None
        self.title = None
        self.drive = None
        self.color = None
        self.vehicle = None
        self.keys = None
        self.highlights = None
        self.primary = None
        self.estimated = None
        self.brand = None
        self.model = None
        self.year = None
        self.odometer = None
        self.cylinders = None
        self.body = None
        self.engine = None
        self.transmission = None
        self.fuel = None
        self.driver: webdriver
        self.__init_web_driver()

    def __init_web_driver(self):
        edge_driver_path = "/home/lasha/Desktop/copart_myauto_integration/msedgedriver"
        edge_service = Service(executable_path=edge_driver_path)

        # proxy = RandomProxy().get_random_proxy()
        edge_options = Options()
        edge_options.add_experimental_option('detach', True)
        # edge_options.add_argument(f'--proxy-server={proxy}')

        self.driver = webdriver.Edge(service=edge_service, options=edge_options)

    def __get_website(self):
        self.driver.get(self.url)
        while True:
            try:
                time.sleep(3)
                WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="top"]/div[1]/div/div[2]/div/div[1]/div[1]/div/div/a/img')))
                break
            except (NoSuchElementException, TimeoutException):
                self.driver.refresh()


    def __fill_attributes(self):
        descriptions_xpath = '/html/body/div[3]/div[3]/div/app-root/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/label'
        values_xpath = '/html/body/div[3]/div[3]/div/app-root/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/span'
        elements_all = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, descriptions_xpath)))
        all_values = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, values_xpath)))
        values_txt = [elem.text for elem in all_values]
        descriptions_txt = [elem.text for elem in elements_all]
        curr_len = min(len(values_txt), len(descriptions_txt))
        for i in range(curr_len):
            self.__setattr__(descriptions_txt[i].split()[0].lower().rstrip(':'), values_txt[i])

    def __fetch_data(self):
        self.__get_website()
        self.__fill_attributes()

    def show_data(self):
        self.__fetch_data()
        self.driver.close()
        print(f'odometer: {self.odometer}\n'
              f'cylinders: {self.cylinders}\n'
              f'body_style: {self.body}\n'
              f'engine: {self.engine}\n'
              f'transmission: {self.transmission}\n'
              f'fuel: {self.fuel}')





