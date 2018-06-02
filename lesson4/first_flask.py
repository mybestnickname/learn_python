from flask import Flask, request, render_template, abort, redirect, url_for
import requests
from req_settings import my_api
import random

app = Flask(__name__)


@app.route('/names')
def show_names(year=2018):
    try:
        year = int(request.args.get('year'))
    except Exception:
        pass
    url = 'http://api.data.mos.ru/v1/datasets/2009/rows?api_key={}'.format(
        my_api)
    year_names_ls = get_names(url, year)
    if not year_names_ls:
        # abort(404)
        return '<h2>Данные за {} год не найдены. :(</h2>'.format(year)
    return render_template('names.html', year=year, names_lst=year_names_ls)


@app.route('/')
def default_page():
    # клааасс)) тут когда я сделал ошибку, куда редиректить
    # дебагер сам подсказал имена функций.
    return redirect(url_for('show_names'))


def get_names(url, year):
    """
    Функция отдаёт список словарей вида
    {
        'Year': 2017, 'Name': 'Мариам\n',
        'Month': 'декабрь', 'global_id': 850999989,
        'NumberOfPersons': 6
    }
    """
    result = requests.get(url)
    if not result.status_code == 200:
        return False
    else:
        req_lst = result.json()
        year_names_lst = []
        for item in req_lst:
            if item['Cells']['Year'] == year:
                year_names_lst.append(item['Cells'])
        return year_names_lst


if __name__ == '__main__':
    try:
        app.run(port=5000 + random.randint(1, 50), debug=True)
    except Exception:
        app.run(port=5000 + random.randint(51, 101), debug=True)
