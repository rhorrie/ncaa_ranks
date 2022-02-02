#Finds the NET ranking for each team

import pandas as pd
from bs4 import BeautifulSoup
import requests

def net_scrape(ncaa):
	
	net = pd.DataFrame()

	url = 'https://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-net-rankings'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	teams = soup.find_all('td')
	
	ranks_array = []
	teams_array = []
	teams_total_text = []
	
	for team in teams:
		teams_text = team.get_text()
		teams_total_text.append(teams_text)

	y = 1
	for x in range(2, len(teams_total_text), 12):
		teams_array.append(teams_total_text[x])
		ranks_array.append(int(y))
		y = y + 1

	net['Teams'] = teams_array
	net['NET Ranks'] = ranks_array

	mapping_dict = {
	'UConn': 'Connecticut',
	'Saint Mary\'s (CA)': 'Saint Mary\'s',
	'Southern California': 'USC',
	'Miami (FL)': 'Miami FL',
	'St. John\'s (NY)': 'St. John\'s',
	'Ole Miss': 'Mississippi',
	'UNI': 'Northern Iowa',
	'NC State': 'N.C. State',
	'Middle Tenn.': 'Middle Tennessee',
	'Seattle U': 'Seattle',
	'Southern Ill.': 'Southern Illinois',
	'Gardner-Webb': 'Gardner Webb',
	'App State': 'Appalachian St.',
	'Western Ky.': 'Western Kentucky',
	'Sam Houston': 'Sam Houston St.',
	'SFA': 'Stephen F. Austin',
	'Fla. Atlantic': 'Florida Atlantic',
	'Col. of Charleston': 'Charleston',
	#'Louisiana': 'Louisiana Lafayette',
	'ETSU': 'East Tennessee St.',
	'LMU (CA)': 'Loyola Marymount',
	'Nicholls': 'Nicholls St.',
	'Northern Colo.': 'Northern Colorado',
	'Southern U.': 'Southern',
	'Western Ill.': 'Western Illinois',
	'South Fla.': 'South Florida',
	'California Baptist': 'Cal Baptist',
	'Boston U.': 'Boston University',
	'FGCU': 'Florida Gulf Coast',
	'UNCW': 'UNC Wilmington',
	#'Purdue Fort Wayne': 'Fort Wayne',
	'Eastern Wash.': 'Eastern Washington',
	'Ga. Southern': 'Georgia Southern',
	#'Detroit Mercy': 'Detroit',
	'Miami (OH)': 'Miami OH',
	'St. Thomas (MN)': 'St. Thomas',
	#'LIU': 'LIU Brooklyn',
	'Kansas City': 'UMKC',
	'Eastern Ky.': 'Eastern Kentucky',
	'Alcorn': 'Alcorn St.',
	'A&M-Corpus Christi': 'Texas A&M Corpus Chris',
	'Eastern Mich.': 'Eastern Michigan',
	'SIUE': 'SIU Edwardsville',
	'North Ala.': 'North Alabama',
	'Northern Ky.': 'Northern Kentucky',
	'Albany (NY)': 'Albany',
	'N.C. A&T': 'North Carolina A&T',
	'Southeastern La.': 'Southeastern Louisiana',
	'CSU Bakersfield': 'Cal St. Bakersfield',
	'ULM': 'Louisiana Monroe',
	'Loyola Maryland': 'Loyola MD',
	'Southeast Mo. St.': 'Southeast Missouri St.',
	'N.C. Central': 'North Carolina Central',
	'Prairie View': 'Prairie View A&M',
	'UTRGV': 'UT Rio Grande Valley',
	'UIC': 'Illinois Chicago',
	'Army West Point': 'Army',
	'McNeese': 'McNeese St.',
	'UT Martin': 'Tennessee Martin',
	'Western Caro.': 'Western Carolina',
	'Central Ark.': 'Central Arkansas',
	'NIU': 'Northern Illinois',
	'St. Francis Brooklyn': 'St. Francis NY',
	'Southern Miss.': 'Southern Miss',
	'Grambling': 'Grambling St.',
	'Saint Francis (PA)': 'St. Francis PA',
	'Northern Ariz.': 'Northern Arizona',
	'UMES': 'Maryland Eastern Shore',
	'CSUN': 'Cal St. Northridge',
	'Western Mich.': 'Western Michigan',
	'Bethune-Cookman': 'Bethune Cookman',
	'Lamar University': 'Lamar',
	'Central Mich.': 'Central Michigan',
	'Omaha': 'Nebraska Omaha',
	'Charleston So.': 'Charleston Southern',
	'Central Conn. St.': 'Central Connecticut',
	'Ark.-Pine Bluff': 'Arkansas Pine Bluff',
	'UIW': 'Incarnate Word',
	'Mississippi Val.': 'Mississippi Valley St.',
	'Eastern Ill.': 'Eastern Illinois'
	}

	net = net.replace({'Teams': mapping_dict})

	ncaa = pd.merge(left = ncaa, right = net, how = 'left', on = 'Teams')

	return ncaa


