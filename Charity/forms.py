from Charity import main
import requests
import sys, json
from flask_wtf import FlaskForm
from wtforms import SelectField

# def locate_charity():

api_key = main.read_from_file("JSON/API_Info.json")
api_id = main.read_from_file("JSON/API_Info.json")
url = "https://api.data.charitynavigator.org/v2/Organizations?app_id=" + api_id['id'] + "&app_key=" + api_key['key']
request_json = requests.get(url).json()

main.save_to_file(request_json, "JSON/charity_api.json")
Charity_api = main.read_from_file("JSON/charity_api.json")


address
charity_name
rating