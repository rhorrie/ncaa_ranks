#Finds the KENPOM ranking for each team (my personal favorite)

import pandas as pd
from bs4 import BeautifulSoup
import requests

def kenpom_scrape(ncaa):
	
	kenpom = pd.DataFrame()

	url = 'https://kenpom.com/index.php'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	ranks = soup.find_all(attrs = {'class': 'hard_left'})
	teams = soup.find_all(attrs = {'class': 'next_left'})
	
	ranks_array = []
	teams_array = []
	
	for rank in ranks:
		rank_text = rank.get_text()
		if rank_text != 'Rk' and rank_text != '':
			ranks_array.append(rank_text)
	for team in teams:
		teams_text = team.get_text()
		if teams_text != 'Team' and teams_text != '':
			teams_array.append(teams_text)
		
	kenpom['Teams'] = teams_array
	kenpom['Ranks'] = ranks_array

	kenpom['Ranks'] = kenpom['Ranks'].astype('int64')

	ncaa['Teams'] = kenpom['Teams']
	ncaa['KENPOM Ranks'] = kenpom['Ranks']

	return ncaa