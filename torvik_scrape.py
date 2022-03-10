#Finds teh Torvik ranking for each team

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

def torvik_scrape(ncaa):
	
	#Creating torvik dataframe
	torvik = pd.DataFrame()

	#Scraping torvik to get all team names
	url = 'https://www.barttorvik.com/trank.php#'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	teams = soup.find_all(attrs = {'class' : 'teamname'})
	
	#Creating arrays
	ranks_array = []
	teams_array = []
	
	#Iterating through scraped data to get team text and assigning ranks
	x = 1
	for team in teams:
		teams_text = team.get_text().split('(')[0].strip()
		teams_text = teams_text.split('vs.')[0].strip()
		teams_array.append(teams_text)
		ranks_array.append(x)
		x = x + 1

	#print(teams_array)

	#Assigning values to torvik dataframe
	torvik['Teams'] = teams_array
	torvik['TORVIK Ranks'] = ranks_array


	#Creating dict to ensure all team names are the same before merging
	mapping_dict = {
	'North Carolina St.': 'N.C. State',
	'College of Charleston': 'Charleston',
	'Louisiana Lafayette': 'Louisiana',
	'Detroit': 'Detroit Mercy',
	'LIU Brooklyn': 'LIU',
	'Fort Wayne': 'Purdue Fort Wayne'
	}

	#Using team dict
	torvik = torvik.replace({'Teams': mapping_dict})

	#print(torvik.to_string())

	#Merging torvik dataframe into the ncaa dataframe
	ncaa = pd.merge(left = ncaa, right = torvik, how = 'left', on = 'Teams')
	
	return ncaa
