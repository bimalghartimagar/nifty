""" Main flask module for running flask application """

from flask import Flask, request, render_template
from src.run_scrape import run
import json
import os
from src.utils.config import get_config
from src.utils import utility
from src.dao import db

app = Flask(__name__)
env_type = os.environ.get('ENV_TYPE', 'dev')


@app.route('/')
def index():
    remote_ip = request.remote_addr
    environment = get_config()
    print(remote_ip)

    args = {
        'remote_ip': remote_ip,
        'environment': environment
    }

    return render_template('index.html', **args)


@app.route('/forex', methods=['GET', 'POST'])
def forex():
    args = {}
    bank_list = db.get_bank_list()
    if request.method == 'GET':
        args.update({'bank_list': bank_list})
        return render_template('forex.html', bank_list=bank_list)
    elif request.method == 'POST':
        rates = run(request.form.getlist('banks'))
        rates_with_diff = utility.calc_diff(rates)
        args.update({'bank_list': bank_list})
        args.update({'rates': rates_with_diff})
        return render_template('forex-result.html', **args)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
