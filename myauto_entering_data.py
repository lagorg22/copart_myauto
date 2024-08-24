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
from urllib.parse import urlparse, parse_qs
import time



edge_driver_path = "/home/lasha/Desktop/copart_myauto_integration/msedgedriver"
edge_service = Service(executable_path=edge_driver_path)

# proxy = RandomProxy().get_random_proxy()
edge_options = Options()
edge_options.add_experimental_option('detach', True)
# edge_options.add_argument(f'--proxy-server={proxy}')

driver = webdriver.Edge(service=edge_service, options=edge_options)

driver.get('https://www.myauto.ge/en/')

#////////////////////////////////manufacturer///////////////////////////////////////////////////////

dropdown_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div'

man_dropdown = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, dropdown_xpath)))

driver.execute_script('arguments[0].click();', man_dropdown)

input_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/input'

input_field = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, input_xpath)))

input_field.send_keys('toyota')

first_suggestion_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[1]/label/span'
time.sleep(3)
first_suggestion = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.XPATH, first_suggestion_xpath))
)
driver.execute_script("arguments[0].click();", first_suggestion)

#////////////////////////////////model////////////////////////////////////

dropdown_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div'

man_dropdown = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, dropdown_xpath)))

driver.execute_script('arguments[0].click();', man_dropdown)

input_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/input'

input_field = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, input_xpath)))

input_field.send_keys('rav4')

first_suggestion_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/label/span'
time.sleep(3)
first_suggestion = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.XPATH, first_suggestion_xpath))
)
driver.execute_script("arguments[0].click();", first_suggestion)


search_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[9]/button'

search_btn = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, search_xpath)))

driver.execute_script('arguments[0].click();', search_btn)

#...///////////////////////////////////////
url = driver.current_url

parsed_url = urlparse(url)

query_params = parse_qs(parsed_url.query)

mans_n_models = query_params.get('mansNModels', [None])[0]

#...///////////////////////////////////////

fuel = 'Hybrid Engine'

fuel_types = {
    'GAS' : '2',
    'Diesel': '3',
    'Electric': '7',
    'Hybrid Engine': '6.10',
}

gearbox = 'Automatic'

gearbox_types = {
    'Automatic': '2.3.4',
    'Manual': '1'
}

drive_wheel = 'all wheel drive'

drive_wheels = {
    '4x4 w/front whl drv': '3',
    '4x4 w/rear whl drv': '3',
    'all wheel drive': '3',
    'four by four': '3',
    'front-wheel drive': '1',
    'rear-wheel drive': '2'
}

OTHER_FUEL_TYPES = '9.8.12'
year = '2020'
engine = '2.5'


new_url = f'https://www.myauto.ge/en/s/for-sell-cars-{year}-{year}?vehicleType=0&bargainType=0&mansNModels={mans_n_models}&yearFrom={year}&yearTo={year}&engineFrom={engine}&engineTo={engine}&currId=1&mileageType=1&fuelTypes={fuel_types[fuel]}.{OTHER_FUEL_TYPES}&gearTypes={gearbox_types[gearbox]}&driveTypes={drive_wheels[drive_wheel]}&page=&layoutId=1'

driver.get(new_url)