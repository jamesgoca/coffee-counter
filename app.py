import requests
import json
import datetime
import os
import jinja2

from dotenv import load_dotenv

load_dotenv()

def get_data():
	token = os.environ.get("token")
	
	auth = { "Authorization": "Bearer {}".format(token) }

	attributes = requests.get(os.environ.get("base"), headers=auth)

	attributes_as_json = attributes.json()

	return attributes_as_json

def create_page(data):
	with open("template.html") as file_:
	    template = jinja2.Template(file_.read())

	yesterday = datetime.datetime.today() - datetime.timedelta(days=1)

	day_before_yesterday = datetime.datetime.today() - datetime.timedelta(days=2)

	yesterday_formatted = yesterday.strftime("%A %B %d, %Y")

	yesterday_coffees = [d for d in data["records"] if d["fields"]["Date"] == yesterday.strftime("%Y-%m-%d")]

	coffees_yesterday = len(yesterday_coffees)

	at_home = [c for c in yesterday_coffees if c["fields"]["Coffee Shop"] == "Home"]

	at_home_count = len(at_home)

	coffees_day_before_yesterday = [d for d in data["records"] if d["fields"]["Date"] == day_before_yesterday.strftime("%Y-%m-%d")]

	coffees_day_before_yesterday_count = len(coffees_day_before_yesterday)

	final = template.render(
		coffees=data["records"],
		yesterday=yesterday_formatted,
		coffees_yesterday=coffees_yesterday,
		at_home_count=at_home_count,
		coffees_day_before_yesterday_count=coffees_day_before_yesterday_count
	)

	with open("index.html", "w+") as index_page:
		index_page.write(final)

data = get_data()

create_page(data)
