#Finds teh Torvik ranking for each team

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

def torvik_scrape(ncaa):
	
	torvik = pd.DataFrame()

	url = 'https://www.barttorvik.com/trank.php#'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	teams = soup.find_all(attrs = {'class' : 'teamname'})
	
	ranks_array = []
	teams_array = []
	
	x = 1
	for team in teams:
		teams_text = team.get_text().split('(')[0].strip()
		teams_array.append(teams_text)
		ranks_array.append(x)
		x = x + 1

	torvik['Teams'] = teams_array
	torvik['TORVIK Ranks'] = ranks_array

	mapping_dict = {
	'North Carolina St.': 'N.C. State',
	'College of Charleston': 'Charleston',
	'Louisiana Lafayette': 'Louisiana',
	'Detroit': 'Detroit Mercy',
	'LIU Brooklyn': 'LIU',
	'Fort Wayne': 'Purdue Fort Wayne'
	}

	torvik = torvik.replace({'Teams': mapping_dict})

	ncaa = pd.merge(left = ncaa, right = torvik, how = 'left', on = 'Teams')
	
	return ncaa

