from copart_data_fetching import Car
from myauto_entering_data import MyautoAnalytics

car = Car('58236974')
car.show_data()

MyautoAnalytics(car).go_to_search_page()








