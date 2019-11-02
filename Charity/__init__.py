from flask import Flask

app = Flask(__name__)

app.config['KEY'] = 'charity'

from Charity import routes