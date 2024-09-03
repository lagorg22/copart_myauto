FUEL_TYPES = {
    'flexible fuel': '2',
    'gas' : '2',
    'diesel': '3',
    'electric': '7',
    'hybrid engine': '6.10',
    'Not Specified': ''
}

GEARBOX_TYPES = {
    'automatic': '2.3.4',
    'manual': '1',
    'Not Specified': ''
}

DRIVE_WHEELS = {
    '4x4 w/front whl drv': '3',
    '4x4 w/rear whl drv': '3',
    'all wheel drive': '3',
    'four by four': '3',
    'front-wheel drive': '1',
    'rear-wheel drive': '2',
    'Not Specified': ''
}

OTHER_FUEL_TYPES = '9.8.12'
DESCRIPTIONS_XPATH = '/html/body/div[3]/div[3]/div/app-root/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/label'
VALUES_XPATH = '/html/body/div[3]/div[3]/div/app-root/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/span'
YEAR_BRAND_MODEL_XPATH = '/html/body/div[3]/div[3]/div/app-root/div[1]/div[1]/div/div[1]/div/div/div/div/div/div/h1'

DESCRIPTIONS_XPATH_GR_YE = '/html/body/div[3]/div[3]/div/app-root/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/vehicle-information-component/div[2]/div/label'
VALUES_XPATH_GR_YE = '/html/body/div[3]/div[3]/div/app-root/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/vehicle-information-component/div[2]/div/span'
YEAR_BRAND_MODEL_XPATH_GR_YE = '/html/body/div[3]/div[3]/div/app-root/div[1]/div[1]/div/div[1]/div/lot-details-header-component/div/div[1]/div/h1'

GREEN_YELLOW_LIGHT_XPATH = '/html/body/div[3]/div[3]/div/app-root/div[1]/div[1]/div/div[1]/div/lot-details-header-component/div/div[1]/div/div/div/div[1]/span[1]/span/span[1]'

DRIVER_PATH = '/home/lasha/Desktop/all/copart_myauto_integration/msedgedriver'

BRAND_DROPDOWN_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div'
BRAND_INPUT_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/input'
FIRST_BRAND_SUGGESTION_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[1]/label/span'

MODEL_DROPDOWN_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div'
MODEL_INPUT_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/input'
MODEL_SEARCHED_DROPDOWN_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/span'
MODEL_DROPDOWN_FIRST_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/label/span'
MODEL_NOT_FOUND_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/p'
MODEL_FIRST_SUGGESTION_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/label/span'

SEARCH_MYAUTO_XPATH = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div[9]/button'

PRICES_XPATH = '/html/body/div[2]/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/div/div/div[1]/p'

LOCATIONS = ('2.3.4.7.15.30.113.52.37.48.47.44.41.31.40.39.38.36.53.54.16.14.13.12.11.10.9.8.6.5.55.56.57.59.58.61.62.63'
             '.64.66.71.72.74.75.76.77.78.80.81.82.83.84.85.86.87.88.91.96.97.101.109.116.119.122.127.131.133')
STANDARD_URL_START = 'https://www.myauto.ge/en/s/for-sell-cars?vehicleType=0&bargainType=0&'

