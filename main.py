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

    ignore_options = {
        'engine_type': request.form.get('ignore_engine') == '1',
        'transmission': request.form.get('ignore_transmission') == '1',
        'drive': request.form.get('ignore_drive') == '1',
        'fuel': request.form.get('ignore_fuel') == '1'
    }

    car = Car(lot_num, ignore_options)
    try:
        data = MyautoAnalytics(car).calculate()
    except ZeroDivisionError:
        data = {'There were no such cars found on Myauto': 'Try ignoring some specs.'}

    return render_template('index.html', data=data, car_details=car.get_details())


if __name__ == '__main__':
    app.run(debug=True)












