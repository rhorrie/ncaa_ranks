#Finds the KENPOM ranking for each team (my personal favorite)

import pandas as pd
from bs4 import BeautifulSoup
import requests

def kenpom_scrape(ncaa):
	
	#Creating kenpom dataframe
	kenpom = pd.DataFrame()

	#Scraping teams and ranks from kenpom
	url = 'https://kenpom.com/index.php'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	ranks = soup.find_all(attrs = {'class': 'hard_left'})
	teams = soup.find_all(attrs = {'class': 'next_left'})
	
	#Creating arrays
	ranks_array = []
	teams_array = []
	
	#Iterating through to get rank and teams text
	for rank in ranks:
		rank_text = rank.get_text()
		if rank_text != 'Rk' and rank_text != '':
			ranks_array.append(rank_text)
	for team in teams:
		teams_text = team.get_text()
		if teams_text != 'Team' and teams_text != '':
			teams_array.append(teams_text)
		
	#Assigning values to kenpom dataframe
	kenpom['Teams'] = teams_array
	kenpom['Ranks'] = ranks_array
	kenpom['Ranks'] = kenpom['Ranks'].astype('int64')

	#Assigning values from kenpom to ncaa dataframe
	ncaa['Teams'] = kenpom['Teams']
	ncaa['KENPOM Ranks'] = kenpom['Ranks']

	return ncaa