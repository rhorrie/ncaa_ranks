#Finds the AP and Coaches top 25 for each team

import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np

def ap_and_coaches_scrape(ncaa):

	#Creating ap and coaches dataframe
	ap = pd.DataFrame()
	coaches = pd.DataFrame()

	#Scraping to find all teams for each
	url = 'https://www.espn.com/mens-college-basketball/rankings'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	teams = soup.find_all(attrs = {'class' : 'pl3 hide-mobile clr-link underline-hover'})

	#Creating arrays needed
	teams_array = []
	ranks_array = np.arange(1, 26)
	ap_array = []
	coaches_array = []

	#Iterating through to get team texts for array
	for team in teams:
		team_text = team.get_text()
		teams_array.append(team_text)

	#Assigning the proper teams to the proper arrays
	for x in range(0, 50):
		if x < 25:
			ap_array.append(teams_array[x])
		if x >= 25:
			coaches_array.append(teams_array[x])

	#Assigning values to proper dataframes
	ap['Teams'] = ap_array
	ap['AP Ranks'] = ranks_array
	coaches['Teams'] = coaches_array
	coaches['Coaches Ranks'] = ranks_array

	#Creating dict to ensure all team names are the same
	mapping_dict = {
	'Michigan State': 'Michigan St.',
	'UConn': 'Connecticut',
	'Ohio State': 'Ohio St.',
	'Iowa State': 'Iowa St.',
	'Murray State': 'Murray St.'
	}

	#Using dicts
	ap = ap.replace({'Teams': mapping_dict})
	coaches = coaches.replace({'Teams': mapping_dict})

	#Merging and ap dataframe into ncaa dataframe
	ncaa = pd.merge(left = ncaa, right = ap, how = 'left', on = 'Teams')
	ncaa['AP Ranks'] = ncaa['AP Ranks'].fillna(ncaa.mean(axis=1).round(0) + 10)
	
	#Merging  coaches dataframe into ncaa dataframe
	ncaa = pd.merge(left = ncaa, right = coaches, how = 'left', on = 'Teams')
	ncaa['Coaches Ranks'] = ncaa['Coaches Ranks'].fillna(ncaa.mean(axis=1).round(0) + 10)
	ncaa[['AP Ranks', 'Coaches Ranks']] = ncaa[['AP Ranks', 'Coaches Ranks']].astype(int)


	return ncaa

