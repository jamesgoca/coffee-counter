import requests
import json
import datetime
import os
import jinja2

def get_data():
	token = "keyFiaoGoLBiymZB7"
	
	auth = { "Authorization": "Bearer {}".format(token) }

	attributes = requests.get('https://api.airtable.com/v0/appoPJiqsrQ3BSRto/Coffees?view=All%20Brews', headers=auth)

	attributes_as_json = attributes.json()

	return attributes_as_json

def create_page(data):
	with open('template.html') as file_:
	    template = jinja2.Template(file_.read())

	today = datetime.datetime.today()

	today_formatted = today.strftime("%A %B %d, %Y")

	today_coffees = []

	coffees_today = len(today_coffees)

	for d in data["records"]:
		if d["fields"]["Date"] == today.strftime("%Y-%d-%m"):
			today_coffees.append(d)

	final = template.render(coffees=data["records"], today=today_formatted, coffees_today=coffees_today)

	with open("index.html", "w+") as index_page:
		index_page.write(final)

data = get_data()

create_page(data)
