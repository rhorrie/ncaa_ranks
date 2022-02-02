#Finds the AP and Coaches top 25 for each team

import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np

def ap_and_coaches_scrape(ncaa):

	ap = pd.DataFrame()
	coaches = pd.DataFrame()

	url = 'https://www.espn.com/mens-college-basketball/rankings'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	teams = soup.find_all(attrs = {'class' : 'pl3 hide-mobile clr-link underline-hover'})

	teams_array = []
	ranks_array = np.arange(1, 26)
	ap_array = []
	coaches_array = []

	for team in teams:
		team_text = team.get_text()
		teams_array.append(team_text)

	for x in range(0, 50):
		if x < 25:
			ap_array.append(teams_array[x])
		if x >= 25:
			coaches_array.append(teams_array[x])

	ap['Teams'] = ap_array
	ap['AP Ranks'] = ranks_array

	coaches['Teams'] = coaches_array
	coaches['Coaches Ranks'] = ranks_array

	mapping_dict = {
	'Michigan State': 'Michigan St.',
	'UConn': 'Connecticut',
	'Ohio State': 'Ohio St.',
	'Iowa State': 'Iowa St.'
	}


	ap = ap.replace({'Teams': mapping_dict})
	coaches = coaches.replace({'Teams': mapping_dict})

	ncaa = pd.merge(left = ncaa, right = ap, how = 'left', on = 'Teams')
	ncaa['AP Ranks'] = ncaa['AP Ranks'].fillna(ncaa.mean(axis=1).round(0))
	ncaa = pd.merge(left = ncaa, right = coaches, how = 'left', on = 'Teams')
	ncaa['Coaches Ranks'] = ncaa['Coaches Ranks'].fillna(ncaa.mean(axis=1).round(0))
	ncaa[['AP Ranks', 'Coaches Ranks']] = ncaa[['AP Ranks', 'Coaches Ranks']].astype(int)


	return ncaa

