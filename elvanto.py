#!/usr/bin/python

import requests, json

def get_contacts(group_name):

	elvanto_url = "https://api.elvanto.com/v1/groups/getAll.json"

	data = { 'fields' : ['people'] }
	headers = {'Content-type': 'application/json'}

	r = requests.post(elvanto_url, data=json.dumps(data), auth=('diybrM8IDRsafNybg2Fixj9M7agNY7H1', 'x'), headers=headers).json()

	contacts = []

	for i in r['groups']['group']:
		if i['name'] == group_name + ' Parents':			
			for y in i['people']['person']:
				tuple = {}
				tuple['firstname'] = y['firstname']
				tuple['email'] = y['email']
				contacts.append(tuple)
				
	return contacts


