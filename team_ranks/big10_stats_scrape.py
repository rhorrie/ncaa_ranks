from flask import Flask, request, render_template, session, redirect
import pandas as pd
import requests
from bs4 import BeautifulSoup

def big10_stats_scrape(team, big10):
	url = 'https://www.sports-reference.com/cbb/schools/' + team + '/2022.html'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	stat_table = soup.find('table', {'id': 'schools_per_game'})
	stats = stat_table.find_all('td')

	table_text_array = []
	team_stats_array = [team]
	team_df = pd.DataFrame()

	for stat in stats:
		stat_text = stat.get_text()
		table_text_array.append(stat_text)

	for x in range(0, 23):
		team_stats_array.append(table_text_array[x])

	big10.loc[len(big10)] = team_stats_array


	return(big10)

