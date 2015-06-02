#!/usr/bin/python

import requests, json

def get_contacts(group_name):

	elvanto_url = "https://api.elvanto.com/v1/groups/getAll.json"

	data = { 'fields' : ['people'] }
	headers = {'Content-type': 'application/json'}

	r = requests.post(elvanto_url, data=json.dumps(data), auth=('***REMOVED***', 'x'), headers=headers).json()

	contacts = {}

	for i in r['groups']['group']:
		if i['name'] == group_name + ' Parents':			
			for y in i['people']['person']:
				tuple = {}
				tuple['firstname'] = y['firstname']
				tuple['email'] = y['email']
				tuple['group'] = [group_name]
				contacts[y['id']] = tuple
				
	return contacts

def get_parents_list(groups):
	parents = {}

	for group in groups:
		parents = update_parent_list(group, parents)

	return parents

def update_parent_list(group, parents):

	contacts = get_contacts(group)

	for uid,contact in contacts.items():
		if uid in parents:
			parents[uid]['group'].extend(contact['group'])
		else:
			parents[uid] = contact

	return parents



