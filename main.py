from copart_data_fetching import Car
from myauto_entering_data import MyautoAnalytics

car = Car('67001474')
car.show_data()

MyautoAnalytics(car).calculate()








