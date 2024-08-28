from operator import index

from copart_data_fetching import Car
from myauto_entering_data import MyautoAnalytics
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', infos=[])

@app.route('/calculate', methods=['POST'])
def calculate():
    lot_num = request.form.get('lot_num')

    car = Car(lot_num)
    data = MyautoAnalytics(car).calculate()

    return render_template('index.html', data=data, car_details=car.get_details())


if __name__ == '__main__':
    app.run(debug=True)












