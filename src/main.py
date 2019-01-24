from flask import Flask, request, render_template
from run_scrape import run
import json
import os
from utils.config import get_config
from dao import db

app = Flask(__name__)
env_type = os.environ.get('ENV_TYPE', 'dev')


@app.route('/')
def index():
    remote_ip = request.remote_addr
    environment = get_config(env_type)
    print(remote_ip)
    return render_template('index.html', remote_ip=remote_ip, environment=environment)

@app.route('/forex', methods=['GET', 'POST'])
def forex():
    bank_list = db.get_bank_list()
    if request.method == 'GET':        
        return render_template('forex.html', bank_list=bank_list)
    elif request.method == 'POST':
        rates = run(request.form.getlist('banks'))
        return render_template('forex-result.html', bank_list=bank_list, rates=rates)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8000)